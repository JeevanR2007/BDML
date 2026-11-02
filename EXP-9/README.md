# Experiment 9: Model Deployment with Flask and Docker

This project trains a Decision Tree classifier on the Iris dataset and exposes it through a Flask REST API.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

The API runs at `http://localhost:5000`.

## Test the prediction endpoint

Send a POST request to `http://localhost:5000/predict` with JSON:

```json
{
  "input": [5.1, 3.5, 1.4, 0.2]
}
```

Example response:

```json
{
  "prediction": "setosa"
}
```

## Run with Docker

```bash
docker build -t iris-flask-api .
docker run -p 5000:5000 iris-flask-api
```
