from flask_app import app
from flask_app.controllers import controller_shows, controller_users
# ...server.py


if __name__ == "__main__":
    app.run(debug=True)