# Python Flask Voting System

## A Base Voting System with Python and Flask

The program features a main voting page for voters to enter their Voter ID and select their canditate for voting and submit their votes. All the votes will be temporarily stored in a sqlite database file and finally export the votes to csv file once the voting gets finished.

## Features

1. **Easy to Configure**
   - The program features a nice sleek UI with its own styling and themes
   - Program can be modified according to it's usage from the main source code itself.

2. **Voting Process**
   - Voter ID can be added from a sperate CSV file along with their name
   - Voters can easily click on the canditate and submit their vote.

3. **Results**
   - Results will be generated into two seperate files with one file revealing which voter's choice and other file revealing the number of votes for each canditates.
## Technologies Used

- Python
- Flask
- SQLite (for database management)
- Pandas (for data manipulation)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/Sidharth-Prabhu/Flask-Voting-System.git
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the application:

   ```
   //Create and activate virtual environment.
   python app.py
   ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make changes and commit (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new pull request.
