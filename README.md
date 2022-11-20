# Django Polls App

The project is deployed on Heroku: [http://mysite-tutorial.herokuapp.com/accounts/](http://mysite-tutorial.herokuapp.com/accounts/)

To develop/test this website, clone this repository and follow the instructions:

## Install Python requirements

```bash
pip install -r requirements.txt
```

## Apply Migrations

```bash
python manage.py migrate
```

## Collect Static Files

```bash
python manage.py collectstatic --no-input
```


## Run Django Web Server

```bash
python manage.py runserver
```

## Install Cypress
Keep the Django server running in on CMD or terminal.

Download and install [NodeJS](https://nodejs.org/en/download/) on your computer.

If the installation is successful, you will be able to run `npm` command from the CMD or terminal.

Open another CMD prompt or terminal, navigate to the polls app project root directory, and run the command:

```bash
npm i cypress --save-dev
```

This will download the cypress binaries in `node_modules` directory.

It will take several minutes to download and install cypress in the polls app's root directory.


## Run the Cypress tests

To execute all the cypress tests, run the following command:
```bash
npm run e2e
```
This command will open a new window and click on the `test.js` file to start the tests.


### (optional)
The below command executes all the tests in the Linux terminal
```bash
./node_modules/.bin/cypress run --headless --browser chrome
```