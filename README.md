# My task submition for Softserve

[![tests](https://github.com/Vicente-G/Softserve-Task/actions/workflows/ci.yml/badge.svg)](https://github.com/Vicente-G/Softserve-Task/actions/workflows/ci.yml)
[![license](https://img.shields.io/badge/license-MIT-purple.svg)](https://github.com/Vicente-G/Database-Model/blob/main/LICENSE)
[![pdm-managed](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fpdm-project%2F.github%2Fbadge.json)](https://pdm-project.org)

As part of my selection process to join the team as a Python test automation junior developer, I am uploading this repository with my answers to the three questions sended to me. As the role is for a test automation, every part of the task's functionalty is covered by automated tests using the examples provided, mocking on some Python builtins when required to fully automate the user's input on the console when required.

## The task

* Create a program that takes an input file, and filter its lines to add only the palindromes to a new file as its output.

* Create a Python class that serve as a Bank Account manager with the 4 methods listed, essentially a custom counter which keeps track of the account's balance, updated only via user input.

* Create a Ball Clock with 2 working modes:
    * A mode that takes the number of balls and returns the number of days (24 hrs) it takes to sort them back to its original order.
    * And another mode that displays the state of the clock after a certain number of minutes have passed.


## Installation

To run this CLI locally, you may require `Python` which can be downloaded [here](https://www.python.org/downloads/) or you may require the `Docker` daemon, which can be easily obtained with [Docker Desktop](https://www.docker.com/products/docker-desktop/) or [Colima](https://github.com/abiosoft/colima).

Following the local installation, run the following commands in order:

```sh
git clone https://github.com/Vicente-G/Softserve-Task
cd softserve-task
```

Now you should be on the CLI folder, from where you can run it with either `Python` or `Docker`, depending on your needs.

## Running

To run this example using `Python`, install `pdm` to manage the dependencies and get it to sync with the lock file, like this:

```sh
pip install --user pdm
pdm sync
```

With all setup, go and run the `test` or `start` scripts to check the functionality by questions, like this:

```sh
# Run the CLI to do any manual testings
pdm run start -h
```
```sh
# Run the already automated tests
pdm run test
```

In the other hand, if you plan to use `Docker`, so "it runs in your machine as well", it may take longer to run, but it may be simpler depending on the case. To build and run, use the following commands:

```sh
docker build -t softserve-task .
docker run softserve-task
```

The `Dockerfile` is pre configured to run the automated tests, but the CLI can be run as well with little changes.

