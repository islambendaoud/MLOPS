import os
import pytest
import mlflow
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score


TEST_MODEL_NAME = os.getenv("TEST_MODEL_NAME")
TEST_MODEL_VERSION = os.getenv("TEST_MODEL_VERSION")
TEST_TEST_TEST = os.getenv("TEST_TEST_TEST")
TEST_FILE = os.getenv("TEST_FILE")
mlflow.set_tracking_uri("http://127.0.0.1:5000")



def test_model():
    # charge the model from mlflow
    model = mlflow.sklearn.load_model(
        model_uri=f"models:/{TEST_MODEL_NAME}/{TEST_MODEL_VERSION}"
    )
    # test the model
    # input data
    input_data = ["The movie is very good I like it a lot. It is very interesting"]
    # expected output
    # predict with the model
    output = model.predict(input_data)
    # test the output
    assert(output == 0 or output == 1) 
    # input data
    input_data = np.array([1,2,4,5,6])

    # test that predict error since the model uses a string as input
    with pytest.raises(AttributeError) as e_info:
        output = model.predict(input_data)
    

    #Vérifier que le modèle fonctionne avec des entrée unusuelles aussi (par exemple caractères spéciaux, entrée vide)
    input_data = [""]
    output = model.predict(input_data)
    assert(output == 0 or output == 1)

    df_t = pd.read_csv(TEST_FILE)
    output = model.predict(df_t["review"])
    assert(len(output) == len(df_t["review"]))
    y = df_t["polarity"]
    assert(accuracy_score(y, output) > float(TEST_TEST_TEST)) 


