# ML_Determining_the_cost_of_cars
This project is an example of the application of machine learning to determine the value of used cars. 
The best trained model was  on data from the auto.csv dataset, and then integrated in Api using FastAPI. The web application was packaged in a Docker container.
## Requirements:
* Python 3.10+

## Training and tuning models
Data preprocessing, training and tuning model in jupyter [Determining_the_cost_of_cars.ipynb](https://github.com/Vladruss/ML_Determining_the_cost_of_cars/blob/main/Determining_the_cost_of_cars.ipynb)

## Running the model locally in fastapi
1. Activate the environment and install dependencies
```
source /path/to/venv/bin/activate
pip install -r requirements.txt
```
2. Launch the service
```
uvicorn main:app --reload
```

## Deployment with Docker
1. Build the Docker image
```
docker build -t ml_api .
```
3. Running the Docker image
```
docker run -d -p 8000:8000 ml_api
```
