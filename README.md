

# How to use this branch

This part of the seminar involves installing and getting started with django channels.

To get this running, simply run the  the following 

## Step 1: Install requirements.txt

`pip install -r requirements.txt`

## Step 2: Create databases

Create the databases and the initial migrations with the following command:
`python manage.py migrate`

## Step 3: Run server Also run ngrok

And start the server with 

`python manage.py runserver`

  ngrok http 8000

You should now be able to go to localhost:8000/chat/ and chat with the bot

## To see the no.of click on each button

localhost:8000/show/

## To clear all entries

localhost:8000/clear/




