from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('principal.html')  

if _name_ == '_main_':
    app.run(debug=True, port=5001)