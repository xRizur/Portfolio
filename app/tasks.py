from flask import Blueprint, request, session, redirect, render_template, url_for
from flask_mysqldb import MySQLdb
from flask import current_app


tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET', 'POST'])
def tasks():
    mysql = current_app.mysql

    if 'loggedin' in session:
        if request.method == "POST":
            task = request.form.get("task")
            if len(task) > 0:  # prevent adding empty tasks
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('INSERT INTO tasks (user_id, task) VALUES (%s, %s)', (session['userId'], task))
                mysql.connection.commit()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM tasks WHERE user_id = %s', (session['userId'],))
        tasks = cursor.fetchall()
        return render_template('tasks.html', tasks=tasks)
    else:
        return redirect('/login')

@tasks_bp.route('/tasks/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    mysql = current_app.mysql
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = %s AND user_id = %s', (task_id, session['userId']))
    mysql.connection.commit()
    cursor.close()
    return redirect('/tasks')


@tasks_bp.route('/edit/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    mysql = current_app.mysql
    cur = mysql.connection.cursor()
    new_task = request.form['task']
    cur.execute('UPDATE tasks SET task = %s WHERE id = %s', [new_task, task_id])
    mysql.connection.commit()
    return redirect(url_for('tasks.tasks'))
