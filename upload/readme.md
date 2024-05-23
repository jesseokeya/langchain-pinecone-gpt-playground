Use this to run a local file-upload server.

# Setup

- Create a Pipenv enviornment with `pipenv shell` and then install dependencies with `pipenv install`
- Start the server with `python app.py`
- In the `pdf` project, find the `.env` file and change the `UPLOAD_URL` line to the following: `UPLOAD_URL=http://localhost:8050`
- Exit the Pipenv virtual enviorment and recreate using `pipenv shell`
- Run `inv dev` to restart the pdf application
