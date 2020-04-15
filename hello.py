from flask import Flask,render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'

@app.route('/hello/')
def hello_name(user):
    return render_template('hello.html',name=user)
	
if name=="__main__":
    app.run(debug=True)