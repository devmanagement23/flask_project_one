from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, duniya'

@app.route('/products')
def products():
    return 'Select the products you like'

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True,port=8000)