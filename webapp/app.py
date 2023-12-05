from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.sklearn
import numpy as np 
import json
# charge the model that is in the /tmp/sentiment-analyzer-model
mlflow_model_path = "/tmp/sentiment-analyzer-model"
# load the model
model = mlflow.sklearn.load_model(mlflow_model_path)


app=FastAPI(title ="Sentiment Analyzer API", version="1.0" , description="Sentiment Analyzer API")

class PredictInput(BaseModel):
    reviews: list[str]



@app.post("/predict")
def predict(input: PredictInput):
    """
    Predict the sentiment of the input reviews

    **param** : text to review

    **return** : dict
    """
    # use model to predict
    output = model.predict(np.array(input.reviews))
    # cast 0 and 1 to negative and positive
    output = np.where(output==0, "negative", "positive")

    return {"predictions" : output.tolist()}

@app.post("/get_details")
def get_details(): 
    """
    Get the details of the model

    **return** : dict
    """
    # load the model details
    details = json.load(open(f'{mlflow_model_path}/model_details.json', 'r'))
    return details

@app.post("/get_stage")
def get_stage():
    """
    Get the stage of the model

    **return** : dict
    """
    # load the model details
    details = json.load(open(f'{mlflow_model_path}/model_details.json', 'r'))
    return {"stage" : details["_current_stage"]}