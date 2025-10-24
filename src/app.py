from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates', static_folder='static')

# Lista para armazenar tarefas (em memória)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form.get('description', '')
    tasks.append({'title': title, 'description': description, 'completed': False})
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)