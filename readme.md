# COV-APP-19

## TO SETUP FIRST TIME
You have to have pip and pipenv installed 
if you don't have pipenv installed read the tutorial [here](https://www.pythontutorial.net/python-basics/install-pipenv-windows/)

Once repo is cloned, navigate into folder then run the command 
`pipenv shell`

This should start a virtual environment (make sure you are navigated into the folder with the PipFile)

Install the dependencies with 
`pipenv install`

then 
`cd govhacksite`

### Before running the server
Need to do a couple things before running the server 

first run the command 
`python manage.py migrate`

## TO START
if you haven't already start a pipenv shell with
`pipenv shell`

then if you aren't already in the base directory

`cd govhacksite`
then start start the server with 
`python manage.py runserver`

this should start the server on localhost:8000
