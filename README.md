# AI Engineering - Live Class Code Repository

Welcome! This repository contains all the code, notes, and exercises from the live AI Engineering classes. It is designed to be a beginner-friendly learning resource for anyone starting their journey into AI Engineering with Python.

---

## About This Repository

This project tracks the topics covered in each lecture. Each session's learnings are documented here along with the relevant commands, concepts, and code examples. The goal is to build a strong foundation in Python project setup, dependency management, version control, and eventually AI/ML tooling.

---

## Lecture : 26-09-2026

### What we covered today

- **Git basics**: initializing a repository, connecting to GitHub, authenticating with a Personal Access Token (PAT), pulling remote changes, and pushing local commits.
- **Project setup with uv**: creating a modern Python project using the `uv init` command.
- **Dependency management**: adding packages like Pydantic using `uv add`.
- **Lock files**: understanding how `uv.lock` ensures reproducible environments.
- **README and project structure**: documenting the repository for future learners.

---

## What is uv?

`uv` is a modern, extremely fast Python package and project manager written in Rust. It combines the functionality of multiple older tools into one:

- Python installation and version management
- Virtual environment creation
- Package installation
- Dependency resolution
- Lock file generation
- Project management

Instead of running multiple commands like:

```bash
python -m venv .venv
source .venv/bin/activate
pip install pydantic
```

You can do the same with:

```bash
uv add pydantic
```

`uv` automatically updates `pyproject.toml`, installs the package, and keeps the lock file in sync.

---

## `pyproject.toml` is like `pom.xml`

If you come from a Java or Maven background, `pyproject.toml` serves the same purpose as `pom.xml`:

| Maven | Python with uv |
|-------|----------------|
| `pom.xml` | `pyproject.toml` |
| `<dependency>` blocks | `dependencies` list |
| Manual version management | `uv add package-name` |
| Build plugins | `[build-system]` section |

Example of adding a dependency:

```bash
uv add pydantic
```

This updates `pyproject.toml`:

```toml
dependencies = [
    "pydantic>=2.13.5",
]
```

---

## What is `uv.lock`?

`uv.lock` is a lock file that records the exact versions of every package and its transitive dependencies installed in your environment.

Benefits of using a lock file:

- **Reproducibility**: everyone on the team gets the same package versions.
- **Stability**: avoids unexpected breaking changes from automatic updates.
- **Faster installs**: dependency resolution is already done.

It is similar to:

- `package-lock.json` in Node.js
- `yarn.lock` in Yarn
- `requirements.txt` with pinned versions

Useful commands:

```bash
uv lock      # update the lock file
uv sync      # install packages exactly as listed in uv.lock
```

---

## What is Pydantic?

Pydantic is a Python library for data validation and settings management. It uses Python type hints to validate that your data matches the expected structure.

### Why use Pydantic?

- Automatic data validation
- Clear and helpful error messages
- Easy conversion between Python objects and JSON
- Less manual error checking
- Widely used in FastAPI, LangChain, and AI/ML projects

### Example

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

user = User(name="Pritish", age=25, email="pritish@example.com")
print(user)
```

If invalid data is passed, Pydantic raises a clear error:

```text
age: Input should be a valid integer
email: The email address is not valid
```

---

## Project Structure

```text
ai_engg_personal_course_code/
├── .gitignore                  # Files and folders ignored by Git
├── .python-version             # Python version used by the project
├── pyproject.toml              # Project configuration (like Maven's pom.xml)
├── uv.lock                     # Exact dependency versions for reproducibility
├── README.md                   # This file
└── src/
    └── ai_engg_live/
        └── __init__.py         # Main Python package and entry point
```

### File descriptions

- **`README.md`**: Project overview and lecture notes.
- **`.gitignore`**: Prevents temporary or environment-specific files from being committed.
- **`pyproject.toml`**: Defines project metadata, dependencies, and build settings.
- **`.python-version`**: Stores the Python version so `uv` or `pyenv` can use it automatically.
- **`src/ai_engg_live/__init__.py`**: The Python package's main module. Contains the `main()` function as the project entry point.
- **`uv.lock`**: Lock file that pins exact dependency versions.

---

## Note on `.py` vs `.ipynb` Files

- **`.py` files**: Used for production-grade applications and final scripts.
- **`.ipynb` files (Jupyter Notebooks)**: Used for learning, experimentation, and quick interactive changes.

In this course, we will use both. Notebooks help us explore ideas quickly, while `.py` files help us structure clean, reusable code.

---

## Common Commands

### Git commands

```bash
git init -b main                                             # Initialize a Git repo on the main branch
git remote add origin <repo-url>                             # Connect to a GitHub repository
git pull origin main --rebase                                # Pull remote changes and rebase local commits
git add .                                                    # Stage all changes
git commit -m "Your commit message"                          # Commit staged changes
git push origin main                                         # Push commits to GitHub
```

### uv commands

```bash
uv init                                                      # Create a new Python project
uv add <package-name>                                        # Add a dependency
uv remove <package-name>                                     # Remove a dependency
uv lock                                                      # Update the lock file
uv sync                                                      # Install dependencies from uv.lock
uv run python <file.py>                                      # Run a Python file inside the project environment
```

---

## How to Use This Repository

1. Clone the repository:
   ```bash
   git clone https://github.com/praj031/ai_engg_personal_course_code.git
   cd ai_engg_personal_course_code
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

3. Run the main script:
   ```bash
   uv run python src/ai_engg_live/__init__.py
   ```

---

## Author

- **Pritish Raj** - [pritishraj.official@gmail.com](mailto:pritishraj.official@gmail.com)

---

## License

This repository is for educational purposes related to the live AI Engineering course.
