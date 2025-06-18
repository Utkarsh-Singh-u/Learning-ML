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


##variable rule
@app.route("/success/<int:score>")
def success(score):
  res=''
  if score>=50:
    res="PASS"
  else:
    res="FAIL"
  return render_template("result.html",result=res)


@app.route("/successres/<int:score>")
def successres(score):
  res=''
  if score>=50:
    res="PASS"
  else:
    res="FAIL"
  exp={'score':score,"res":res}
  return render_template("result1.html",result=exp)


if __name__ == '__main__':
  app.run(debug=True)