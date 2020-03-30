from flaskrecap import app,db

from flask import render_template,request,redirect,url_for

from flaskrecap.forms import TodoForm

from flaskrecap.models import Todo


#CRUD
#Create Retrieve Update Delete

@app.route('/', methods=['GET','POST'])
def home():
    form = TodoForm()
    if request.method == 'POST' and form.validate():
        task = form.task.data
        assignee = form.assignee.data
        assigner = form.assigner.data
        description = form.description.data
        print(f'Task: {task} \n Assignee:{assignee} \n Assigner:{assigner} \n Description:{description}')

        db.session.add(Todo(task,assignee,assigner,description))
        db.session.commit()
    return render_template('home.html',form=form)

@app.route('/todos',methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return render_template('todos.html',todos = todos)

@app.route('/todos/update/<int:todo_id>',methods=['GET','POST'])
def update_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id) # todo.id

    updateForm = TodoForm()
    if request.method == 'POST' and updateForm.validate():
        task = updateForm.task.data
        assignee = updateForm.assignee.data
        assigner = updateForm.assigner.data
        description = updateForm.description.data

        todo.task = task
        todo.assignee = assignee
        todo.assigner = assigner
        todo.description = description

        db.session.commit()
        return redirect(url_for('get_todos'))
    return render_template('update_todos.html',form = updateForm)


# Detail View for Todos
@app.route('/todos/<int:todo_id>')
def todo_detail(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    return render_template('todo_detail.html', todo = todo)


# Delete Route for Todos

@app.route('/todos/delete/<int:todo_id>')
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('get_todos'))