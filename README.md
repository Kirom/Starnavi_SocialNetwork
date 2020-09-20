# Starnavi_SocialNetwork
Test assessment by Starnavi.


If you have any questions, you can contact me in telegram @Nizhdanchik or email me viktor.mironov.dev@gmail.com.

Postman collection provided for API testing.
Postman collection link: https://www.getpostman.com/collections/877388e9706ffd96bb03

To authorize you need to provide JWT in headers. Example: Key: `Authorization`, Value: `Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwNjIxMDg5LCJqdGkiOiJhMWQ2YjFkODRiZjQ0MDgzODAxMTcyOTRkNTIwMjc5MCIsInVzZXJfaWQiOjEwfQ.rsDKv2A8k52YpBLxfF5VzfzEDAiD-h7neWNPJEj9Hf0`.

You can register an account by 'Create user' request. You need to provide username and password in request's body. 

You can obtain JWT by 'Obtain JWT' request. You need to provide existing username and password in request's body. 

## Running all the stuff
1. Clone repo: `git clone https://github.com/Kirom/Starnavi_SocialNetwork.git`
2. Create virtualenv, for example: `python3 -m venv venv` or `virtualenv -p python3 venv`
3. Activate it `source venv/bin/activate`
4. Install all the packages `pip install -r requirements.txt`
5. Start the app itself `./manage.py runserver`

