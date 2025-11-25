# MathLib: A Simple Python Library for Basic Mathematical Operations

![alt text](image-4.png)

MathLib is a simple Python library for basic mathematical operations, including arithmetic and algebraic functions. It's designed to be easy to use and extendable for more advanced mathematical operations.

## Features

- **Arithmetic Operations**: Addition, subtraction, multiplication, and division.
- **Algebraic Operations**: Solving simple linear equations.

## Important steps

### Step 1: Set Up the Project Structure

First, set up your directory structure:

```
MathLib/
├── mathlib/
│   ├── __init__.py
│   ├── arithmetic.py
│   ├── algebra.py
│   ├── complex_numbers.py
│   ├── logarithmic.py
│   ├── matrix_operations.py
│   ├── power_roots.py
│   ├── random_utils.py
│   ├── statistics.py
│   ├── trigonometry.py
│   └── utility.py
├── tests/
│   ├── test_arithmetic.py
│   ├── test_algebra.py
│   ├── test_complex_numbers.py
│   ├── test_logarithmic.py
│   ├── test_matrix_operations.py
│   ├── test_power_roots.py
│   ├── test_random_utils.py
│   ├── test_statistics.py
│   ├── test_trigonometry.py
│   └── test_utility.py
├── setup.py
├── README.md
└── LICENSE
```
---------

## Installation
- **Step-1: Install the Package Locally**

    You can install MathLib directly from the source code:

    ```bash
    git clone https://github.com/arunp77/Data-engineering-tools.git
    ```
    Navigate to the root directory of your project (where setup.py is located) 
    ```bash
    cd /Data-engineering-tools/mathlib
    ```
    and then run:
    ```bash
    pip install -e . -v
    ```
    The `-e` flag stands for "editable," which means any changes you make to the code will immediately be reflected without needing to reinstall the package. Here `-v` will give you more detailed output about what is happening during the installation process.

    ![alt text](image.png)

    We can also install it using:

    ```bash
    pip install mathlib
    ```
    ![alt text](image-1.png)

- **Step 2: Verify Installation**
  
  After running the installation, you can verify that the package was installed by running:

    ```bash
    pip show mathlib
    ```
    This should display information about the mathlib package, such as the version and location.

    > **Verify Import in Python Shell:**
    > Try importing mathlib directly in the Python shell to ensure it is correctly recognized:
    > ```bash
    > >>> import mathlib
    >
    > >>> mathlib
    > ```
    > We can also install mathlib, directly using `setup.py` file, using:
    > ```bash
    > python setup.py install --verbose
    > ```
    > This will give you more detailed output about what is happening during the installation process.
    >
    > If you're using `pip install`, you can add the `-v` option for verbose output:


- **Step 3: Run the Tests**
  Once the package is installed, you should run the tests to ensure everything is working as expected.

  Navigate to the root directory of your project and run:
  ```bash
    pytest tests/
  ```
  This will execute the tests defined in `tests/test_arithmetic.py` and `tests/test_algebra.py`. If all the tests pass, it indicates that your package is functioning correctly.

- **Step 4: Create Docekrimage**
  ```bash
  docker build -t arunp77/mathlib:latest .
  ```

  and then push it to DOcker. 
  ```bash
  docker push arunp77/mathlib:latest
  ```

  Here, you must remember that, you must have created a Docker Access token from the DOcker hub and then saved it to your Github secrets. FOr more details on this, you can follow step by step guide provided at [my documentation page created for another project](https://github.com/arunp77/Job-Market-project/blob/main/Docker-image-integration.md)
  
  Image of the library is available at: [https://hub.docker.com/r/arunp77/mathlib](https://hub.docker.com/r/arunp77/mathlib)

# Package

This is also available as package on npm on following [link](https://www.npmjs.com/package/mathlib-npm-new) and on [pypi](https://pypi.org/project/arunp77-mathlib/) (for more details, please follow follow link: [https://docs.github.com/en/packages/quickstart](https://docs.github.com/en/packages/quickstart)).

![alt text](image-2.png)

![alt text](image-3.png)

## Contributing

Contributions are welcome! If you'd like to improve MathLib, please fork the repository and create a pull request with your changes. Make sure to update the tests as needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

