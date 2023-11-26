import click as ck 
from sentiment_analyzer.model_manager import ModelManager 
import subprocess
import pkg_resources
@ck.command()
@ck.option('--inpute_file', '-i' ,  type = ck.Path(), help='input file'  , default = "data/test.csv")
@ck.option('--model_name', '-m', type = str, required=True , help='model name')
@ck.option('--model_version', '-v', type = str, required=True , help='model version')
@ck.option('--mlflow_url', '-u', type = str, help='mlflow url' , default =  'http://127.0.0.1:5000' )
@ck.option('--status', '-s', type = str, help='mlflow status' )

def promote(inpute_file  , model_name , model_version , mlflow_url  , status) :
    print("hello world")
    test_result = subprocess.run(["pytest",pkg_resources.resource_filename('sentiment_analyzer', "./tests")], capture_output=False)
    if test_result.returncode == 0:
        print("tests passed , promoting model")
        manager = ModelManager(inpute_file , None ,model_name , model_version , mlflow_url)
        manager.promote(status)
    else : 
        print("tests failed , aborting promotion")
        exit(1)
if __name__ == '__main__':
    promote()