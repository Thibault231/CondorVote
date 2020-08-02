import os
import webbrowser

if __name__ == "__main__":
    os.system('python manage.py')
    webbrowser.open('http://127.0.0.1:8000/')
    os.system('python manage.py runserver')