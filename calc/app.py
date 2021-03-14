from flask import Flask, request
from operations import op

app = Flask(__name__)


@app.route('/add')
def add():
    a,b = get_args(request)
    return str(op['add'](a,b))

@app.route('/sub')
def sub():
    a,b = get_args(request)
    return str(op['sub'](a,b))

@app.route('/mult')
def mult():
    a,b = get_args(request)
    return str(op['mult'](a,b))

@app.route('/div')
def div():
    a,b = get_args(request)
    return str(op['div'](a,b))

@app.route('/math/<operation>')
def test_all_in_one(operation):
    a,b = get_args(request)
    return str(op[operation](a,b))

def get_args(request):
    a = int(request.args['a'])
    b = int(request.args['b'])
    return a,b