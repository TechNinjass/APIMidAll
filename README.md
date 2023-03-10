#### The IDE must load the Python packages from **venv**

## Environment Settings
### Step 1

- Into the local repository folder, run:

```bash
python3 -m venv ./venv
```

- After activate the Python venv

```bash
source venv/bin/activate
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
