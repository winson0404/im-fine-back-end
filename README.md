# im-fine-back-end

## Set run configuration in Pycharm
1. right click `manage.py` at root and click run
2. go top right and click `manage.py` button to `edit configuration`
3. go to `Python/manage` and add `runserver` to parameter
4. now u can just run the backend server by clicking run button

## Getting the dependencies
Simply run `pip install -r requirements.txt` to install all required dependencies.

## Running the server
1. Run `python manage.py makemigrations`.
2. Run `python manage.py migrate`.
3. Run `python manage.py runserver`.

## Opening schema
After running the server, navigate `http://127.0.0.1:8000/`
