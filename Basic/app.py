from flask import Flask,render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, SelectField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class MyForm(FlaskForm):
    name = StringField("ป้อนชื่อของคุณ")
    isAccept = BooleanField("ยอมรับเงื่อนไขบริการข้อมูล")
    gender = RadioField('เพศ', choices=[('male', 'ชาย'), ('female', 'หญิง'), ('other', 'อื่นๆ')])
    skill = SelectField('ความสามารถพิเศษ', choices=[('English', 'พูดภาษาอังกฤษ'), ('Sing', 'ร้องเพลง'), ('Game', 'เกม')])
    submit = SubmitField("บันทึก")

@app.route('/', methods=['GET', 'POST'])
def index():
    name = False
    isAccept = False
    gender = False
    skill = False
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        isAccept = form.isAccept.data
        gender = form.gender.data
        skill = form.skill.data
        # ลบข้อมูลจากแบบฟอร์ม
        form.name.data = ""
        form.isAccept.data = ""
        form.gender.data = ""
    return render_template("index.html", form=form, name=name, isAccept=isAccept, gender=gender, skill=skill)

if __name__ == '__main__':
    app.run(debug=True)