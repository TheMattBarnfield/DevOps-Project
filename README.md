# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### Requirements

*Poetry
*Python
*A trello account

### Installing dependencies
```bash
$ poetry install
```

### Create a trello board

Create a trello board with the columns:
*`Not Started`
*`In Progress`
*`Completed`

### Environment variables

Copy `.env.template` to `.env` and fill it in with the correct values.

### Run the app

Once the setup script has completed and all packages have been installed, start the Flask app by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Tests

For the end-to-end tests, you'll need to install firefox and Gecko Driver.

Run the tests with the command:
```poetry run pytest tests/<unit|integration|e2e>```
