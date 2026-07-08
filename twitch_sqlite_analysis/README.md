# Twitch Advanced SQLite Analysis

This portfolio project leverages Python, Pandas, and SQLite to run data pipelines and extract meaningful business insights from streaming data tracking the Top 1000 Twitch Streamers.

### 1. Top 5 Most Streamed Games Overall
| most_streamed_game   |   streamer_count |
|:---------------------|-----------------:|
| Just Chatting        |              257 |
| League of Legends    |               84 |
| Grand Theft Auto V   |               74 |
| VALORANT             |               60 |
| Casino               |               36 |

### 2. Average Followers by Language (Languages with >10 Streamers)
| language   |    avg_followers |   total_streamers |
|:-----------|-----------------:|------------------:|
| Spanish    |      1.77615e+06 |               106 |
| English    |      1.13374e+06 |               401 |
| Portuguese | 775177           |                82 |
| French     | 766026           |                72 |
| Italian    | 740931           |                13 |

### 3. Stream Duration Tiers vs. Average Followers Gained
| stream_length       |   avg_followers_gained |
|:--------------------|-----------------------:|
| Short (Under 4 hrs) |                   3882 |
| Medium (4 to 8 hrs) |                   3375 |
| Long (Over 8 hrs)   |                   2606 |

### 4. Top Games for Individual Streamer Follower Growth
| most_streamed_game   |   avg_followers_gained |
|:---------------------|-----------------------:|
| Fitness & Health     |                   9640 |
| Super Mario Odyssey  |                   9500 |
| Team Fortress 2      |                   8900 |
| GeoGuessr            |                   8460 |
| Madden NFL 24        |                   7574 |

### 5. Streamer Growth Efficiency Profile (Followers Generated per Hour)
| name      | most_streamed_game   |   efficiency_score |
|:----------|:---------------------|-------------------:|
| ninja     | Fortnite             |           15236.6  |
| sypherpk  | Fortnite             |            4381.31 |
| auronplay | Minecraft            |            3636.77 |
| fortnite  | Fortnite             |            3406.72 |
| elmariana | Just Chatting        |            2823.15 |

### 6. Most Optimized Day of the Week to Stream per Game
| most_streamed_game             | best_day   |   avg_growth |
|:-------------------------------|:-----------|-------------:|
| Minecraft                      | Wednesday  |        18808 |
| Fortnite                       | Tuesday    |        10043 |
| Tom Clancy's Rainbow Six Siege | Monday     |         9670 |
| Fitness & Health               | Saturday   |         9640 |
| Super Mario Odyssey            | Tuesday    |         9500 |

