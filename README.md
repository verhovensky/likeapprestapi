# Simple API

Featuring user sing up, registration, login, publication creation/deletion, publication like/unlike and statistics.

- JWT authentication
- User registration and sing up
- Publication creation (always made by user)
- Publication like/unlike
- User/publications/likes statistics

Requires:
- Django==3.2
- djangorestframework==3.12.4

## Install
Make venv/pipenv<br/>
Connect your favourite DB backend<br/>
(Optional) Adjust timezone settings in settings.py to fit your needs
Then in project folder:
```sh
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

## License

MIT

**Free Software**
