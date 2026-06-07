#integrate HTML with flask
#HTTP verb GET and POST
'''
    jinja2 template engine
    {%...%} conditions, for loops
    {{   }} expressions to print output
    {#...#} this is for comments
'''
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',result=res,score=score)

# @app.route('/fail/<int:score>')
# def fail(score):
#     return "<html><body><h1>The Result is failed</h1></body></html>"

#result checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score=marks))

#result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        math=float(request.form['maths'])
        c=float(request.form['c'])
        ds=float(request.form['ds'])
        total_score=(science+math+c+ds)/4
    res=""
    if total_score >= 50:
        res="success"
    else:
        res="fail"
    return redirect(url_for(res,score=total_score))

if __name__=='__main__':
    app.run(debug=True)