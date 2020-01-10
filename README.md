# Car Owners API  

The goal is to create a REST API that allows the requester to access information on car owners models data.

## :oncoming_automobile: Getting Started

### Prerequisites

```
Django v2
python3
```

### Installation

Please follow the steps below:

Create a new virtual environment for this application and activate it.
[Python 3 Virtual Environment Tutorial](https://docs.python.org/3/tutorial/venv.html)

After activating the virtual environment, point to the root folder of this project and run:
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

## :oncoming_automobile: About the data
The data I provided an interface to is a list of car owners: their names, ages, jobs, countries and genders. In addition to the car model
they own, the year of the model and the car VIN.
The data is fake and it was generated on this website: [mockaroo.com](https://mockaroo.com/)

## Docker commands

Point to the directory where the Dockerfile exists (./carOwners)
```
docker build -t car_owners .

docker run -p 8000:8000 -it --rm car_owners
```
