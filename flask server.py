from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/1')
def page1():
    return render_template('1.html')

@app.route('/2')
def page2():
    return render_template('2.html')
if __name__ == '__main__':
    app.run(debug=True)