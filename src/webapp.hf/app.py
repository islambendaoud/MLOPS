from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.sklearn
import numpy as np 
import json
# import loguru
# import logging
from loguru import logger 
from pymongo import MongoClient
import os 
import joblib

usr = os.getenv("MONGO_INITDB_ROOT_USERNAME")
ps = os.getenv("MONGO_INITDB_ROOT_PASSWORD")


# charge the model that is in the /tmp/sentiment-analyzer-model
model = joblib.load("/model/model.pkl")


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
    # loguru.logger.info("Predicting the sentiment of the input reviews")
    try : 
    # use model to predict
        output = model.predict(np.array(input.reviews))
        # cast 0 and 1 to negative and positive
        output = np.where(output==0, "negative", "positive")
        client = MongoClient(f"mongodb://{usr}:{ps}@mongodb:27017")
        db = client["mydatabase"]
        collection = db["mycollection"]
        collection.insert_one({"input": input.reviews, "output": output.tolist()})

        return {"predictions" : output.tolist()}
    except Exception as e:
        logger.error(f"Error : {e}")
        raise e 
    
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

@app.post("/history")
def history():
    """
    get the history in the database , n inputs and outputs"""

    client = MongoClient(f"mongodb://{usr}:{ps}@mongodb:27017")
    db = client["mydatabase"]
    collection = db["mycollection"]
    # get the last n inputs and outputs
    history = collection.find().sort("_id", -1).limit(10)
    # convert the cursor to a list
    history = list(history)
    # convert the _id to string
    for i in range(len(history)):
        history[i]["_id"] = str(history[i]["_id"])
    return history