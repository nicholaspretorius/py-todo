from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:n1k1kn0x@localhost:5433/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    complete = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Todo ID: {self.id}, name: {self.description}, complete: {self.complete}>'


# db.create_all()


@app.route('/')
def index():
    return render_template('index.html', todos=Todo.query.order_by('id').all())


@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        # todo = request.form.get('description')
        description = request.get_json()['description']
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
        # return redirect(url_for('index'))
        # 'index' is the name of the controller for route '/'
    except():
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return jsonify(body)
    # if not error:
    #     # return jsonify({
    #     #     'description': todo.description
    #     # })
    #     return jsonify(body)


@app.route('/todos/<todo_id>/set-complete', methods=['POST'])
def update_todo(todo_id):
    error = False
    try:
        complete = request.get_json()['complete']
        todo = Todo.query.get(todo_id)
        print('Todo: ', todo)
        todo.complete = complete
        db.session.commit()
    except():
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
