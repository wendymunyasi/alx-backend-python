# Project Name
**0x03. Unittests and Integration Tests**

## Author's Details
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel: *+254707240068.*

##  Requirements

### Python Scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using gcc, using python3 (version 3.8.5).
*   All your files should end with a new line.
*   The first line of all your files should be exactly `#!/usr/bin/env python3`.
*   Your code should use the pycodestyle (version `2.8.*`).
*   All your files must be executable.
*   The length of your files will be tested using `wc`.
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)`' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified).


## Project Description
Learn the difference between unit and integration tests.
Common testing patterns such as mocking, parametrizations and fixtures.

* **0. Parameterize a unit test** - Implement the `TestAccessNestedMap.test_access_nested_map` method to test that the method returns what it is supposed to. - `test_utils.py`.
* **1. Parameterize a unit test** - Implement `TestAccessNestedMap.test_access_nested_map_exception`. Use the `assertRaises` context manager to test that a `KeyError` is raised for the given inputs (use `@parameterized.expand`). - `test_utils.py`.
* **2. Mock HTTP calls** - Define the `TestGetJson(unittest.TestCase)` class and implement the `TestGetJson.test_get_json` method to test that `utils.get_json` returns the expected result. - `test_utils.py`.
* **4. Parameterize and patch as decorators** - Declare the `TestGithubOrgClient(unittest.TestCase)` class and implement the `test_org` method. - `test_client.py`.
* **5. Mocking a property** - Implement the `test_public_repos_url` method to unit-test `GithubOrgClient._public_repos_url`. - `test_client.py`.
* **6. More patching** - Implement `TestGithubOrgClient.test_public_repos` to unit-test `GithubOrgClient.public_repos`. - `test_client.py`.
* **7. Parameterize** - Implement `TestGithubOrgClient.test_has_license` to unit-test `GithubOrgClient.has_license`. - `test_client.py`.
* **8. Integration test: fixtures** - Create the `TestIntegrationGithubOrgClient(unittest.TestCase)` class and implement the `setUpClass` and `tearDownClass` which are part of the `unittest.TestCase` API. - `test_client.py`.
* **9. Integration tests** - Implement `test_public_repos` to  test `GithubOrgClient.public_repos`. - `test_client.py`.


## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
