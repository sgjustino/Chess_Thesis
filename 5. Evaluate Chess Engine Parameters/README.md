# Dataset: Data taken from step 4 - consolidated Fen-incorporated constellation data file.

# Info: 
* In step 1, we use Stockfish (20 depths, multipv=5) to compute the centipawn score and variabilities of the 5 optimal moves (SD) of the constellation 1st ply. 
* In step 2, we use Stockfish (20 depths, multipv=5) to compute the centipawn score, number of nodes searched and the variabilities of the 5 optimal moves (SD) for the constellation 11th ply. 
* In step 3, we calculate the CP_Change between the frist and last ply of the constellation. We then calculate the SDdiff - the standard deviation of the difference (SDdiff) in centipawn scores between the first and last ply of the constellation. These give us the 2 variables for difficulty measure.
* In step 4, we use Stockfish (20 depths, multipv=5) to compute the centipawn score of the 1st reaction move to the constellation.

# Environment: Python Scripts on Windows with Python 3.11.4 and Stockfish Engine 16.0