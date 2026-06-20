# Python Practice

A beginner-friendly collection of small exercises and examples to learn and reinforce core Python concepts. The repository is organized by topic (folders named with a leading number for ordering) so you can work through subjects sequentially.

## Repository Structure

- `01_basics/` — Basic syntax, printing, and simple expressions
- `02_virtual/` — Virtual environment and project setup examples
- `03_data_types/` — Strings, numbers, lists, tuples, sets, and dicts
- `04_conditionals/` — If/else, boolean logic, and branching
- `05_loops/` — `for` / `while` loops and iteration exercises
- `06_functions/` — Defining and using functions, scope, and arguments
- `07_comprehensions/` — List/dict/set comprehensions
- `08_generators_decorators/` — Generators, iterators, and decorators
- `09_OOPS/` — Classes, objects, inheritance, and OOP patterns
- `10_Files_Exception_Handling/` — File I/O and exception handling
- `11_threads_concurrency/` — Threading and multiprocessing examples
- `12_async_python/` — Async/await and concurrency patterns
- `13_pydantic/` — (Optional) pydantic examples and models

Each folder contains chapter files (`chapter_X.py`) and practice scripts (`practice_X.py`).

## Prerequisites

- Python 3.8+ recommended
- (Optional) Create and activate a virtual environment when experimenting:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

## Running Examples

Run any script directly with Python from the repository root. Examples:

```bash
python3 01_basics/chapter_1.py
python3 05_loops/practice_3.py
```

Prefer running small scripts one at a time while editing them in your editor.

## Adding New Practice Content

- Add a new numbered folder for the topic (keep the leading number for ordering).
- Include at least one `chapter_X.py` with examples and one `practice_X.py` with exercises.
- Use clear, descriptive file names and add short comments explaining the goal of each script.

## Contributing

This repository is primarily for personal learning, but contributions are welcome:

- Open an issue or submit a pull request with suggested examples or fixes.
- Keep changes small and focused; add tests or example outputs when helpful.

## License & Use

Use these exercises freely for learning and teaching. If you redistribute substantial portions, please credit the original source.

---

If you'd like, I can also:

- add a small `requirements.txt` or `pyproject.toml` for dependency management
- add a CONTRIBUTING.md with contribution guidelines
- run a quick pass to standardize docstrings and comments across chapters

Tell me which of these you'd like next.
