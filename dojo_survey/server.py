from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html") #This route renders the Dojo Survey page with survey questions/comment box on it.

@app.route('/process', methods = ['POST'])
def submit():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favorite_language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result') #This post route will collect the information the user enters on the Dojo Survey page and store in session.  Then it will redirect user to result page.

@app.route('/result')
def result():
    return render_template("result.html") #This route will render the results of what the user entered on the Dojo Survey page, with a button on the bottom to "go back" to that page.

if __name__=="__main__":
    app.run(debug=True)

