# Python Type Annotations and Typing Toolkit Guide

## 1. Core Principles of Type Annotations
Type annotations (introduced in PEP 484) allow developers to explicitly declare the expected data types for variables, function parameters, and return values.

* **The Runtime Reality:** Python remains a **dynamically typed language** at runtime. The Python interpreter completely ignores type annotations during execution. They do not enforce types, cast data, or throw runtime errors.
* **The Purpose:** Annotations exist for static analysis. They are utilized by tools like **Mypy**, IDE type-checkers (like VS Code's Pyright), and data-validation libraries (like **Pydantic**) to catch bugs before code runs.

```python
# Variable annotation
age: int = 25

# Function parameter and return type annotation
def greet(name: str) -> str:
    return f"Hello, {name}"
```

---

## 2. In-Depth Component Breakdown

### A. Generic Collections (`list[...]` and `dict[...]`)
These are used to annotate data containers and specify the exact internal data types they hold.
* **Python 3.9+ Standard:** You can use the built-in `list` and `dict` types directly for annotation.
* **Legacy Method (Python 3.8 and below):** Requires importing uppercase variants from the typing module: `from typing import List, Dict`.

```python
# A list containing only integers
scores: list[int] = [88, 92, 79]

# A dictionary with string keys and float values
prices: dict[str, float] = {"apple": 1.50, "orange": 2.25}

# Complex nested container: A list containing dictionaries
user_matrix: list[dict[str, int]] = [{"id": 1, "age": 30}]
```

### B. `Optional`
`Optional[X]` indicates that a value can either be of type `X` **or it can be `None`**. It is typically used for optional configuration flags or parameters that default to `None`.
* **Python 3.10+ Standard:** Use the pipe operator `X | None` instead of importing `Optional`.

```python
from typing import Optional

# Using explicit Optional (Compatible with all versions)
def get_user_id(username: str) -> Optional[int]:
    if username == "admin":
        return 1
    return None

# Modern alternative (Python 3.10+) - No import required
def get_user_id_modern(username: str) -> int | None:
    return 1 if username == "admin" else None
```

### C. `Union`
`Union[X, Y]` explicitly states that a parameter or variable can accept **multiple distinct types** (either type `X` OR type `Y`).
* **Python 3.10+ Standard:** Use the pipe operator `X | Y` instead of importing `Union`.

```python
from typing import Union

# Can accept either a raw integer or a float
def process_payment(amount: Union[int, float]):
    pass

# Modern alternative (Python 3.10+) - No import required
def process_payment_modern(amount: int | float):
    pass
```

### D. `Callable`
`Callable` is used when passing a function object as an argument into another function (Higher-Order Functions).
* **Syntax:** `Callable[[ParamType1, ParamType2], ReturnType]`
* **Rules:**
  * Use an empty list `[]` if the function takes no arguments.
  * Use `...` (ellipsis) if you want to restrict the return type but allow any number or type of parameters: `Callable[..., ReturnType]`.

```python
from typing import Callable

# Expects a function that takes two ints and returns an int
def compute(x: int, y: int, algo: Callable[[int, int], int]) -> int:
    return algo(x, y)

def add(a: int, b: int) -> int:
    return a + b

# Valid execution
result = compute(5, 10, add)
```

---

## 3. Comprehensive Production Example

This example combines variables, collections, optional dependencies, multiple types, and functional object parameters into a single production signature.

```python
from typing import Callable, Optional, Union

def process_data_pipeline(
    raw_data: list[Union[int, str]], 
    logger: Optional[Callable[[str], None]] = None
) -> dict[str, int]:
    
    clean_count = 0
    for item in raw_data:
        if isinstance(item, int):
            clean_count += 1
            
    if logger is not None:
        logger(f"Processed {clean_count} valid integers.")
        
    return {"total_integers": clean_count}
```

Modern Python 3.10+ alternative for the identical signature:

```python
def process_data_pipeline_modern(
    raw_data: list[int | str], 
    logger: Callable[[str], None] | None = None
) -> dict[str, int]:
    # Logic remains identical
    pass
```
