import warnings 
import pandas as pd
from pathlib import Path

from loan_default_risk.utils.common import save_json
from loan_default_risk.entity.config_entity import ModelEvaluationConfig

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import dagshub
import mlflow

import joblib 

warnings.filterwarnings('ignore')

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config


   
    def eval_metrics(self, actual, pred):
        acc = accuracy_score(y_pred = pred, y_true = actual)
        precision = precision_score(y_pred = pred, y_true = actual)
        recall = recall_score(y_pred = pred, y_true = actual)
        f1 = f1_score(y_pred = pred, y_true = actual)
        return acc, precision, recall, f1
   

    def log_into_mlflow(self):
        

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)


        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]


        dagshub.init(repo_owner='revanth-kumar-01-ai', repo_name='Loan-Default-Risk-Prediction', mlflow=True)
        
        
        with mlflow.start_run():


            predicted_qualities = model.predict(test_x)


            (acc, precision, recall, f1) = self.eval_metrics(test_y, predicted_qualities)
           
            # Saving metrics as local
            scores = {"accuracy_score": acc, "precision_score": precision, "recall_score": recall, "f1": f1}
            save_json(path=Path(self.config.metric_file_name), data=scores)


            mlflow.log_params(self.config.all_params)


            mlflow.log_metric("accuracy_score", acc)
            mlflow.log_metric("precision_score", precision)
            mlflow.log_metric("recall_score", recall)
            mlflow.log_metric("f1", f1)


