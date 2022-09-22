from flask import Flask, redirect, url_for

### WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome To My Website :)"

@app.route('/success/<int:score>')
def success(score):
    return "pass socre is " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "fail socre is " + str(score)

### Result checker
@app.route('/results/<int:score>')
def results(score):
    result = ""
    if score < 50:
        result = 'fail'
    else:
        result = 'success'

    return redirect(url_for(result, score=score))

if __name__ == '__main__':
    app.run(debug=True)