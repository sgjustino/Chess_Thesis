import pandas as pd
import numpy as np
import os

# Get the current working directory
current_dir = os.getcwd()

# Construct file paths relative to the current working directory
CSV_PATH = os.path.join(current_dir, 'ctp_all_years_FEN_data_analyzed.csv')
OUTPUT_PATH = os.path.join(current_dir, 'ctp_all_years_FEN_data_analyzed.csv')

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(CSV_PATH)

# Calculate the cp change between const_11_cp and constellation_fen_1_cp
df['constellation_cp_change'] = df['const_11_cp'] - df['const_1_cp']

# Calculate the standard deviation of the difference
df['cp_sd_diff'] = np.sqrt(df['const_11_cp_multipv_variability']**2 + df['const_1_cp_multipv_variability']**2)

# Save the updated DataFrame back to the CSV file
df.to_csv(OUTPUT_PATH, index=False)