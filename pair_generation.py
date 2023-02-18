import csv
import json

# Read CSV file
with open('scoring.csv', 'r') as f:
    data = list(csv.reader(f))
    headers = data[0]
    data = data[1:]

# Create prompt and completion pairs
pairs = []
for player in data:
    prompt = f"Write a summary of {player[headers.index('Player')]}'s statistics:"
    completion = f"{player[headers.index('Player')]} played {player[headers.index('GP  Games played')]} games, starting {player[headers.index('GS  Games started')]} of them. He had an average of {player[headers.index('MPG  Minutes Per Game')]} minutes per game, scoring {player[headers.index('PPG  Points Per Game')]} points per game. He made {player[headers.index('FGM  Field Goals Made')]} out of {player[headers.index('FGA  Field Goals Attempted')]} field goals, for a field goal percentage of {player[headers.index('FG%  Field Goal Percentage')]}. He made {player[headers.index('3FGM  Three-Point Field Goals Made')]} out of {player[headers.index('3FGA  Three-Point Field Goals Attempted')]} three-point field goals, for a three-point field goal percentage of {player[headers.index('3FG%  Three-Point Field Goal Percentage')]}. He made {player[headers.index('FTM  Free Throws Made')]} out of {player[headers.index('FTA  Free Throws Attempted')]} free throws, for a free throw percentage of {player[headers.index('FT%  Free Throw Percentage')]}. He plays as {player[headers.index('Position')]} for the {player[headers.index('Team')]}."
    pairs.append({"prompt": prompt, "completion": completion})

# Export to JSON file
with open('prompt_completion_pairs.json', 'w') as f:
    json.dump(pairs, f)

