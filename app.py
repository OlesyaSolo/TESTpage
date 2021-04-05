from flask import Flask, render_template, request

app = Flask(__name__)

tasks_method = ['play_game', 'sleep', 'drink_wine']

@app.route("/")
@app.route("/list")
def items():  
    return render_template("list.html", 
                           tasks=tasks_method)



@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'GET':
        return render_template("add.html")
    else:
        task_body = request.form.get('task_body', None)
        if task_body:
            tasks_method.append(task_body)
        return items()

  

if __name__ == "__main__":
    app.run(host="localhost", port="5000", debug=True)

