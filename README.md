# drf_library

A library system built with Django and Django REST framework


# How to run the project?

First, you have to install Python 3.11 before downloading the project. After that:

Step 1: Clone the project:
            
            git clone https://github.com/kirvaland/drf_library.git

Step 2: Change env.sample file to .env file

Step 3: Write your secret key and debug choice to your .env file

Step 4: Go inside project folder, open cmd and type the following commands to install Django, Django REST Framework and run the server:

            pip install -r requirements.txt
            python manage.py makemigrations
            python manage.py migrate
            python manage.py runserver

Step 5: Open the browser and go to localhost:8000