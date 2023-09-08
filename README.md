# Market-place-API
REST API for the internet service for creating supplies advertisments. Users can create advertisments, rate supplies and communicate with each other to sell and buy supplies.

# Launch project in the dev-mode
- Create and activate virtual environment
- Install dependencies from requirements.txt file:
```
pip install -r requirements.txt
```
- Apply the migrations of the project:
```
python3 manage.py migrate
```
- In folder with file manage.py execute a command:
```
python3 manage.py runserver
```
- You can read the documentation by following the link:
```
[http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)
```
