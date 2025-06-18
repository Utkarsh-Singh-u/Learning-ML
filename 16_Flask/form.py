from flask import Flask, render_template, request
'''  
it will create an instance of the flask class,
which will be your WSGI application.
'''
##WSGI application
app= Flask(__name__)

@app.route("/")
def welcome():
  return "Welcome to the Flask Application!"

@app.route("/form", methods = ['GET','POST,'])
def form():
  if request.method=='POST':
    pass
  return render_template('form.html')

@app.route("/submit", methods=['POST','GET'])
def submit():
  if request.method=='POST':
    name= request.form['name']
    return f" hello {name}"
  return render_template('form.html')

if __name__ == '__main__':
  app.run(debug=True)