release: python manage.py collectstatic --no-input && python manage.py migrate
web: gunicorn snapchat.wsgi --bind 0.0.0.0:$PORT --log-file -
