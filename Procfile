web: python manage.py collectstatic --no-input && python manage.py migrate && gunicorn -b 0.0.0.0:$PORT biblioteka.wsgi --log-level debug
