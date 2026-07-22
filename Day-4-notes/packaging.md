# Python Packaging and Distribution Guide

## 1. Why a Configuration File is Necessary
A plain Python script can be run locally, but it cannot be neatly distributed or managed by package installers like `pip`. A formal configuration file provides vital metadata and instructions required by the Python ecosystem:
* **Identity:** Defines the official distribution name and version number for tracking and updates.
* **Dependency Management:** Lists external libraries required by your package. When a user runs `pip install`, `pip` reads this list and automatically installs the requirements first.
* **Code Discovery:** Explicitly tells the build backend which directories contain production source code, preventing local tests or scratchpads from being packaged.
* **CLI Entry Points:** Configures terminal command shortcuts, allowing users to execute functions in your package directly from the system command prompt.

---

## 2. Comparison: pyproject.toml vs. setup.py

| Feature | Modern Standard: pyproject.toml | Legacy Method: setup.py |
| :--- | :--- | :--- |
| **File Nature** | Static text configuration data (TOML format) | Dynamic executable Python script |
| **Security** | Safe; read by parsers without executing code | Riskier; arbitrary code executes during metadata inspection |
| **Build System** | Pluggable; supports modern backends (Hatch, Flit, Poetry) | Rigid; strictly locked into Setuptools |
| **Readability** | High; standardized, declarative structures | Variable; programmatic dictionaries and function calls |

### Structural Vulnerabilities of setup.py
1. **The Execution Hazard:** Because `setup.py` is executable code, `pip` had to run the script just to discover basic details like the package name. Malicious actors could inject harmful code directly into a `setup.py` file that would trigger automatically upon inspection. `pyproject.toml` contains only declarative data, rendering code execution impossible.
2. **The Build System Monopolization:** Python historically forced the entire ecosystem to rely on a single package compiler called `setuptools`. The `pyproject.toml` file introduces a standardized `[build-system]` table, allowing developers to switch to faster, more modern compilers easily.
3. **The Bootstrap Chicken-and-Egg Bug:** If a legacy `setup.py` script required a specific third-party library to determine its own version number, it would crash. Python could not install that prerequisite library because it had not parsed the `setup.py` file yet. `pyproject.toml` solves this by handling build-time requirements in an isolated pre-installation step.

---

## 3. Comprehensive pyproject.toml Template

Below is a complete, modern structure using `hatchling` as the build engine.

```toml
[build-system]
# Specifies the exact backend tool needed to compile the package
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
# Core Package Metadata
name = "mycalc"
version = "1.0.0"
description = "A simple and efficient calculator package"
readme = "README.md"
requires-python = ">=3.8"
authors = [
    { name = "Your Name", email = "you@example.com" }
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

# Third-party runtime dependencies
dependencies = [
    "numpy>=1.20.0",
]

[project.scripts]
# Creates an executable terminal command mapping to a specific function
# Syntax: command_name = "package.module:function"
mycalc-cli = "mycalc.entry:main"
```

### Ideal Project Layout
```text
mycalc_project/
├── pyproject.toml
├── README.md
└── src/
    └── mycalc/
        ├── __init__.py
        ├── calculator.py
        └── entry.py
```

---

## 4. Compilation and Distribution Commands

### Building the Package Locally
To compile the text configuration into optimized distribution binaries, execute the following commands from the project root folder (where `pyproject.toml` lives):

```bash
# 1. Install the standardized building tool
pip install build

# 2. Run the compiler module
python -m build
```

This creates a `dist/` directory containing two distinct build variants:
1. **Source Distribution (`.tar.gz`):** A compressed archive containing the raw source code and metadata files.
2. **Built Distribution (`.whl` / Wheel):** A highly optimized binary distribution format ready for direct, fast installation.

### Installing and Transferring the Wheel
To run or test your built package on an isolated or separate target computer, copy the `.whl` file to that system and point `pip` directly to it:

```bash
# Install the local wheel file directly
pip install calc_pkg-1.0.0-py3-none-any.whl
```

### Remote and Public Alternatives
* **Git Version Control:** If the code is pushed to a remote platform, users can install it cleanly via terminal by targeting the repository URI:
  ```bash
  pip install git+https://github.com
  ```
* **Python Package Index (PyPI):** To publish your creation so anyone globally can download it using standard shorthand syntax, deploy the artifact using `twine`:
  ```bash
  pip install twine
  twine upload dist/*
  ```
  Once published, any system can immediately consume the project globally:
  ```bash
  pip install mycalc
  ```
