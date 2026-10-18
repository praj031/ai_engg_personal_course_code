# AI Engineering - Live Course Repository

This repository tracks the complete journey of the **AI Engineering live course**. Each week contains the concepts, code, exercises, and homework covered in class, organized for future revision and project growth.

The repository is built as a modern Python project using **uv** for dependency management, **Git** for version control, and **Jupyter Notebooks** + **Python scripts** for hands-on learning.

> **Status:** Week 1 is complete. Week 2 will be added as the course progresses.

---

## 📚 Course Roadmap

| Week | Focus Area | Status |
|------|-----------|--------|
| **Week 1** | Python Foundations for AI Engineering | ✅ Complete |
| **Week 2** | *(To be updated based on upcoming classes)* | 🔄 Upcoming |

---

## 🗓️ Week 1: Python Foundations for AI Engineering

### Overview

Week 1 establishes the Python skills required for modern AI Engineering work. Topics progress from basic language features to object-oriented programming, asynchronous I/O, API calls, and finally data validation with Pydantic — all of which are essential when building AI applications that call LLMs, fetch data concurrently, and validate structured inputs/outputs.

### Topics Covered

#### 1. Project Setup & Tooling (`uv`, Git, VS Code)

- Initializing a Python project with `uv init`
- Understanding `pyproject.toml` as the project manifest (similar to Maven's `pom.xml`)
- Dependency management with `uv add` and reproducible installs via `uv.lock`
- Virtual environment handling
- Git workflow: init, remote, pull, add, commit, push using a Personal Access Token (PAT)
- Difference between `.py` production scripts and `.ipynb` learning notebooks

#### 2. Python Fundamentals

- Variables, dynamic typing, and mutability vs. rebinding
- Basic types: `str`, `int`, `float`, `bool`, `NoneType`
- The `is None` vs `not value` distinction for missing-value checks
- String formatting with f-strings, `.strip()`, `.upper()`, `.split()`, `.join()`
- Control flow: `if/elif/else`, `for`, `while`, `continue`, `break`
- Core collections: `list`, `dict`, `tuple`, `set`
- Functions, type hints, and the mutable default argument trap
- Exception handling with `try/except/else/finally` and custom exceptions
- Modules and imports
- List comprehensions

#### 3. Object-Oriented Programming

- Classes, `__init__`, `self`, and instance attributes
- `@classmethod` as an alternative constructor
- `@staticmethod` for utility functions inside a class namespace
- `@property` for computed attributes
- Inheritance and `super()`
- Method overriding
- Composition (critical for AI agent design)
- Duck typing
- Dataclasses for reducing boilerplate
- Variadic arguments `*args` and `**kwargs` for flexible function signatures

#### 4. Asynchronous I/O

- Why async matters for AI Engineering (API calls, LLM requests, database queries)
- `async def` coroutines and `await`
- Sequential vs. concurrent execution with `asyncio.gather()`
- The event loop and `asyncio.run()` for `.py` scripts
- Top-level `await` in Jupyter notebooks
- Async generators and `async for`
- Real HTTP requests using `httpx.AsyncClient`
- Concurrent API calls to JSONPlaceholder
- Combining user profile, posts, and todos into a single dictionary before sending to an LLM

#### 5. Pydantic: Data Validation & Serialization

- `BaseModel` and runtime type enforcement
- Required vs. optional fields
- Nested models
- `Field()` constraints: `min_length`, `max_length`, `ge`, `le`, `gt`, `lt`, `alias`
- Modern `Annotated` syntax
- `@field_validator` for single-field rules
- `@model_validator` for cross-field rules
- Specialized types: `EmailStr`, `SecretStr`
- `ConfigDict(extra="forbid")`
- Serialization pipeline: `model_validate()`, `model_dump()`, `model_dump_json()`

### Week 1 Files

| File | Description |
|------|-------------|
| `src/ai_engg_live/1_fundamentals.ipynb` | Python basics: types, strings, control flow, collections, functions, exceptions, modules, comprehensions |
| `src/ai_engg_live/1_homework[26-10-2026].ipynb` | Week 1 fundamentals homework: casting, string formatting, retry loops, collections, safe logging |
| `src/ai_engg_live/2_oops_in_python.ipynb` | OOP concepts: classes, inheritance, composition, dataclasses, `*args`/`**kwargs` |
| `src/ai_engg_live/3_learn_async_io.ipynb` | Async I/O: coroutines, `asyncio.gather`, event loop, `httpx.AsyncClient`, concurrent API calls |
| `src/ai_engg_live/4.1_Api_call.py` | Standalone async script: fetch a single post with `httpx` |
| `src/ai_engg_live/4.2_API_call.py` | Standalone async script: fetch user, post, and todo concurrently |
| `src/ai_engg_live/5_learn_Pyndatic.ipynb` | Pydantic models, validation, constraints, nested models, serialization, and homework solutions |
| `src/ai_engg_live/homework[26-10-2026].ipynb` | Additional homework notebook |
| `src/ai_engg_live/__init__.py` | Package entry point with a simple `main()` function |

### Week 1 Key Takeaways

1. **Modern Python project setup** uses `uv` for fast dependency management and `pyproject.toml` for configuration.
2. **Type hints are documentation**, not runtime enforcement; use **Pydantic** when you need real validation.
3. **Async I/O** lets AI applications fetch multiple data sources concurrently instead of waiting sequentially.
4. **Pydantic** is the bridge between raw JSON (from APIs or LLMs) and reliable Python objects.
5. **OOP patterns** like composition and duck typing are heavily used when designing AI agents and tool systems.

---

## 🗓️ Week 2: Coming Soon

> This section will be updated after the Week 2 classes are delivered.
> Topics may include: working with LLM APIs, prompt engineering basics, embeddings, vector databases, or building simple AI agents.

---

## 🏗️ Project Structure

```text
ai_engg_live/
├── .gitignore                  # Files and folders ignored by Git
├── .python-version             # Python version used by uv/pyenv
├── pyproject.toml              # Project metadata, dependencies, build settings
├── uv.lock                     # Exact dependency versions for reproducibility
├── README.md                   # This file
└── src/
    └── ai_engg_live/
        ├── __init__.py         # Package entry point
        ├── 1_fundamentals.ipynb
        ├── 1_homework[26-10-2026].ipynb
        ├── 2_oops_in_python.ipynb
        ├── 3_learn_async_io.ipynb
        ├── 4.1_Api_call.py
        ├── 4.2_API_call.py
        ├── 5_learn_Pyndatic.ipynb
        └── homework[26-10-2026].ipynb
```

### File Descriptions

- **`README.md`**: Week-wise course overview and project documentation.
- **`.gitignore`**: Prevents temporary, environment-specific, or IDE files from being committed.
- **`pyproject.toml`**: Project configuration, dependencies, and build backend (equivalent to Maven's `pom.xml`).
- **`.python-version`**: Stores the Python version so `uv` or `pyenv` can use it automatically.
- **`uv.lock`**: Lock file that pins exact dependency versions for reproducible installs.
- **`src/ai_engg_live/__init__.py`**: The package's main module and entry point.
- **`.ipynb` notebooks**: Interactive learning, experimentation, and homework.
- **`.py` scripts**: Clean, reusable, production-style code examples.

---

## 🛠️ Common Commands

### uv Commands

```bash
uv init                                                      # Create a new Python project
uv add <package-name>                                        # Add a dependency
uv remove <package-name>                                     # Remove a dependency
uv lock                                                      # Update the lock file
uv sync                                                      # Install dependencies exactly as in uv.lock
uv run python src/ai_engg_live/__init__.py                   # Run a script inside the project environment
uv run python src/ai_engg_live/4.2_API_call.py             # Run an async API script
```

### Git Commands

```bash
git init -b main                                             # Initialize a Git repo on the main branch
git remote add origin <repo-url>                             # Connect to a GitHub repository
git pull origin main --rebase                                # Pull remote changes and rebase local commits
git add .                                                    # Stage all changes
git commit -m "Your commit message"                          # Commit staged changes
git push origin main                                         # Push commits to GitHub
```

---

## 🚀 How to Use This Repository

1. Clone the repository:
   ```bash
   git clone https://github.com/praj031/ai_engg_personal_course_code.git
   cd ai_engg_personal_course_code
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

3. Run the package entry point:
   ```bash
   uv run python src/ai_engg_live/__init__.py
   ```

4. Open the notebooks in VS Code or JupyterLab and run the cells week by week.

---

## 📌 Notes

- The project uses **Python 3.13+** as specified in `pyproject.toml`.
- Notebooks use **top-level `await`**, which is supported because Jupyter already runs an event loop.
- Standalone `.py` async scripts use `asyncio.run(main())` as the entry point.
- `SecretStr` values are hidden by default during serialization to avoid leaking API keys in logs.

---

## 👤 Author

- **Pritish Raj** - [pritishraj.official@gmail.com](mailto:pritishraj.official@gmail.com)

---

## 📜 License

This repository is for educational purposes related to the live AI Engineering course.
