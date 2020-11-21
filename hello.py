from flask import Flask,request,g,make_response,render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
  ug = request.headers.get('User-Agent')
  print('request headers:',request.headers)
  print('g:',g)
  # res = make_response( '<h1>Hello Python:)</h1><h2>%s</h2>' % ug,400)
  # res.set_cookie('answer','43')
  h = request.headers
  return render_template('index.html',h=h)

@app.route('/user/<name>')
def user(name):
  return '<h2>hello, %s !</h2>' % name

if __name__ == '__main__':
  manager.run()