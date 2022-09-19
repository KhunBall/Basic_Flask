from flask import Flask,render_template, request, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class MyForm(FlaskForm):
    name = StringField("ป้อนชื่อของคุณ", validators=[DataRequired()])
    isAccept = BooleanField("ยอมรับเงื่อนไขบริการข้อมูล")
    gender = RadioField('เพศ', choices=[('male', 'ชาย'), ('female', 'หญิง'), ('other', 'อื่นๆ')])
    skill = SelectField('ความสามารถพิเศษ', choices=[('English', 'พูดภาษาอังกฤษ'), ('Sing', 'ร้องเพลง'), ('Game', 'เกม')])
    address = TextAreaField("ที่อยู่ของคุณ")
    submit = SubmitField("บันทึก")

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['isAccept'] = form.isAccept.data
        session['gender'] = form.gender.data
        session['skill'] = form.skill.data
        session['address'] = form.address.data
        # ลบข้อมูลจากแบบฟอร์ม
        form.name.data = ""
        form.isAccept.data = ""
        form.gender.data = ""
        form.address.data = ""
    return render_template("index.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)