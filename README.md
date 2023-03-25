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
pip install -r requirements.txt
```

### Important Notes
- If new or updated dependency package was added in the project structure, the **requirements.txt** must be updated

```bash
pip freeze > requirements.txt
```

### Start  via docker-compose
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

### Start mode debug
```bash
export FLASK_ENV=development
export FLASK_APP=app.py
```

## Executing Database 

### For you to control changes in the database follow the instructions below:
  
  1. Open the "flaskr" folder in console with following command:
  ```bash
  cd flaskr
  ```

  2. Open new terminal using shell
  ```bash
     flask shell
  ```
  3. Imports dependencies 
  ```bash
    from flaskr.db import db_instance
    from flaskr.models import *
  ```

  4. Then create database:
  ```bash
     db_instance.create_all()
  ```
