from flask import Flask,request,render_template,redirect, url_for
import requests
app =Flask(__name__)
BACKEND_URL = 'http://127.0.0.1:9000'

@app.route('/')
def home():
    name = request.values.get('name', 'someone')
    return render_template('index.html', name=name)

@app.route('/submit',methods=['POST'])
def submit():
    form_data = dict(request.form)
    name=request.form.get('name',"someone")
    response=requests.post(BACKEND_URL + '/submit',json=form_data)
    message=response.json().get("message", "unknown")
    if response.json().get("success", False):
        return redirect(url_for("success",name=name))
    else:
        return render_template('index.html',name=name,success=False,message=message)


@app.route('/success')
def success():
    name = request.args.get("name", "someone")

    return render_template(
        'submit.html',
        name=name,
        success=True,
        message="Data submitted successfully"
    )




if __name__ =='__main__':
    app.run()
