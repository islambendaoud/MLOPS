import click as ck 
from sentiment_analyzer.model_manager import ModelManager 
import pandas as pd 


@ck.command()
@ck.option('--training-set', '-t' ,  type = ck.Path(), help='input file'  , default = "data/test.csv")
@ck.option('--model_name', '-m', type = str, required=True , help='model name')
@ck.option('--model_version', '-v', type = str, required=True , help='model version')
@ck.option('--mlflow_url', '-u', type = str, help='mlflow url' , default =  'http://127.0.0.1:5000' )
@ck.option('--training-set-id', '-i', type = str, help='id of the training set' )
@ck.option('--register-updated-model', '-r', type = str, help='register-updated-model' )
def retrain(training_set, model_name, model_version, mlflow_url, training_set_id, register_updated_model):
    model_manager = ModelManager(None , None ,model_name , model_version , mlflow_url)
    model_manager.retrain(training_set, training_set_id, register_updated_model)
    print("Model retrained successfully")

