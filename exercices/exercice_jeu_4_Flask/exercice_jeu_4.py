from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def morpion():
    print(request.args.get('number'))
    data = {
        1: "X",
        2: "_",
        3: "O",
        4: "X",
        5: "O",
        6: "X",
        7: "_",
        8: "O",
        9: "X"
        }
    return render_template("main.html", data=data)

app.run()
