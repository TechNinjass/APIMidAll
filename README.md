# MidAll - Back-end Project 

This is built with Flask, Flask-RESTful and Flask-SQLAlchemy.
## Pre-requirements
- [Python 3.x LTS](https://www.python.org/downloads/)
- [Docker v20.10.12+](https://docs.docker.com/get-docker/)
- [Docker Compose v2.2.3+](https://docs.docker.com/compose/install/) - other versions [see here](https://github.com/docker/compose/releases)

## Recommended IDEAs
 - [VSCode with Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
 - [IntelliJ with Python Plugin](https://plugins.jetbrains.com/plugin/631-python)

#### The IDE must load the Python packages from **venv**
## Environment Settings
### Step 1

- Into the local repository folder, run:

```bash
python -m venv venv
```

- After activate the Python venv

```bash
source venv/Scripts/activate
```

- Update **pip** package

```bash
python -m pip install -U pip
```
### Step 2

- Installing the Python project's dependency packages

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```
### Important Notes
- If new or updated dependency package was added in the project structure, the **requirements.txt** must be updated

```bash
pip freeze > requirements.txt
```
## Executing Database Migrations using Flask-Migrate
### For you to control changes in the database follow the instructions below:
  
  1. Open the "flaskr" folder in console with following command:
  ```bash
  cd flaskr
  ```

  2. Create a migration repository. If the **migrations** folder already exists this command is not necessary.
  ```bash
    python -m flask db init
  ```
  3. To build a new migration, for example, "Initial migration"
  ```bash
    python -m flask db migrate -m "Initial migration."
  ```

  4. Then you can apply the migration to the database:
  ```bash
    python -m flask db upgrade
  ```

**Notes**: To see all the commands that are available run this command:
  ```bash
    python -m flask db --help
  ```

  Official documentation for [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)

## Set paths and values in application

Before run the statements below, edit the value of parameter
**FLASKR_DEV_DIR** in the **.env** file of the **docker** folder with the
absolute path of **flaskr/** project folder in you host and declare absolute
path of cloud folder in **config_credentials.py** file
## Running Flask back-end via docker-compose
### Start all back-end via docker-compose

```bash
cd docker
docker-compose build --no-cache
docker-compose up --force-recreate -d ; docker-compose logs -f
```
### To stop docker docker-compose

```bash
# In the project root folder
cd docker
docker-compose down --remove-orphans
```
### Run application for development

1. Declare as variable for debugging
```bash
    export FLASK_ENV=development
    export FLASK_APP=app.py
```
2.Enter the flaskr folder and run
```bash
    cd flaskr
    flask run
```


