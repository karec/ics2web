from flask import Flask, jsonify
from icalendar import Calendar

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"


dic = [
    {
        'event': 'toto',
        'date': '29/01/14',
        'hour': '16h',
        'part': [
            'toto',
            'titi',
            'tata'
        ]
    }
]

@app.route('/get')
def get():
    return jsonify({'event': dic})

if __name__ == '__main__':
    app.run(debug=True)