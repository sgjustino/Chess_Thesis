# Codebook for `final_data.csv`

This codebook provides detailed descriptions of each column in the `final_data.csv` file, which contains all processed data used for analysis and modeling in step 7 and 8.

## Column Descriptions

- **game_id**: Unique identifier for each chess game.
- **date_played**: The date when the game was played.
- **constellation_ply**: The ply (half-move) number at which the constellation occurred.
- **constellation_str**: String representation of the constellation in Standard Algebraic Notation (SAN), e.g., Bxf6|c3|Bg5|Nc2|O-O|a4|bxa4|Rxa4|a5|Bc4|Rb8.
- **idf**: Inverse Document Frequency score of the constellation, indicating the rarity of the pattern.
- **white_elo**: Elo rating of the white player.
- **black_elo**: Elo rating of the black player.
- **result**: Result of the game (e.g., 1-0, 0-1, 1/2-1/2).
- **player_made**: Indicates which player made the constellation (white or black) - i.e. playing the 1st and 11th ply.
- **white_id**: Unique identifier for the white player.
- **black_id**: Unique identifier for the black player.
- **year_played**: The year in which the game was played.
- **constellation_fen_1** to **constellation_fen_11**: Forsyth-Edwards Notation (FEN) strings representing the chessboard positions for each ply in the constellation.
- **reaction_fen_1**: FEN string representing the chessboard position for the first reaction move to the constellation.
- **const_11_cp**: Centipawn evaluation (depth=20) of the position at the 11th ply of the constellation.
- **const_11_nodes_searched**: Number of nodes searched by the chess engine at the 11th ply of the constellation.
- **const_11_cp_multipv_variability**: Variability in centipawn evaluation across multiple principal variations (multipv=5) at the 11th ply of the constellation.
- **reaction_fen_1_cp**: Centipawn evaluation (depth=20) of the position for the first reaction move.
- **const_1_cp**: Centipawn evaluation (depth=20) of the position at the 1st ply of the constellation.
- **const_1_nodes_searched**: Number of nodes searched by the chess engine at the 1st ply of the constellation.
- **const_1_cp_multipv_variability**: Variability in centipawn evaluation across multiple principal variations (multipv=5) at the 1st ply of the constellation.
- **cp_sd_diff**: Standard deviation of the difference (SDdiff) in centipawn scores between the first and last ply of a given constellation.
- **constellation_cp_change**: Change in centipawn evaluation between the 1st and 11th ply of the constellation.
- **reaction_move_type**: Type of the reaction move (e.g., blunder, mistake, inaccuracy, optimal move).