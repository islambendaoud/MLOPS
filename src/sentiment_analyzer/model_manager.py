# python class named ModelManager
import mlflow
import pandas as pd

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