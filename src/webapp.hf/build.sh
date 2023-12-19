
docker build\
    -t sentiment-analyzer:1.0-model_3_hyperopt-2\
    --build-arg MLFLOW_SERVER_URI=http://host.docker.internal:5000\
    --build-arg MODEL_NAME=model_3_hyperopt\
    --build-arg MODEL_VERSION=2\
    .