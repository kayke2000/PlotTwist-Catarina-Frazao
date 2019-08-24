from flask import FLask, request, render_template, redirect

app = Flask(__name__)

@app.route('/', methods =['POST'])
def login():
    pass





if __name__ == '__main__':
    app.run(host='localhost', port='8080', debug = True)