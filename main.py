from flask import Flask,render_template
import os

app = Flask(__name__,static_folder='static')

@app.route('/home',methods=['GET'])
@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/login.php',methods=['GET'])
@app.route('/admin',methods=['GET'])
def admin():
    return render_template('admin.html')


@app.route('/login',methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/about',methods=['GET'])
def test():
    return render_template('about.html')


@app.route('/<path:path>')
def catch_all(path):
    return render_template('home.html')

if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=False)
