from flask import Flask,request,g,make_response,render_template,session,redirect,url_for,flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required,DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)

class NameForm(FlaskForm):
  name = StringField('What is your name? ',validators=[DataRequired()])
  submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
  return render_template('500.html'),500

@app.route('/',methods=['GET','POST'])
def index():
  ug = request.headers.get('User-Agent')
  print('request headers:',request.headers)
  print('g:',g)
  # res = make_response( '<h1>Hello Python:)</h1><h2>%s</h2>' % ug,400)
  # res.set_cookie('answer','43')
  h = request.headers
  name = None
  form = NameForm()
  if form.validate_on_submit():
    old_name = session.get('name')
    name = form.name.data
    if old_name is not None and old_name != name:
      flash('Looks like you have changed your name!')
    session['name'] = name
    return redirect(url_for('index'))
  return render_template('index.html',form=form,name=session.get('name'))

@app.route('/user/<name>')
def user(name):
  # return '<h2>hello, %s !</h2>' % name
  return render_template('user.html',name=name)


if __name__ == '__main__':
  manager.run()