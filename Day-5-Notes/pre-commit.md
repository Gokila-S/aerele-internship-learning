# 🛠️ Pre-Commit Hooks Notes

Pre-commit hooks are automated scripts that run safety checks (formatting, syntax validation, linting) **before you commit code to Git**. If a check fails, it blocks the commit, preventing broken or poorly formatted code from entering the repository.

---

## 🚀 Step-by-Step Setup

### 1. Install the Package
Ensure your virtual environment (`.venv`) is active, then run:
```powershell
pip install pre-commit
```

Verify the installation:
```powershell
pre-commit --version
```

### 2. Create the Configuration Blueprint
Create a file named `.pre-commit-config.yaml` in your root project directory and add this production-ready configuration:

```yaml
repos:
  - repo: https://github.com
    rev: v4.6.0  # Hook ecosystem version
    hooks:
      - id: trailing-whitespace   # Automatically trims trailing empty spaces
      - id: end-of-file-fixer     # Ensures files end with a clean new line
      - id: check-yaml            # Validates YAML syntax correctness

  - repo: https://github.com
    rev: 24.4.2
    hooks:
      - id: black                 # Automated professional Python formatter
```

### 3. Register with Git
Initialize your repository (if not already done) and link the framework configuration to Git's lifecycle hooks:
```powershell
git init
pre-commit install
```

---

## 💻 Core Execution Commands

### Run Hooks on Specific Files
To isolate checks to targeted files without analyzing the whole project, pass the file paths using the `--files` flag:
```powershell
pre-commit run --files path/to/file.py path/to/another.py
```

### Run a Specific Hook ID on Specific Files
To test only **one** tool (e.g., just `black`) against specific files, include the hook's structural ID:
```powershell
pre-commit run black --files path/to/file.py
```

### Run on Staged Files (Default Manual Trigger)
To manually test only files currently added via `git add`:
```powershell
pre-commit run
```

### Force Run on All Files
Highly recommended when setting up pre-commit on an existing project for the first time:
```powershell
pre-commit run --all-files
```

### Emergency Bypass Shortcut
If an emergency requires you to commit code while skipping the pre-commit pipeline completely, append the `--no-verify` flag to your standard Git commit command:
```powershell
git commit -m "Emergency fix" --no-verify
```

---

## 🧠 Mentor Interview Script

> *"We leverage the `pre-commit` framework to automate strict static code analysis and quality control immediately before files enter local repository history. By mounting linters and code formatters like `black` directly onto Git's native lifecycle hooks via `.pre-commit-config.yaml`, we establish a standardized quality gate across the team. This process completely mitigates human errors—such as dangling trailing spaces, invalid YAML schemas, or broken formats—long before the code ever gets pushed to production environments or shared staging servers."*
