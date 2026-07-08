import sqlite3
import pandas as pd

# Define queries to execute and export
QUERIES = {
    "Top 5 Most Streamed Games Overall": """
        SELECT most_streamed_game, COUNT(*) as streamer_count
        FROM streamers
        GROUP BY most_streamed_game
        ORDER BY streamer_count DESC
        LIMIT 5;
    """,
    
    "Average Followers by Language (Languages with >10 Streamers)": """
        SELECT language, ROUND(AVG(total_followers), 0) as avg_followers, COUNT(*) as total_streamers
        FROM streamers
        GROUP BY language
        HAVING total_streamers > 10
        ORDER BY avg_followers DESC
        LIMIT 5;
    """,
    
    "Stream Duration Tiers vs. Average Followers Gained": """
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
    """,
    
    "Top Games for Individual Streamer Follower Growth": """
        SELECT most_streamed_game, ROUND(AVG(followers_gained_per_stream), 0) AS avg_followers_gained
        FROM streamers
        GROUP BY most_streamed_game
        ORDER BY avg_followers_gained DESC
        LIMIT 5;
    """,
    
    "Streamer Growth Efficiency Profile (Followers Generated per Hour)": """
        WITH StreamerEfficiency AS (
            SELECT name, most_streamed_game, total_time_streamed, total_followers,
            (total_followers * 1.0 / total_time_streamed) AS followers_per_hour_streamed
            FROM streamers
            WHERE total_time_streamed > 1000 
        )
        SELECT name, most_streamed_game, ROUND(followers_per_hour_streamed, 2) AS efficiency_score
        FROM StreamerEfficiency
        ORDER BY efficiency_score DESC
        LIMIT 5;
    """,
    
    "Most Optimized Day of the Week to Stream per Game": """
        WITH GameDayStats AS (
            SELECT most_streamed_game, day_with_most_followers_gained AS best_day,
            AVG(followers_gained_per_stream) AS avg_growth
            FROM streamers
            GROUP BY most_streamed_game, day_with_most_followers_gained
        ),
        RankedDays AS (
            SELECT most_streamed_game, best_day, ROUND(avg_growth, 0) AS avg_growth,
            ROW_NUMBER() OVER(PARTITION BY most_streamed_game ORDER BY avg_growth DESC) as rank
            FROM GameDayStats
        )
        SELECT most_streamed_game, best_day, avg_growth
        FROM RankedDays
        WHERE rank = 1
        ORDER BY avg_growth DESC
        LIMIT 5;
    """
}

# Base README header
markdown_output = (
    "# Twitch Advanced SQLite Analysis\n\n"
    "This portfolio project leverages Python, Pandas, and SQLite to run data pipelines "
    "and extract meaningful business insights from streaming data tracking the Top 1000 Twitch Streamers.\n\n"
)

# Execute queries and append results to markdown output
with sqlite3.connect('twitch.db') as conn:
    for i, (title, sql_query) in enumerate(QUERIES.items(), 1):
        df = pd.read_sql_query(sql_query, conn)
        
        print(f"\n--- {title.upper()} ---")
        print(df)
        
        markdown_output += f"### {i}. {title}\n"
        markdown_output += df.to_markdown(index=False) + "\n\n"

# Export final compiled markdown
with open("README.md", "w") as file:
    file.write(markdown_output)

print("\nAnalysis complete. README.md updated successfully.")