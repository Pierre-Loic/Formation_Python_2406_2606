from flask import Flask, render_template, request
from flask_classful import FlaskView
from TicTacToes.TicTacToe import TicTacToe



class SiteTicTacToe(TicTacToe,FlaskView) :
    app = Flask(__name__)        

    def construct_IHM(self):
        self.restart_IHM()

    #@app.route('/')
    #def morpion(self):
    #    print(request.args.get('number'))
    #    return render_template("main.html", data=self.data)      
    
    @app.route('/')
    def index(self):
    # http://localhost:5000/
        return "<h1>This is my indexpage</h1>"


    def bsicname(self):
    # customized route
    # http://localhost:5000/diffrentname
        return "<h1>This is my coustom route</h1>"
       

    def launch_IHM(self):
        self.app.run()

        
    def restart_IHM(self):
        self.data = {
            1: " ",
            2: " ",
            3: " ",
            4: " ",
            5: " ",
            6: " ",
            7: " ",
            8: " ",
            9: " "
            }
