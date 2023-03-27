from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1

    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session.clear()

    return redirect('/')

@app.route('/action_buttons', methods=['POST'])
def action_buttons():
    if request.form['select'] == 'add_two':
        session['counter'] += 1
    elif request.form['select'] == 'reset':
        session['counter'] = 0
    
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)