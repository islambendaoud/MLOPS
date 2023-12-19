import click as ck 
import pkg_resources
import mlflow 
from skops import hub_utils
import sklearn
import tempfile
import skops 
import pandas as pd 


@ck.command()
@ck.option('--model_name', '-m', type = str, required=True , help='model name')
@ck.option('--model_version', '-v', type = str, required=True , help='model version')
@ck.option('--mlflow_url', '-u', type = str, help='mlflow url' , default =  'http://127.0.0.1:5000' )

@ck.option('--data_file', '-d', type = str, required = True)
@ck.option('--hf_id', '-i', type = str, required = True )
@ck.option('--hf_token', '-t', type = str, required = True )

def hf_export( model_name , model_version , mlflow_url , data_file , hf_id , hf_token)  :

     # Créer une instance de ModelManager
    mlflow.set_tracking_uri(mlflow_url)
    print(mlflow_url)
    model = mlflow.sklearn.load_model(
                model_uri=f"models:/{model_name}/{model_version}"
            )
    # put the model in tmp as pickle 
    data = pd.read_csv(data_file)
    with tempfile.TemporaryDirectory() as tmp_path:
        mlflow.sklearn.save_model(model, tmp_path)
        

    
        f = open(tmp_path+ "/requirements.txt", "r")
        requirements = f.readlines()
        requirements.append(f"scikit-learn={sklearn.__version__}")
        hub_utils.init(
        model=tmp_path+"/model.pkl", 
        requirements=requirements, 
        dst=tmp_path + '/tmp',
        task="text-classification",
        data=data,
    )
        hub_utils.push(
            repo_id = hf_id+"/the-very-best-model",
            token = hf_token,
            source = tmp_path+'/tmp',
                    )
    


if __name__ == '__main__':
    hf_export()