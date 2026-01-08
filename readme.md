Business Case: Predicting Online Purchase Intent

Overview

This repository contains the code and analysis for a data science business case focused on predicting online purchasing intent using session-level behavioural data, supplemented with a macro level retail demand indicator.

The project is framed as a hypothetical consulting engagement, where the objective is to develop an interpretable predictive model that can support evidence based decision making in a digital retail context.

The workflow covers data ingestion, preprocessing, feature engineering, model training, evaluation, visualisation, and basic pipeline testing to ensure reproducibility and robustness.


To clone the Repo :

git clone https://github.com/Bandohhh/business_case.git
cd business_case


To Create a virtual enviroment:
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows

To install packages needed to run the code :
pip install -r requirements.txt


To Run the model, train and generate figures:
python -m src.model

To generate evaluation output (Confusion matrix ,Classification metrics (precision, recall, F1, ROC–AUC)):
python -m src.evaluate

All visual outputs can be viewed in the figures folder 

To run all test:
pytest