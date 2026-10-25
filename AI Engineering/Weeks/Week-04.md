# 🤖 AI Engineering · Week 04 — ML Fundamentals and the Classifier Boss

> 📅 **Mon 16 Nov 2026 → Sun 22 Nov 2026** · Season 1 — Foundation Forge · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 03](Week-03.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-04.md) · [Week 05 →](Week-05.md)

**Why this week:** AI-engineer interviews still test ML basics: data splits, precision vs recall, overfitting. A classic model is also your cheapest baseline, and in W7 you will check whether an LLM actually beats it. Everything here runs offline on the company laptop with scikit-learn.

## 🗓️ Sessions

### Monday 16 Nov · 45 min — The ML workflow: data splits, baselines and scikit-learn
- 📚 **Learn:** AI > ML > deep learning > GenAI. Supervised learning maps features to labels (classification, regression); unsupervised learning finds structure without labels (clustering). Workflow: split train/validation/test once (stratify for imbalanced classes), fit on train, tune on validation, report test once, and always compare with a dumb baseline. Read: [scikit-learn getting started](https://scikit-learn.org/stable/getting_started.html) (about 10 min). Optional: [Dividing datasets (Google ML Crash Course)](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets).
- 🛠️ **Do:** In `03-ml-basics/01_workflow.ipynb` (`uv add scikit-learn pandas`) load `load_breast_cancer()` (bundled, no download), split 60/20/20 with `stratify` and `random_state=42`, then fit `DummyClassifier(strategy='most_frequent')` and `LogisticRegression(max_iter=5000)`. Report validation accuracy for both. Done when: the notebook shows both scores, the test split is still untouched, and a markdown cell explains why the baseline matters.

### Tuesday 17 Nov · 45 min — Classification metrics: confusion matrix, precision, recall, F1, ROC-AUC
- 📚 **Learn:** Accuracy misleads on imbalanced data. The confusion matrix counts TP, FP, FN, TN; precision = TP/(TP+FP) (how many flagged items are right), recall = TP/(TP+FN) (how many real positives you caught), F1 = their harmonic mean; ROC-AUC measures ranking quality across thresholds, and moving the threshold trades precision for recall. Read: [Accuracy, precision and recall (Google ML Crash Course)](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall). Optional: [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html).
- 🛠️ **Do:** For Monday's model print the validation confusion matrix, compute precision, recall and F1 by hand from its four numbers, and compare with `classification_report`. Use `predict_proba` to try thresholds 0.3, 0.5 and 0.7 and tabulate precision/recall, plus `roc_auc_score`. Done when: hand and library numbers match and you can say which threshold you would choose for cancer screening, and why.

### Thursday 19 Nov · 45 min — Overfitting, regularisation and cross-validation
- 📚 **Learn:** Overfitting = great on training data, poor on new data (high variance); underfitting = too simple (high bias). Fixes: more data, simpler models, regularisation (`C` in LogisticRegression, `max_depth` in trees), early stopping. k-fold cross-validation averages several train/validation splits for a steadier estimate. Read: [Cross-validation (scikit-learn)](https://scikit-learn.org/stable/modules/cross_validation.html) (first section and the k-fold figure). Optional: [Overfitting (Google ML Crash Course)](https://developers.google.com/machine-learning/crash-course/overfitting).
- 🛠️ **Do:** Train `DecisionTreeClassifier` with `max_depth` 1 to 15 and plot train vs validation accuracy with matplotlib (W3). Then run 5-fold `cross_val_score(scoring='f1')` for LogisticRegression with C = 0.01, 1 and 100. Done when: the plot shows where overfitting starts, the CV table lists mean and std per C, and your note names the depth and C you would choose.

### Friday 20 Nov · 45 min — Text as features: bag of words and TF-IDF
- 📚 **Learn:** Models need numbers: `CountVectorizer` turns text into word counts, `TfidfVectorizer` down-weights words that appear everywhere, n-grams keep short phrases; a `Pipeline` chains vectorizer + classifier so exactly the same steps run in training and prediction (no leakage). TF-IDF + logistic regression is the classic fast text baseline. Read: [Feature extraction (scikit-learn)](https://scikit-learn.org/stable/modules/feature_extraction.html) (Text feature extraction: bag of words and tf-idf). Optional: [Pipelines](https://scikit-learn.org/stable/modules/compose.html).
- 🛠️ **Do:** Download the [SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection) zip in your browser and unzip it into `03-ml-basics/data/`. Load it with pandas (tab-separated, no header) and print the class balance. Then fit a `TfidfVectorizer` on 8 job titles and show the top-weighted terms of two titles. Done when: the dataset loads (about 5,574 messages, roughly 13% spam) and you can explain why 'engineer' gets a low weight across job titles.

### Saturday 21 Nov · 45 min — BOSS BATTLE: spam classifier with honest metrics in 45 minutes
- 📚 **Learn:** Rules: 45-minute timer, docs allowed, no AI code generation, commit every 15 minutes. Use a stratified split, `Pipeline(TfidfVectorizer, LogisticRegression)`, a `DummyClassifier` baseline and 5-fold CV. Rubric /100: correct split and no leakage 25, metrics (confusion matrix, P/R/F1, ROC-AUC) 25, baseline comparison 15, 5 analysed errors 20, README 15. Reference: [Classification of text documents (scikit-learn example)](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html).
- 🛠️ **Do:** Ship `03-ml-basics/spam_classifier.py`: train on 80% (stratified), report the test confusion matrix, precision/recall/F1 for 'spam', ROC-AUC and 5-fold CV F1, compare with the baseline, and save 5 misclassified messages with a one-line reason each. Add 2 pytest tests (the pipeline predicts a valid label; no test row appears in training). Done when: the rubric score is 80+, spam F1 is 0.85 or higher, and tag `v1.0-spam-boss` is pushed.

## 📦 Deliverable (by Saturday night)
`03-ml-basics/`: workflow, metrics and overfitting notebooks, a TF-IDF exploration and a tested spam classifier with confusion matrix, P/R/F1, ROC-AUC, cross-validation and error analysis (tag `v1.0-spam-boss`).

## ✅ Self-check (Sunday test preview)
- Why do you need separate validation and test sets?
- Define precision, recall and F1. When do you prefer high recall over high precision?
- A model scores 99% accuracy on data with 1% positives. Is it good? What do you check?
- What is overfitting? Name three ways to reduce it.
- What does k-fold cross-validation give you that a single split does not?
- Why put the vectorizer inside a Pipeline instead of fitting it on all the data first?

## 🚀 Stretch (optional)
Cluster the SMS messages with `KMeans` on TF-IDF vectors (k = 2 to 6) and inspect the top terms per cluster (unsupervised learning), or work through Google ML Crash Course's [logistic regression module](https://developers.google.com/machine-learning/crash-course/logistic-regression).
