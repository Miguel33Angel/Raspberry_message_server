# Basic server used in a raspberry pi for connecting to a ESP32 that acts as a beeper
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html')


# if __name__ == '__main__':
#     print("Server running")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
