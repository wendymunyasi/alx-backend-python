# Project Name
**0x01. Python - Async**

## Author's Details
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel: *+254707240068.*

##  Requirements

### Python Scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using gcc, using python3 (version 3.8.5).
*   All your files should end with a new line.
*   The `main.py` files are used to test your functions, but you don’t have to push them to your repo.
*   The first line of all your files should be exactly `#!/usr/bin/python3`.
*   Your code should use the pycodestyle (version `2.8.*`).
*   All your files must be executable.
*   The length of your files will be tested using `wc`.
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)`' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified).


## Project Description
Learn `async` and `await` syntax.
How to execute an async program with `asyncio`.
How to run concurrent coroutines.
How to create `asyncio` tasks.
How to use the `random` module.


* **0. Basic annotations - add** - Write a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float. - `0-basic_async_syntax.py`.
* **1. Let's execute multiple coroutines at the same time with async** - Import `wait_random` from the previous file and write an async routine called `wait_n` that takes in 2 int arguments (in this order): `n` and `max_delay`. You will spawn `wait_random` n times with the specified max_delay. - `1-concurrent_coroutines.py`.
* **2. Measure the runtime** - Import `wait_n ` from the previous file and create a `measure_time` function with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n`. - `2-measure_runtime.py`.
* **3. Tasks** - Import `wait_random` from `0-basic_async_syntax`. Write a function `task_wait_random` that takes an integer `max_delay` and returns a `asyncio.Task`. - `3-tasks.py`.
* **4. Tasks** - Take the code from `wait_n` and alter it into a new function `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called. - `4-tasks.py`.


## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
