# Python Function Arguments In-Depth Guide

## 📌 Argument Types and Rules

### 1. Positional Arguments
Positional arguments are bound to parameter names based strictly on the **order** in which they are passed from left to right.
* **Rule:** You must provide exactly the number of arguments the function expects. Changing the order alters which parameter receives which value.

```python
def describe_pet(animal_type, name):
    print(f"I have a {animal_type} named {name}.")

# Position matters
describe_pet("dog", "Rex")  # I have a dog named Rex.
describe_pet("Rex", "dog")  # I have a Rex named dog.
```

---

### 2. Keyword Arguments
Keyword arguments are passed by explicitly naming the parameter and assigning it a value using the `=` symbol during the function call.
* **Rule:** Order no longer matters because Python maps values directly by name. However, **positional arguments must always come before keyword arguments** during a function call.

```python
def describe_pet(animal_type, name):
    print(f"I have a {animal_type} named {name}.")

# Order does not matter here
describe_pet(name="Rex", animal_type="dog") 

# INVALID: Positional argument follows keyword argument
# describe_pet(animal_type="dog", "Rex") 
```

---

### 3. Default Arguments
Default arguments allow you to assign a fallback value to a parameter in the function definition. If the caller omits that argument, Python uses the default.
* **Rule:** Parameters with default values **must be placed after** parameters without default values in the function definition.
* **Pitfall:** Never use mutable objects (like lists or dictionaries) as default values. Python evaluates defaults only once when the function is defined, meaning all subsequent calls share the exact same object instance.

```python
# Correct positioning
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")          # Hello, Alice! (Uses default)
greet("Bob", "Goodbye") # Goodbye, Bob! (Overrides default)

# BAD: Dangerous mutable default
def add_item(item, target_list=[]):
    target_list.append(item)
    return target_list

print(add_item("apple"))  # ['apple']
print(add_item("banana")) # ['apple', 'banana'] <-- Trapped data!

# GOOD: The safe way to use defaults for mutable objects
def safe_add_item(item, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list
```

---

### 4. *args (Arbitrary Positional Arguments)
The single asterisk `*` allows a function to accept an **unlimited number of positional arguments**.
* **Rule:** Python collects all extra positional arguments passed to the function and packs them into a single immutable **tuple** named `args`. 

```python
def calculate_sum(*args):
    print(type(args)) # <class 'tuple'>
    return sum(args)

print(calculate_sum(1, 2, 3, 4, 5)) # 15
print(calculate_sum())              # 0 (Works with zero arguments too)
```

---

### 5. **kwargs (Arbitrary Keyword Arguments)
The double asterisk `**` allows a function to accept an **unlimited number of keyword arguments**.
* **Rule:** Python collects all extra named arguments and packs them into a mutable **dictionary** named `kwargs`, where keys are parameter names and values are the argument data.

```python
def save_user_profile(username, **kwargs):
    print(type(kwargs)) # <class 'dict'>
    print(f"User: {username}")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

save_user_profile("johndoe", email="john@test.com", age=30, city="Chennai")
# Output:
# User: johndoe
# - email: john@test.com
# - age: 30
# - city: Chennai
```

---

### 6. Keyword-Only Arguments
Keyword-only arguments are parameters that **can only be passed by name**, never by position.
* **Rule:** You enforce this by putting a bare asterisk `*` as a standalone separator in the parameter list. Any parameter defined *after* the bare `*` (or after a `*args` collection) is strictly locked to keyword calls.
* **Purpose:** It protects your API. If you have configuration flags or boolean parameters, forcing names prevents callers from accidentally passing random values in the wrong order.

```python
# The * acts as a boundary wall
def process_data(data, *, standard_scale=False, clean_whitespace=True):
    print(f"Processing data with scale={standard_scale}")

# Correct Usage:
process_data("raw text", standard_scale=True)

# INVALID: Python blocks this because you didn't name the parameters
# process_data("raw text", True, False) 
# TypeError: process_data() takes 1 positional argument but 3 were given
```

---

## 🏆 The Ultimate Rule: Absolute Ordering

When mixing these types together inside a single function definition, Python enforces a strict sequence. If you violate this arrangement, your script will throw a syntax error.

The required definition sequence is:
1. **Positional** parameters
2. **Optional / Default** parameters
3. **`*args`** (or a single `*` marker)
4. **Keyword-only** parameters (with or without defaults)
5. **`**kwargs`**

```python
# The maximum valid signature structure
def master_function(pos1, pos2, default1="Val", *args, kw_only1, kw_only2="Default", **kwargs):
    pass
```
