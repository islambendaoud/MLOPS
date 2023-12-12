import click
import mlflow
import mlflow.sklearn
import json
@click.command()
@click.option("--mlflow_server_uri")
@click.option("--model_name")
@click.option("--model_version")
@click.option("--target_path")

def main(mlflow_server_uri, model_name, model_version, target_path):
    mlflow.set_tracking_uri(mlflow_server_uri)
    client = mlflow.client.MlflowClient(mlflow_server_uri)

    model = mlflow.sklearn.load_model(model_uri=f'models:/{model_name}/{model_version}')
    mlflow.sklearn.save_model(model, target_path)
    details = client.get_model_version(name=model_name, version=model_version)
    #open if not exist create if exist overwrite
    io = open(f'{target_path}/model_details.json', 'w')

    json.dump(details.__dict__, io)

if __name__ == "__main__":
    main()