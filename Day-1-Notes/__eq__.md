# 📝 Python Equality (`==`) Cheat Sheet & Notes

## 📌 Core Rule
*   `==` evaluates **Value/Content Equality** (via the `__eq__` method).
*   `is` evaluates **Reference/Memory Identity**.

---

## ⚡ Summary Table

| Category | Type / Scenario | What `==` Checks First | What `==` Checks Next |
| :--- | :--- | :--- | :--- |
| **Plain Objects** | Custom classes without custom code | **Reference** (`is`) | *Nothing* (Returns `False` if reference fails) |
| **Dataclasses** | Classes using `@dataclass` | **Object Type** | **Values** (Field-by-field check) |
| **Containers** | Lists, Tuples, Dicts, Sets | **Reference** (Short-circuit optimization) | **Values** (Deep item-by-item loop) |
| **Basic Types** | `int`, `str`, `bool`, `float` | **Values Alone** | *Nothing* |

---

## 🔍 Detailed Behavior

### 1. Plain Custom Objects (Reference Only)
Standard user-defined classes fallback directly to the base `object` behavior.
```python
class User:
    def __init__(self, name): 
        self.name = name

u1 = User("Alice")
u2 = User("Alice")

print(u1 == u2)  # False ❌ (Different memory addresses)
```

### 2. Dataclasses (Value Only)
The `@dataclass` decorator auto-generates an `__eq__` method that compares data fields directly.
```python
from dataclasses import dataclass

@dataclass
class User:
    name: str

u1 = User("Alice")
u2 = User("Alice")

print(u1 == u2)  # True  (Field values match)
```

### 3. Complicated Containers (Reference ➔ Value)
Python uses a quick **short-circuit optimization** for collections to save CPU cycles.
*   **Step 1:** Checks `is` reference. If identical, instantly returns `True`.
*   **Step 2:** If references differ, loops through the structure to verify values.
```python
list_a = [1] * 1000
list_b = list_a  # Shared reference

print(list_a == list_b)  # True ⚡ (Instant; skips checking 1000 items)
```

### 4. Basic Types (Value Only)
Primitives bypass memory location entirely to evaluate a logical data match.
```python
print(5 == 5.0)       # True (Math value matches)
print("abc" == "abc") # True (Character sequences match)
```
