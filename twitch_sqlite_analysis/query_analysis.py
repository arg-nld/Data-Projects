import sqlite3
import pandas as pd

# Connect to the database we just built
conn = sqlite3.connect('twitch.db')

# ---------------------------------------------------------
# Query 1: What are the top 5 most streamed games overall?
# ---------------------------------------------------------
print("\n--- TOP 5 MOST STREAMED GAMES ---")
query1 = """
SELECT most_streamed_game, COUNT(*) as streamer_count
FROM streamers
GROUP BY most_streamed_game
ORDER BY streamer_count DESC
LIMIT 5;
"""
print(pd.read_sql_query(query1, conn))


# ---------------------------------------------------------
# Query 2: Which languages generate the most followers on average?
# ---------------------------------------------------------
print("\n--- AVG FOLLOWERS BY LANGUAGE ---")
query2 = """
SELECT language, ROUND(AVG(total_followers), 0) as avg_followers, COUNT(*) as total_streamers
FROM streamers
GROUP BY language
HAVING total_streamers > 10  -- Only show languages with more than 10 top streamers
ORDER BY avg_followers DESC
LIMIT 5;
"""
print(pd.read_sql_query(query2, conn))


# ---------------------------------------------------------
# Query 3: Does streaming longer mean you gain more followers?
# ---------------------------------------------------------
print("\n--- STREAM DURATION VS FOLLOWERS GAINED ---")
query3 = """
SELECT 
    CASE 
        WHEN average_stream_duration < 4 THEN 'Short (Under 4 hrs)'
        WHEN average_stream_duration BETWEEN 4 AND 8 THEN 'Medium (4 to 8 hrs)'
        ELSE 'Long (Over 8 hrs)'
    END as stream_length,
    ROUND(AVG(followers_gained_per_stream), 0) as avg_followers_gained
FROM streamers
GROUP BY stream_length
ORDER BY avg_followers_gained DESC;
"""
print(pd.read_sql_query(query3, conn))

# Always close the connection
conn.close()