import click as ck 
import pandas as pd
from sentiment_analyzer.model_manager import ModelManager 

@ck.command()
@ck.option('--inpute_file', '-i' ,  type = ck.Path(), help='input file')
@ck.option('--output_model', '-o', type = ck.Path(), required=True , help='output file')
@ck.option('--model_name', '-m', type = str, required=True , help='model name')
@ck.option('--model_version', '-v', type = str, required=True , help='model version')
@ck.option('--mlflow_url', '-u', type = str, help='mlflow url' , default =  'http://127.0.0.1:5000' )
@ck.option('--text', '-t', type = str, help='text to predict')
def predict(inpute_file  , output_model, model_name , model_version , mlflow_url , text ) : 

    manager = ModelManager(inpute_file , output_model,model_name , model_version , mlflow_url)
    output = manager.predict(text)

    df = pd.read_csv(inpute_file)
    df.drop("polarity" , axis = 1 , inplace = True)
    df["polarity"] = output
    df.to_csv(output_model)
    return ouput
if __name__ == '__main__':
    predict()