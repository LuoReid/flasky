from flask import Flask,request,g,make_response,render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
  return render_template('500.html'),500

@app.route('/')
def index():
  ug = request.headers.get('User-Agent')
  print('request headers:',request.headers)
  print('g:',g)
  # res = make_response( '<h1>Hello Python:)</h1><h2>%s</h2>' % ug,400)
  # res.set_cookie('answer','43')
  h = request.headers
  return render_template('index.html',h=h,current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
  # return '<h2>hello, %s !</h2>' % name
  return render_template('user.html',name=name)


if __name__ == '__main__':
  manager.run()