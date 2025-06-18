from flask import Flask
'''  
it will create an instance of the flask class,
which will be your WSGI application.
'''
##WSGI application
app= Flask(__name__)

@app.route("/")
def welcome():
  return "Welcome to the Flask Application!"

@app.route("/index")
def index():
  return "Welcome to index page!"

if __name__ == '__main__':
  app.run(debug=True)