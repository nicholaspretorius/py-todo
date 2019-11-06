from flask import Flask, render_template

app = Flask(__name__)

todos = [{
    'description': 'Todo 1'
}, {
    'description': 'Todo 2'
}, {
    'description': 'Todo 3'
}]


@app.route('/')
def index():
    return render_template('index.html', todos=todos)


if __name__ == '__main__':
    app.run(debug=True)
