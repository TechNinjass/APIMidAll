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

### Start SQL Server via docker-compose
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

```bash
export FLASK_ENV=development
export FLASK_APP=app.py
```