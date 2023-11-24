import click as ck 
import pandas as pd
from sentiment_analyzer.model_manager import ModelManager 

@ck.command()
@ck.option('--inpute_file', '-i' ,  type = ck.Path(), help='input file'  , default = "data/test.csv")
@ck.option('--model_name', '-m', type = str, required=True , help='model name')
@ck.option('--model_version', '-v', type = str, required=True , help='model version')
@ck.option('--mlflow_url', '-u', type = str, help='mlflow url' , default =  'http://127.0.0.1:5000' )
@ck.option('--status', '-s', type = str, help='mlflow status' )

def promote(inpute_file  , model_name , model_version , mlflow_url  , status) : 

    manager = ModelManager(inpute_file , None ,model_name , model_version , mlflow_url)
    manager.promote(status)

if __name__ == '__main__':
    promote()