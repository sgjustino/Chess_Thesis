import pandas as pd
import chess
import chess.engine
import os
import statistics
import numpy as np

# Get the current working directory
current_dir = os.getcwd()

# Construct file paths relative to the current working directory
STOCKFISH_PATH = os.path.join(current_dir, 'stockfish', 'stockfish-windows-x86-64.exe')
CSV_PATH = os.path.join(current_dir, 'ctp_all_years_FEN_data_cleaned.csv')
OUTPUT_PATH = os.path.join(current_dir, 'ctp_all_years_FEN_data_analyzed.csv')

def analyze_fen(engine, fen, player_made):
    try:
        board = chess.Board(fen)
        scores = []  # Collect scores for score variability calculation
        nodes_list = []  # Collect nodes for nodes searched variability calculation
        
        # Analyse the position at a fixed depth with MultiPV enabled
        analysis = engine.analyse(board, chess.engine.Limit(depth=20), multipv=5)
        
        # Collect scores and nodes from all principal variations
        for pv_info in analysis:
            # Ensure 'score' and 'nodes' are present in the info dictionary
            if 'score' in pv_info and 'nodes' in pv_info:
                score = pv_info["score"].white().score(mate_score=10000)
                # Adjust score based on the player who made the move
                if player_made == "black":
                    score = -score
                scores.append(score)
                nodes_list.append(pv_info["nodes"])
        
        # Calculate variability (standard deviation) of CP scores
        score_variability = statistics.stdev(scores) if len(scores) > 1 else 0
        
        # Use the score from the first principal variation
        final_score = scores[0] if scores else None
        total_nodes_searched = sum(nodes_list)  # Sum of nodes searched across all PVs
        
        return final_score, total_nodes_searched, score_variability, False
    except Exception as e:
        print(f"Exception during analysis: {e}")
        return None, None, None, True

def main():
    df = pd.read_csv(CSV_PATH, keep_default_na=False, na_values='')

    # Ensure all necessary columns exist
    columns = ['const_11_cp', 'const_11_nodes_searched', 'const_11_cp_multipv_variability']
    for column in columns:
        if column not in df.columns:
            df[column] = np.nan

    unprocessed_df = df[pd.isna(df['const_11_cp'])]

    total_rows = len(unprocessed_df)
    print(f"Total positions to analyze: {total_rows}")

    for index, row in unprocessed_df.iterrows():
        fen_11 = row['constellation_fen_11']
        player_made = row['player_made']

        try:
            with chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH) as engine:
                cp_score, nodes_searched, score_variability, error_occurred = analyze_fen(engine, fen_11, player_made)
                
                if not error_occurred:
                    # Update the original DataFrame with analysis results
                    df.at[index, 'const_11_cp'] = cp_score
                    df.at[index, 'const_11_nodes_searched'] = nodes_searched
                    df.at[index, 'const_11_cp_multipv_variability'] = score_variability
                else:
                    df.at[index, 'const_11_cp'] = 'NA'
        except chess.engine.EngineTerminatedError as e:
            print(f"Engine terminated unexpectedly for FEN {fen_11}: {e}")
            df.at[index, 'const_11_cp'] = 'NA'

        # Intermediate save for every 100 rows or at the end of unprocessed rows
        if (index + 1) % 100 == 0 or (index + 1) == total_rows:
            df.to_csv(OUTPUT_PATH, index=False)
            print(f"Progress: {((index + 1) / total_rows) * 100:.2f}%, intermediate save completed.")

    # Final save after processing all unprocessed rows
    df.to_csv(OUTPUT_PATH, index=False)
    print("Final save completed.")


if __name__ == "__main__":
    main()