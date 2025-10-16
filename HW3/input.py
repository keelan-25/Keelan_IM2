from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/signup')
def form():
    return render_template('form.html')


@app.route('/profile', methods=['POST'])
def profile():
    name = request.form['name']
    username = request.form['username']
    age = request.form['age']
    bio = request.form['bio']
    hobby = request.form['hobby']
    return render_template('profile.html', 
                           name=name, 
                           username=username, 
                           age=age, 
                           bio=bio, 
                           hobby=hobby)

if __name__ == '__main__':
    app.run(debug=True)
