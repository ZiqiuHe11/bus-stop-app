Bus Stop Query System

Bus stop query website based on Flask and SQLite, supporting paginated browsing, search and bus stop details.

## Features

- Home page with search box and quick links

- Bus stop list, paginated display, support page jump

- Bus stop details page, display detailed address, type and coordinate information

- Search function, support fuzzy query by station name, street, and area

- Custom 404 error page

- Deployed in Render, support online access

## Technology stack

- Python 3.10 + Flask

- SQLite database

- Jinja2 template engine + Bootstrap 5

- Deployment: Render cloud platform

## Project structure

bus_stop_app/

├── app.py # Flask application main file

├── bus_stops.db # SQLite database file

├── templates/ # HTML template directory

│ ├── base.html

│ ├── index.html

│ ├── stops.html

│ ├── stop_detail.html
│ ├── search.html
│ └── 404.html
└── static/ # Static files (CSS, etc.)

## Run steps

1. Clone the repository and enter the directory
git clone https://github.com/your username/your repository name.git
cd your repository name
Create a virtual environment and install dependencies

cd ~/workspace/bus_stop_app
python3 -m venv venv
source venv/bin/activate
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=3000
Browser access
http://127.0.0.1:5000/


Online access address
The project has been successfully deployed on Render Cloud platform, access link:
https://bus-stop-app.onrender.com/
You can browse the bus stop list directly, support paging jump, for example:
Homepage: https://bus-stop-app.onrender.com/
Bus stop list (page 26): https://bus-stop-app.onrender.com/stops?page=26



Deployment instructions
Use Render platform to deploy, configure Python version to 3.10+
Specify the startup command: gunicorn app:app
The database file needs to be included in the project root directory