# Flask Todo App

This is a simple Todo list application built using Flask.

## Features

- Users can create, update, delete, and view todo tasks.
- Tasks are stored in a SQLite database.
- Minimalistic user interface.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/mohitrajrathor/flask_todo_app.git
```


2. Navigate into the project directory:
```bash 
cd <path to your working directory>
```


3. Create a virtual environment:
```bash
python -m venv venv
```


4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. Install the required dependencies:
```bash
pip install -r requirements.txt
```


## Usage

1. Ensure you're in the project directory and the virtual environment is activated.

2. Run the Flask application:
```bash
flask run --app app.py
```


3. Open a web browser and navigate to `http://localhost:5000` to access the Todo app.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new Pull Request.


## Acknowledgments

- Flask documentation: https://flask.palletsprojects.com/
- SQLite documentation: https://www.sqlite.org/docs.html
- Bootstrap: https://getbootstrap.com/
