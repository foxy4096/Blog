# Blog
A simple Blog app made with django


<h2>Instructions</h2>

<h4>Make sure you have <a href="https://python.org/downloads/"> python</a> installed</h4>

Step 1. Open a terminal

Step 2. Type this command
```
pip install pipenv
```

Step 2. Paste the given code in the terminal
```
git clone https://github.com/foxy4096/Blog.git
```
Step 3. Now type this in the terminal
```
cd Blog
```
Step 4. Now paste this in the terminal
```
pipenv install --ignore-pipfile
# and 
pipenv shell
```
Step 5. Now type
```
python manage.py makemigrations
# and
python manange.py migrate
```
Step 6. Now go type this command to create a new superuser
```
python manage.py createsuperuser
```
Step 7. After that type this and go to your web browser and go to <a href="http://localhost:8000">here</a>
```
python manage.py runserver
```