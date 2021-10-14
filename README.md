# API Food for Fitness Foods LC ( a codesh challenge)

Application entirely written in python using Django, Django REST Framework and Postgres.

### Requirements
- Docker e Docker Compose
- Python 3.6+


### Instructions to run the project
First, download the project and make a virtual enviroment:
```
git clone https://github.com/IsaiasDimitri/[projeto].git 
cd [projeto]
python -m venv .env

. .env/bin/activate # if you are running Linux or
.env\Scripts\activate.bat # if you are inside Windows
```  
The last commands should build our container and up our API at http://localhost:8000:
```
docker-compose build
docker-compose up
``` 

You should see the URL's and a first product, already loaded by using product fixture.

The application sets a cronjob, to automatically feed the database at 1:00am.  
The command that do it can be invoked any time by calling the custom command (inside the container)
```
python manage.py feed_db
```

To stop the application, press CTRL+C.