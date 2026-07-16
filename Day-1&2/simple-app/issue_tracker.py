import json
from typing import TypedDict, Optional, Callable

# --- BLOCK B (Day 2): Type Hint Contracts ---
class IssueDict(TypedDict):
    id: int
    title: str
    status: str  # "Open" or "Resolved"

# --- BLOCK C (Day 2): First-Class Functions & Decorators ---
def log_action(func: Callable) -> Callable:
    """Decorator to intercept execution and log system actions."""
    def wrapper(*args, **kwargs):
        # Day 1: f-strings for concise formatting
        print(f" LOG: Executing {func.__name__}...")
        result = func(*args, **kwargs)
        print(f" LOG: Completed {func.__name__}.")
        return result
    return wrapper

class LocalIssueManager:
    # Day 2: Defusing the mutable default argument trap by initializing via None
    def __init__(self, storage_path: str = "issues.json", initial_issues: Optional[list[IssueDict]] = None) -> None:
        self.storage_path = storage_path
        self.issues: list[IssueDict] = initial_issues if initial_issues is not None else []
        
    # --- BLOCK B (Day 1): Context Managers (EAFP Approach) ---
    def save_to_disk(self) -> None:
        """Side Effect Edge Layer: Persists data safely using a context manager."""
        try:
            with open(self.storage_path, "w") as file:
                json.dump(self.issues, file, indent=4)
        except IOError as e:
            print(f"Failed to write storage file: {e}")

    # --- BLOCK A (Day 2): Pure Function Core ---
    def compute_next_id(self) -> int:
        """Pure Function: Calculates next sequential ID without modifying state."""
        if not self.issues:
            return 1
        # Day 1: List comprehension instead of manual for-loops
        return max([issue["id"] for issue in self.issues]) + 1

    # --- BLOCK A & C (Day 2): One Function, One Job & Early Return ---
    @log_action
    def create_issue(self, title: str) -> IssueDict:
        """Validates input, creates a tracking dictionary, and handles storage entry."""
        # Day 2: Return early guard clause
        if not title or title.strip() == "":
            raise ValueError("Issue title cannot be empty.")

        new_issue: IssueDict = {
            "id": self.compute_next_id(),
            "title": title.strip(),
            "status": "Open"
        }
        
        # Day 1: Modifying a mutable list object reference in-place
        self.issues.append(new_issue)
        self.save_to_disk()  # Side effect pushed to execution boundary
        return new_issue

    @log_action
    def resolve_issue(self, issue_id: int) -> bool:
        """Locates an active issue by ID matching criteria and updates its tracking state."""
        # Day 1: Using truthiness and tuple unpacking via enumerate
        for index, issue in enumerate(self.issues):
            # Day 1: Identity checking vs Value comparison (issue_id == issue["id"])
            if issue["id"] == issue_id:
                if issue["status"] == "Resolved":
                    return False # Guard clause: Already processed
                
                self.issues[index]["status"] = "Resolved"
                self.save_to_disk()
                return True
        return False

# --- VERIFYING EXECUTION ---
if __name__ == "__main__":
    # Day 1 Setup: Clean local instantiation
    manager = LocalIssueManager()
    
    # 1. Add issues
    issue1 = manager.create_issue("Fix memory leak in background worker")
    issue2 = manager.create_issue("Refactor deeply nested API controller loop")
    
    print(f"\nCreated Issues: {manager.issues}\n")
    
    # 2. Resolve an issue
    success = manager.resolve_issue(issue1["id"])
    print(f"Resolution Status: {success} | Updated State: {manager.issues}")