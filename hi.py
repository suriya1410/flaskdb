from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello_world():
    return 'Hello World Rishi'

if _name_ == '_main_':
   app.run(host="0.0.0.0", port=80)
