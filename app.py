from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
import pandas as pd
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Database setup
conn = sqlite3.connect('votes.db', check_same_thread=False)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS votes
             (voter_id TEXT PRIMARY KEY, candidate TEXT)''')
conn.commit()

# Load voters from CSV
try:
    voters_df = pd.read_csv('voters.csv')
    voters = voters_df[['voter_id', 'voter_name']].astype(
        str).to_dict('records')
except FileNotFoundError:
    print("Error: voters.csv file not found.")
    exit()

# Load candidates
candidates = ["Candidate A", "Candidate B", "Candidate C"]


@app.route('/')
def index():
    return render_template('index.html', candidates=candidates)


@app.route('/get_voter_name', methods=['POST'])
def get_voter_name():
    voter_id = request.form['voter_id']
    voter = next((v for v in voters if v['voter_id'] == voter_id), None)
    if voter:
        return jsonify({'voter_name': voter['voter_name']})
    else:
        return jsonify({'error': 'Invalid Voter ID'}), 404


@app.route('/vote', methods=['POST'])
def vote():
    voter_id = request.form['voter_id']
    candidate = request.form.get('candidate')

    voter = next((v for v in voters if v['voter_id'] == voter_id), None)
    if voter:
        if candidate:
            try:
                c.execute(
                    "INSERT INTO votes (voter_id, candidate) VALUES (?, ?)", (voter_id, candidate))
                conn.commit()
                flash("Vote cast successfully!", "success")
            except sqlite3.IntegrityError:
                flash("Error: Voter ID has already voted.", "danger")
        else:
            flash("Please select a candidate.", "warning")
    else:
        flash("Invalid Voter ID.", "danger")

    return redirect(url_for('index'))


@app.route('/end_election')
def end_election():
    # Save detailed results to results.csv
    results = pd.read_sql_query("SELECT * FROM votes", conn)
    results.to_csv('results.csv', index=False)

    # Calculate vote counts and save to results_summary.csv
    vote_counts = results['candidate'].value_counts().reset_index()
    vote_counts.columns = ['candidate', 'total_votes']
    vote_counts.to_csv('results_summary.csv', index=False)

    flash("Election ended. Results have been saved to results.csv and results_summary.csv.", "info")
    return redirect(url_for('index'))


@app.route('/check_election_status')
def check_election_status():
    return jsonify({'election_ended': 'results_summary.csv' in os.listdir()})



if __name__ == '__main__':
    app.run(debug=True)
