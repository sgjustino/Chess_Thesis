# Dataset: Data taken from step 6 move-classified file (final_data.csv found in final_data folder)

# Info: 
* A multinomial logistic regression using scikit-learn's LogisticRegression class was applied to move types (Blunder, Mistake, Inaccuracy, Optimal), modeling pattern complexity variables (change in centipawn score, standard deviation difference, nodes searched, IDF).
* Data preprocessing removed error FEN rows and checkmate situations, yielding 106,810 occurrences from 2,277 constellations in 31,688 games by 19,215 unique players.
* Model validation employed an 80/20 train-test split, randomly distributing unique constellation patterns to prevent correlational issue.
* The model utilise 'LBFGS' solver and class imbalance was addressed using scikit-learn's cost-sensitive learning (class_weight='balanced').
* Model assessment included performance metrics (weighted precision, recall, F1 score), coefficient analysis, confusion matrix visualisation, ROC-AUC curve plotting, and permutation testing via Monte Carlo resampling.
* Players' Elo ratings and rating differences were initially considered but omitted from the final model due to negligible impact.

# Assumptions:
* Independence of Observations: While perfect independence between observations cannot be assumed in chess gameplay, our model treats each constellation-move_type pair as a separate instance. The random distribution of unique constellations across training and test sets helps mitigate potential dependencies. Multinomial logistic regression is applied with the understanding that minor violations of the independence assumption are often tolerable, especially with large datasets. Model performance metrics and cross-validation are used to validate the approach.
* Multicollinearity: Variance Inflation Factor (VIF) scores were computed for all predictors. The results indicated no significant multicollinearity concerns, ensuring the stability and interpretability of our model coefficients.
* Non-Linearity: Multinomial logistic regression assumes linearity in the log-odds of class probabilities but is generally more robust to non-linear relationships than its binary counterpart due to its ability to capture complex decision boundaries across multiple classes. To optimise our model efficiently and address potential non-linearity, we employed the LBFGS (Limited-memory Broyden–Fletcher–Goldfarb–Shanno) solver. This choice was made for its effectiveness in handling large datasets and high-dimensional spaces, its efficiency in optimising multinomial logistic regression models, and its ability to navigate potential non-linear relationships through adaptive step size and Hessian matrix approximation. While LBFGS does not directly transform non-linear relationships, it helps the model find the best linear approximation of potentially non-linear patterns in the data, balancing interpretability with the flexibility needed to capture complex chess position dynamics.

![alt text](<MLR Model Figure.png>)

# Environment: Kaggle Notebooks (Python 3.10.13, 1 instances of 30gb memory ram)