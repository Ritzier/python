# Python

## Poetry

Project manager for Python, the project tree is so good

### Project setup

Create a new project, name with `pyproject`

```sh
poetry new pyproject
```

The project tree:

```sh
./pyproject
├── pyproject
│   └── __init__.py
├── tests
│   └── __init__.py
├── pyproject.toml
└── README.md
```

### Run Project With Poetry

1. **Install the project**

```sh
poetry install
```

2. **Define a `main` fuction in project**

`pyproject/__init__.py`:

```python
def main():
    print("Hello")
```

3. **Configure the Run Script in `pyproject.toml`**

`pyproject.toml`:

```toml
[tool.poetry.scripts]
run = "pyproject:main"
```

> **Note:** It's better to use your project name to make it more descriptive

4. **Run the Project Using Peotry**

To run project, use the `poetry run` command

```sh
poetry run run
```

