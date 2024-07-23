import pandas as pd
import chess
import chess.engine
import os

# Get the current working directory
current_dir = os.getcwd()

# Construct file paths relative to the current working directory
STOCKFISH_PATH = os.path.join(current_dir, 'stockfish', 'stockfish-windows-x86-64.exe')
CSV_PATH = os.path.join(current_dir, 'ctp_all_years_FEN_data_cleaned.csv')
OUTPUT_PATH = os.path.join(current_dir, 'ctp_all_years_FEN_data_analyzed.csv')

def analyze_fen(fen, player_made):
    # Check if the FEN is NaN or empty
    if pd.isna(fen) or fen.strip() == '':
        return 'NA'
    
    with chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH) as engine:
        try:
            board = chess.Board(fen)
            info = engine.analyse(board, chess.engine.Limit(depth=20), multipv=5)
            score = info["score"].white().score(mate_score=10000)
            
            # Adjust score based on the player who made the move
            if player_made.lower() == 'black':
                score = -score
            
            return score
        except Exception as e:
            print(f"Exception during analysis: {e}")
            return 'NA'

def main():
    df = pd.read_csv(CSV_PATH, keep_default_na=False, na_values='')
    df['reaction_fen_1_cp'] = None  # Initialize the column for centipawn scores

    total_rows = len(df)
    print(f"Total positions to analyze: {total_rows}")

    for index, row in df.iterrows():
        fen_1 = row['reaction_fen_1']
        player_made = row['player_made']
        cp_score = analyze_fen(fen_1, player_made)
        df.at[index, 'reaction_fen_1_cp'] = cp_score

        # Intermediate save for every 1% or at the end of the DataFrame
        if (index + 1) % (total_rows // 100) == 0 or (index + 1) == total_rows:
            df.to_csv(OUTPUT_PATH, index=False)
            print(f"Progress: {((index + 1) / total_rows) * 100:.2f}%, intermediate save completed.")

    # Final save after processing all rows
    df.to_csv(OUTPUT_PATH, index=False)
    print("Final save completed.")

if __name__ == "__main__":
    main()