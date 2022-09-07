from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    data = {"name":"KhunBall", "age":28, "salary":"5000"}
    return render_template("index.html", mydata = data)

@app.route('/about')
def about():
    products = ["เสื้อผ้า", "เตารีด", "ผ้าห่ม", "ยาสามัญประจำบ้าน", "คีย์บอร์ด"]
    return render_template("about.html", myproduct = products)

@app.route('/admin')
def admin():
    # ชื่อ อายุ
    username = "KhunBall"
    return render_template("admin.html", username = username)

@app.route('/sendData')
def signupForm():
    fname = request.args.get('fname')
    description = request.args.get('description')
    return render_template("thankyou.html", data = {"name": fname, "description": description})

if __name__ == '__main__':
    app.run(debug=True)

