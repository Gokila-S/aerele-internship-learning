
---

### 1. Frappe

* **What it is:** A rapid-development, Python/JS-based full-stack web framework designed specifically for data-driven business apps (like ERPNext).
* **The Stack:** `Python/JS` $\rightarrow$ `Frappe Framework` $\rightarrow$ `ERPNext / Custom Apps` $\rightarrow$ `MariaDB / Postgres`.

---

### 2. DocType (The Blueprint)

* **What it is:** The **schema definition** (metadata) of a business entity.
* **Database link:** Creating a DocType automatically creates a corresponding database table (prefixed with `tab`, e.g., `tabStudent`).
* **Analogy:** It is the **Class** in Object-Oriented Programming (OOP).

---

### 3. Document (The Instance)

* **What it is:** A single, unique **data record** (a row in the database table) populated using a DocType blueprint.
* **Analogy:** It is the **Object/Instance** of a Class in OOP.
* **Key Ratio:** *One DocType $\rightarrow$ Millions of Documents.*

---

### 4. Document Class

* **What it is:** The core Python base class (`from frappe.model.document import Document`) that acts as an ORM.
* **Why it matters:** Your custom controller inherits from this class, instantly granting your DocType access to built-in CRUD operations:
* `.insert()` (Create)
* `.save()` (Update)
* `.delete()` (Delete)
* `.submit()` (Freeze/Commit)



---

### 5. Controller

* **What it is:** The Python file (`[doctype_name].py`) matching your DocType.
* **Role:** Houses the backend server-side business logic, access controls, and data manipulation rules.

---

### 6. Lifecycle Hooks

* **What they are:** Event-driven methods triggered automatically by the framework at specific stages of a document’s life.
* **The Pipeline:**
1. **`validate()`**: Runs checks and constraints (e.g., age verification).
2. **`before_save()`**: Automatically manipulates data before database commit (e.g., concatenating `first_name` + `last_name`).
3. **`on_submit()`**: Executes unalterable actions post-submission (e.g., creating ledger entries).



---

### 7. The File Trio (Inside a DocType Folder)

Each DocType is defined by exactly three core files:

| File Extension | Name | Role | Runs On |
| --- | --- | --- | --- |
| **`.json`** | Metadata | Defines fields, permissions, layouts, and properties. | Database/Build |
| **`.py`** | Controller | Python class containing validation and server-side hooks. | Server |
| **`.js`** | Client Script | Client-side scripting for UI logic, button triggers, and field changes. | Browser |