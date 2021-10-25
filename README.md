# Django PostgreSQL Rest Api

Prereqs: Python 3.9

Clone this repo, then in the directory run

    pipenv install

If pipenv is not installed, run `pip install pipenv`

Run `pip -V` to make sure you are on virtual environment, output should be like

```
pip 21.2.4 from {your_user_dir}\.virtualenvs\imdb_mid_project-ybDDyv4O\lib\site-packages\pip (python 3.9)
```

If you are not on virtual environment, run `pipenv shell`

To run server, run the following

`python manage.py runserver`

## Database

The database of this test is on the Azure cloud

To access with pgAdmin

Click **Add New Server** on the main page of pgAdmin

Name can be whatever

Hostname/address is **imdb-midterm-postgres.postgres.database.azure.com**

The password of the DB server is **!Password**

![](https://i.gyazo.com/57f5a53d4438f17e927336bb41731acb.png)

There is already a database **project_db** I created for testing

In the database, the table **TestApp_table1** is generated by [Django Migrations](https://docs.djangoproject.com/en/3.2/topics/migrations/)

## Test api

Test api with [Postman](https://www.postman.com/downloads/)

### GET

![](https://i.gyazo.com/34494b17325cab4e3f607110cb18c251.png)

### POST

POST to insert data

![](https://i.gyazo.com/3ae349583e2728eea8412cbf443cd821.png)

Verify it's working by using GET

### PUT

PUT to update data

![](https://i.gyazo.com/ed6c744d64f0710ffc3689666359082f.png)

Verify it's working by using GET

### DELETE

![](https://i.gyazo.com/9eb1a7e360ba0ff700d7bedc7beaef5f.png)

Ref:
    
* https://art-of-engineer.blogspot.com/2021/06/python-django-postgresql-rest-api.html
