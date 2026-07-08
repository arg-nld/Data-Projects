import sqlite3
import pandas as pd

# 1. Connect to SQLite (Creates a file named 'twitch.db' automatically if it doesn't exist)
print("Connecting to SQLite database...")
conn = sqlite3.connect('twitch.db')

try:
    # 2. Read the Kaggle CSV data into Python using Pandas
    print("Reading CSV data...")
    csv_file_path = 'twitch_data.csv'
    df = pd.read_csv(csv_file_path)
    
    # 3. Clean up the Column Names
    # SQL databases hate column names with spaces or weird symbols (e.g., 'Channel Name' or 'Watch Time (Hours)')
    # This line converts all column names to lowercase and replaces spaces with underscores
    df.columns = df.columns.str.replace(' ', '_').str.lower()
    df.columns = df.columns.str.replace('(', '').str.replace(')', '') # removes parentheses
    
    print(f"Cleaned Columns: {list(df.columns)}")
    
    # 4. Export the Pandas Dataframe into an SQL Table named 'streamers'
    # if_exists='replace' means if you run this script twice, it will overwrite the table instead of breaking
    print("Writing data into SQL table 'streamers'...")
    df.to_sql('streamers', conn, if_exists='replace', index=False)
    
    print("\n--- SUCCESS! ---")
    print("Your database 'twitch.db' has been created.")
    print("The table 'streamers' is ready for your SQL queries.")

except Exception as e:
    print(f"\nAn error occurred: {e}")
    print("Make sure your Kaggle file is in this folder and named exactly 'twitch_data.csv'")

finally:
    # 5. Close the Database Connection
    # Always close your connections so the database file doesn't get corrupted or locked!
    conn.close()
    print("Database connection closed cleanly.")