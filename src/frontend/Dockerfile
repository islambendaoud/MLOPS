FROM python:3.9-slim 
WORKDIR /frontend
RUN pip install streamlit pymongo
COPY app.py .

EXPOSE 8501
CMD ["streamlit", "run", "app.py"]