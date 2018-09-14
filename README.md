
## Setup
1 - Install requirements
````
$ pip install -r requirements.txt
````
2 - Configure the database
````
$ python manage.py migrate
````
## Start the project
In order to start this project you will need to have running Django and Scrapyd at the same time.

In order to run Django
````
$ python manage.py runserver
````
In order to run Scrapyd
````
$ cd scrapy_app
$ scrapyd
````

## After started:
cd into /suziScraper and start job of spider_1:
````
curl http://localhost:6800/schedule.json -d project=default -d spider=bottoms
````
and spider_2:
````
curl http://localhost:6800/schedule.json -d project=default -d spider=exclusives
````
then open http://127.0.0.1:6800/jobs to check jobs process.
The crawled data will be automatically saved in the Django models
(it was cool to get experience with scrapy)

## After finished:
open
http://127.0.0.1:8000/
and press *OK* to get data in Json
