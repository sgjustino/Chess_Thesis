import pandas as pd
import math

def win_percent_from_cp(cp):
    """
    Calculate the winning percentage from centipawn values based on Lichess formula.
    """
    MULTIPLIER = -0.00368208
    win_chance = 2 / (1 + math.exp(MULTIPLIER * cp)) - 1
    win_percent = 50 + 50 * win_chance
    return win_percent

def classify_move_change(before_cp, after_cp):
    """
    Classify the move based on the change in winning percentage from Lichess formula.
    """
    if pd.isna(before_cp) or pd.isna(after_cp):
        return 'NA'
    before_win_percent = win_percent_from_cp(before_cp)
    after_win_percent = win_percent_from_cp(after_cp)
    win_percent_change = after_win_percent - before_win_percent
    if win_percent_change <= -30:
        return 'Blunder'
    elif -30 < win_percent_change <= -20:
        return 'Mistake'
    elif -20 < win_percent_change <= -10:
        return 'Inaccuracy'
    else:
        return 'Optimal'

def classify_move_change_cp(cp_change):
    """
    Classify the move based on the change in centipawn values using Lichess formula.
    """
    if pd.isna(cp_change):
        return 'NA'
    cp_judgements = [
        (-300, 'Blunder'),
        (-100, 'Mistake'),
        (-50, 'Inaccuracy')
    ]
    for threshold, judgement in cp_judgements:
        if cp_change <= threshold:
            return judgement
    return 'Optimal'

# Load CSV file
df = pd.read_csv('ctp_all_years_FEN_data_analyzed.csv')

# Calculate reaction_win_percent_change and move_type for each row
results = df.apply(lambda row: classify_move_change(row['const_11_cp'], row['reaction_fen_1_cp']), axis=1)
df['reaction_move_type'] = results

# Save the modified DataFrame back to a CSV file
df.to_csv('ctp_all_years_FEN_data_analyzed_with_classifications.csv', index=False)