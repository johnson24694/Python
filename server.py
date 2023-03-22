from flask import Flask  
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'   #localhost:5000/ will return "Hello World!"

@app.route('/dojo')
def dojo():
  return "Dojo!"  #Localhost:5000/dojo will return "Dojo!"

@app.route('/say/<name>')
def say(name):
    print(name)
    return "Hi, "  + name + "!"  #localhost:5000/say/<name> will return Hi, <name>! 

@app.route('/repeat/<times>/<name>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def repeat(times, name):
    print(times)
    print(name)
    return str(name) * int(times)  #prints the "name" as a string "times" number of times.

if __name__=="__main__":
    app.run(debug=True)