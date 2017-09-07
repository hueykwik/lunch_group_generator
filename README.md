# Lunch Group Generator

A simple tool to help create random groups for lunch.

## Getting Started

### Prerequisites

Python 3, Click, and Pytest (for running unit tests).

```
pip install -r requirements.txt
```

## Using the App

### Make groups
To use an example roster:

```
cp roster-example.txt roster.txt
python lunch.py groups
```

### Adding people

```
python lunch.py add --name 'Jon Snow'
```

### Clearing the roster

```
python lunch.py clear
```

## Approach
First, I outlined user stories and also wrote down use cases I wouldn't handle.

I'll mention these below as User Stories and Future.

### User Stories

* As an employee, on Friday, I'll create a list of groups for lunch and paste the results in an e-mail or Slack message.
* As an employee, I'll add a new employee or set of employees to the roster.

### Future

* Way to view the roster from the CLI. (Workaround: Look at the text file)
* Way to delete a set of people from the roster. (Workaround: Use the text file)
* Program just stores data locally on one machine.
* Web UI
* Way to mark someone as unavailable for lunch.

After that, I started doing TDD to figure out how to divide a list of people into groups. Once I had that working, I created a skeleton CLI and then started filling in functionality.

In researching how to write good CLIs, I came across Click, so I spent a bit of time learning how to use it.
