from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html", title="Login")





if __name__ == '__main__':
    app.run(host='localhost', port='8080', debug = True)