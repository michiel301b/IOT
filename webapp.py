from flask import *

app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index1')
def volvo():
    return render_template('index1.html')

if (__name__) == '__main__':
    app.run(debug=True)