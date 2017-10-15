# chess-web

chess-web is the web client for the entire application. It takes cares of displaying the board and updating positions while the battle is occuring.

It relies on flask, including a celery job queuer to start the battle. A communication with a redis instance is required as updating positions relies on a publish–subscribe pattern.

## Installation

### Run with docker

Just build the image from the Dockerfile
```
docker build -t dockerweb:dev .
docker run -p 5000:8000 dockerweb:dev
```

### Run locally

Or install the package on your python environment (don't forget to use virtual environements) and run it:
```
pip install -r requirements.txt
pip install -e .
python manage.py
```
