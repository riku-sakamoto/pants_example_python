# Example Python Monorepo for poetry users

This is an example repository when you create monorepo by pants from repositories managed by poetry.

In order to run this repository, `pants` binary is necessary. Please install beforehand.

* pants: https://www.pantsbuild.org/


## Configuration

Configuration of directories is shown below.

```text
.
├── libs
│   └── fizzbuzz
│       ├── fizzbuzz/
│       ├── pyproject.toml
│       ├── README.md
│       └── tests/
├── pants.toml
├── projects
│   ├── project_a
│   │   ├── pyproject.toml
│   │   └── src/
│   └── project_b
│       ├── pyproject.toml
│       └── src/
```

Dependencies of libraries is shown below.

```mermaid
```


## Example Goals

### Test fizzbuzz library

```bash
pants libs/fizzbuzz ::
```

### Format all files

```bash
pants fmt ::
```

### Run project code

```bash
pants run projects/project_a/src/main.py -- --show-fizzbuzz
```

### Generate lock files

```bash
pants generate-lockfiles
```


## Refenrece

* [pants document](https://www.pantsbuild.org/)
* [example-python(GitHub)](https://github.com/pantsbuild/example-python/tree/main)
