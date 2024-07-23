# Code and Dataset for Decoding the Middlegame Thesis

## Background
This GitHub repository contains the code and data for the thesis project titled "Decoding the Middlegame: A Novel Quantitative Framework for Evaluating Chess Constellation Complexity." The project focuses on evaluating the complexity of chess middlegames by analysing patterns of moves (termed constellations) using chess engine parameters and pattern frequencies. The goal is to predict the quality of subsequent moves based on specific constellations across the middlegames.

The repository is organised into 9 folders: 8 for each step in the data processing pipeline and 1 for the final dataset. Note that due to ChessBase's licensing terms and intellectual property rights, this repository only includes the final dataset and not the ChessBase Mega Database 2023 or earlier pre-processed files.

## Steps Involved in the Thesis

### 1. Split PGN to CSV Files by Years
Parsing PGN files and splitting game data into yearly CSV files.
- **Subfolders**: 7 folders, one for each year of data.

### 2. Extract Middlegame Data
Extracting data specific to the middlegame phase for each game from the CSV files.
- **Subfolders**: 8 folders, one for each year of data, plus an additional folder for initial analysis on the distribution of Elo ratings and ply count.

### 3. Extract Constellations and Calculate IDF Scores
Extracting chess constellations and calculating their Inverse Document Frequency (IDF) scores.

### 4. Incorporate FEN Data to Constellations
Incorporating Forsyth-Edwards Notation (FEN) data into the constellations for subsequent engine evaluations.
- **Subfolders**: 8 folders, one for each year of data, plus an additional folder for combining the year files.

### 5. Evaluate Chess Engine Parameters
Evaluating and extracting various chess engine parameters using Stockfish 16.0 for the complexity variables. Specifically, to calculate the CP Change, CP Variability, and Nodes Searched for constellations.
- **Subfolders**: Includes the Stockfish 16.0 folder/files.

### 6. Classify Reaction Move to Different Move Types
Classifying reaction moves into different move types (blunder, mistake, inaccuracy, optimal move).

### 7. Examine Move Distribution and Outliers
Analysing the distribution of reaction move types and identifying outliers for complexity variables.

### 8. Multinomial Logistic Regression Modeling and Prediction
Developing a multinomial logistic regression model to predict reaction moves based on the complexity variables.

## Final Data
The `final_data` folder contains `final_data.csv`, which includes all processed and integrated data used for analysis and modeling in steps 7 and 8. The folder also includes `codebook.md`, detailing the descriptions of each column in `final_data.csv`.

### Data Source
The original data used for this project utilised a subset of data from 2015 to 2021 sourced from the [ChessBase Mega Database 2023](https://shop.chessbase.com/en/products/mega_database_2023). Due to ChessBase's licensing terms and intellectual property rights, only the final processed dataset is included in this repository.