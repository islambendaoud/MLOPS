# python class named ModelManager
import mlflow
import pandas as pd
from mlflow.tracking import MlflowClient


class ModelManager:
    def __init__(self, inpute_file, output_model, model_name, model_version, mlflow_url):
        self.inpute_file = inpute_file
        self.output_model = output_model
        self.model_name = model_name
        self.model_version = int(model_version)

        self.mlflow_url = mlflow_url

    def predict(self):
        mlflow.set_tracking_uri(self.mlflow_url)
        print(self.mlflow_url)
        model = mlflow.sklearn.load_model(
            model_uri=f"models:/{self.model_name}/{self.model_version}"
        )
        df = pd.read_csv(self.inpute_file)
        output = model.predict(df["review"])
        return output
    

    def promote(self , status): 
        client = MlflowClient(self.mlflow_url)
        client.transition_model_version_stage(
            name=self.model_name, version=self.model_version, stage=status
            )
        print(f"promoted model {self.model_name} version {self.model_version} to stage {status}")
        return None 
    
    def retrain(self, training_set, training_set_id, register_updated_model):
        mlflow.set_tracking_uri(self.mlflow_url)
        mlflow.set_experiment("model_design_3")
        model = mlflow.sklearn.load_model(
            model_uri=f"models:/{self.model_name}/{self.model_version}"
        )
        df = pd.read_csv(training_set)
        model.fit(df["review"], df["polarity"])
        tags = {"parent_version": self.model_version, 'retrained': 'True' , 'training_set_id': training_set_id}
        if register_updated_model :
            with mlflow.start_run():
                mlflow.sklearn.log_model(model, f"models/{self.model_name}")
                mlflow.set_tags(tags)
        return None 