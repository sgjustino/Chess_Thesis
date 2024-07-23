# Dataset: Dataset is taken from step 1 csv files.

# Info: The second step serve to filter the games to only include the middlegame phase. This is done by adapting Stockfish's classical evaluation, which applies a tapered phase evaluation with proportional ratios for middle and endgame calculations. We incorporated the non-pawn material scores from FEN strings as a determining factor for the middle game phase, utilizing Stockfish's limits of 15258 (start of middle game) and 3915 (start of end game). This approach ensures that the constellations we analyse are indicative of the middle game's strategic complexity, tailoring to each game's unique progress. Our dataset was then filtered to include game states where the non-pawn material score fell within the defined range.

![alt text](<Middlegame Extraction.png>)

# Initial Analysis: With the filtered data, an initial examination is conducted to understand the distribution of elo ratings and plys of games.

![alt text](<chessbase elo rating distribution.png>)

# Environment: Kaggle Notebooks (7 instances of 30gb memory ram each)