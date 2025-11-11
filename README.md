"""
# Python Fundamentals Cheatsheet – Complete Version

This cheatsheet covers all essential Python concepts:
- Variables & Data Types
- Functions, args, kwargs
- Decorators (function & class)
- Classes & Objects
- Context Managers
- Control Structures (if, elif, else)
- Error Handling (try, except, finally)
- Modules & Packages
- Special methods (__init__, __call__, __enter__, __exit__)
- Global & Nonlocal
- Real-world use cases

---

## 1️⃣ Variables & Data Types
- **Definition:** Containers for storing values
- **Types:** int, float, str, bool, list, tuple, set, dict
- **Use cases:** Store user info, balances, scores, configs
- **Example:** 
    balance = 5000          # int
    username = "Rajan"      # str
    scores = [10, 20, 30]   # list

---

## 2️⃣ Functions (`def`)
- **Definition:** Reusable blocks of code to perform a task
- **Parameters:** Inputs to function
- **Return:** Output from function
- **Use cases:** Calculations, API calls, reusable logic
- **Example:**
    def calculate_total(a, b):
        return a + b

---

## 3️⃣ *args & **kwargs
- **`*args`** → Accepts any number of positional arguments (tuple)
- **`**kwargs`** → Accepts any number of keyword arguments (dict)
- **Use cases:** Flexible function calls, decorators, API wrappers
- **Example:**
    def show_scores(*args, **kwargs):
        print(args)   # Positional
        print(kwargs) # Named

---

## 4️⃣ Decorators
- **Definition:** Functions or classes that modify/enhance other functions
- **Types:** Function decorator, decorator with arguments, class decorator
- **Use cases:** Logging, caching, authentication, metrics, formatting
- **Example:**
    def uppercase(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs).upper()
        return wrapper

---

## 5️⃣ Class Decorators
- **Definition:** Decorators implemented using a class
- **Key Methods:** 
    - __init__(self, func) → store function or parameters
    - __call__(self, *args, **kwargs) → executed instead of function
- **Use cases:** Count events, enhance function output, track state

---

## 6️⃣ Classes & Objects
- **Definition:** Blueprints (classes) to create instances (objects)
- **Key Concepts:** 
    - __init__ → constructor
    - self → reference to instance
    - Methods → functions inside class
- **Use cases:** Model users, wallets, products, games

---

## 7️⃣ Context Managers (`with`)
- **Definition:** Manage resources safely (files, DB, APIs)
- **Key Methods:** __enter__ (setup), __exit__ (cleanup)
- **Use cases:** File handling, database sessions, network connections

---

## 8️⃣ Control Structures
- **if-elif-else** → Conditional logic
- **Use cases:** Decision making in code, branching logic
- **Example:**
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    else:
        grade = "C"

---

## 9️⃣ Error Handling
- **Keywords:** try, except, finally, raise
- **Use cases:** Prevent crashes, input validation, API errors
- **Example:**
    try:
        x = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("Always runs")
- **raise:** Manually throw an exception
    if balance < 0:
        raise ValueError("Balance cannot be negative")

---

## 🔟 Special Methods & Attributes
- **Common Methods:** 
    - __init__ → constructor
    - __str__ → string representation
    - __call__ → make object callable
    - __enter__, __exit__ → context manager
- **Use cases:** Customize OOP behavior, class decorators, resource management

---

## 1️⃣1️⃣ Global vs Nonlocal
- **global:** Modify variable at module level
- **nonlocal:** Modify variable in enclosing function
- **Use cases:** Counters, state tracking, decorators

---

## 1️⃣2️⃣ Modules & Packages
- **Definition:** Reusable code libraries
- **Common Modules:** math, random, datetime, os, sys
- **Use cases:** Calculations, date/time, randomness, system tasks

---
## 1️⃣3️⃣ Iterators & Generators 
- **Iterator:**  
  - Implements `__iter__()` and `__next__()`  
  - Used to iterate manually or in loops  
  - **Use:** Custom sequence classes, streaming data  

- **Generator:**  
  - Created using `yield` in functions  
  - Produces values lazily (one at a time)  
  - **Use:** Efficient data streaming, infinite sequences  

- **Cheatsheet Summary:**  
  | Concept | Keyword/Method | Purpose |
  |----------|----------------|----------|
  | Iterator | `__iter__()`, `__next__()` | Custom looping logic |
  | Generator | `yield` | Lazy iteration, memory-efficient |
  | StopIteration | Raised when iteration completes | End of iteration |

---

## 1️⃣4️⃣ Looping Techniques 
- **for loop:** Iterate over iterable objects  
- **while loop:** Run until condition is false  
- **Loop Controls:**  
  - `break` → Exit loop  
  - `continue` → Skip current iteration  
  - `pass` → Do nothing (placeholder)  
  - `else` → Runs if no break occurs  
- **Examples:**  
    ```
    for i in range(1, 6):
        if i == 3:
            continue
        print(i)
    ```
- **Use cases:** Counters, searches, condition-based iteration  

---

## 1️⃣5️⃣ Python Data Structures
- **List:** Ordered, mutable  
    ```
    fruits = ["apple", "banana", "cherry"]
    ```
- **Tuple:** Ordered, immutable  
    ``
    cords = (10, 20)
    ```
- **Set:** Unordered, unique items  
    ```
    id = {1, 2, 3}
    ```
- **Dict:** Key-value pairs  
    ```
    user = {"name": "Rajan", "age": 25}
    ```
- **Use cases:**  
  - **List:** Store and manipulate collections  
  - **Tuple:** Store constant or fixed data  
  - **Set:** Remove duplicates, perform set operations  
  - **Dict:** Store relationships (key-value pairs)  

---

## 1️⃣6️⃣ Practical Business Use Cases
- **Variables:** Store user data, balances, configurations  
- **Functions:** Reusable logic, API calls, calculations  
- **Decorators:** Logging, authentication, caching, metrics  
- **Class Decorators:** Track events, enhance outputs, manage state  
- **Classes & Objects:** Model users, wallets, products, etc.  
- **Context Managers:** File handling, DB connections, API sessions  
- **Control Structures:** Conditions for logic branching  
- **Error Handling:** Manage invalid input or failed operations  
- **Args/Kwargs:** Dynamic APIs and flexible function calls  
- **Modules:** Utility imports like math, datetime, os  
- **Iterators/Generators:** Memory-efficient data handling  
- **Looping:** Iteration for searches, counting, data processing  
- **Data Structures:** Organize and manage collections efficiently

---

## 📌 Key Takeaways
1. Python is flexible and dynamic — variables and types can change.  
2. Functions & decorators allow code reuse and enhancement.  
3. Classes provide structured design for real-world entities.  
4. Context managers and error handling help manage resources safely.  
5. *args, **kwargs, global, and nonlocal give flexibility and state control.  
6. Master these fundamentals to build scalable, maintainable, professional Python projects.
"""
