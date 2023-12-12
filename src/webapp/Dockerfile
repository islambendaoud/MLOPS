FROM python:3.9-slim 
WORKDIR /webapp
RUN pip install mlflow fastapi uvicorn loguru pymongo
COPY app.py .
COPY get_mlflow_model.py .
ARG MLFLOW_SERVER_URI MODEL_NAME MODEL_VERSION
RUN python3 get_mlflow_model.py --mlflow_server_uri $MLFLOW_SERVER_URI --model_name $MODEL_NAME --model_version $MODEL_VERSION --target_path /tmp/sentiment-analyzer-model

RUN pip install -r /tmp/sentiment-analyzer-model/requirements.txt
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0" , "--port", "8000"]
