# Table of Contents

- [Project Description](#project-description)
- [Virtual Environment Setup (using venv)](#virtual-environment-setup-using-venv)
- [Installation](#installation)
- [Run the tests](#run-the-tests)
- [Usage](#usage)

## Project Description

This project is about QR Code generation developed using Python. With this tool, you can input your URL, and the program will verify if it contains "HTTPS". If it does, it will generate and download an image of your QR Code.

## Virtual Environment Setup (using venv)

To set up a virtual environment for this project using `venv`, follow these steps:

## Create a virtual environment

In this case, the virtual environment created has the name `venv`.

```bash 
python -m venv venv  

# Activate the virtual environment.
# For Windows.
venv\Scripts\activate

# For macOS/Linux.
source venv/bin/activate
```

## Installation

```bash
python -m pip install -r requirements.txt

python setup.py build
python setup.py install

# The previous commands are required in order to run the unit tests inside the project.
# And make distinction between the `src/` that contain logic from the `src/` directory inside `tests`/
```

## Run the tests

```bash
# `pytest` could discover your test directory.
pytest

# Or you could explicit define the directory where to execute the tests.
pytest tests/
```

## Usage 

```bash 
git clone https://github.com/nesrineabkk/QR-CODE-PYTTHON-PROJECT.git

python src/main.py
```
