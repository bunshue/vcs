import pandas as pd

df = pd.read_csv("NBA_players_salary_stats_2018.csv")
df.plot(kind="scatter", x="PTS", y="salary", 
        title="Scatter Plot of NBA Salary and PTS")


