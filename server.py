# Basic server used in a raspberry pi for connecting to a ESP32 that acts as a beeper
# Important: the max num of characters that can be sent is 15 (defined in the HTML)
# Todo: security checks in the form.
# Todo: better looking form
# Todo: login page to introduce new ESP32


from flask import Flask, render_template, request

app = Flask(__name__)

users = [
        {'id': 0, 'name': 'Raquel', 'last_m': 'Hi!'},
        {'id': 1, 'name': 'Mangel', 'last_m': 'Hi!'}
    ]


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', users=users)


@app.route('/', methods=['POST'])
def receive_message():
    for user in users:
        key = "message_to_"+user['name']
        message = request.form[key]
        if len(message) > 0:
            user['last_m'] = message

    return render_template('home.html', users=users)


@app.route('/message/<ESP32_id>', methods=['GET'])
def send_message(ESP32_id):
    n = int(ESP32_id)
    return "Hola "+users[n].get('name')+"! ESP n:"+str(n)


if __name__ == '__main__':
    # app.run(debug=True, port=8800) Only if no terminal is being used
    print("Server running")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
