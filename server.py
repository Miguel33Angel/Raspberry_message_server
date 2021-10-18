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

last_messages=[
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9'
]


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', users=users, last_messages=last_messages)


@app.route('/', methods=['POST'])
def receive_message():
    for user in users:
        key = "message_to_"+user['name']
        message = request.form[key]
        if len(message) > 0:
            user['last_m'] = message
        for i in range(9):
            last_messages[i] = last_messages[i + 1]
        last_messages[9] = message

    return render_template('home.html', users=users, last_messages=last_messages)


@app.route('/message/<ESP32_id>', methods=['GET'])
def send_message(ESP32_id):
    n = int(ESP32_id)
    return users[n].get('last_m')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # print("Server running")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
