#from flask import Flask,render_template
from flask import Flask,render_template,redirect,url_for,make_response,request,abort

app=Flask(__name__)

@app.route('/')
def index():
#    return 'Hello World!'
#    return redirect(url_for('user_index',username='default'))
    username=request.cookies.get('username')
    return 'Hello ,just a test,username={}'.format(username)

@app.route('/user/<username>')
def user_index(username):
#    return render_template('user_index.html',username=username)
    if username=='invalid':
        abort(404)
    
    resp=make_response(render_template('user_index.html',username=username))
    resp.set_cookie('username',username)
    
    return resp

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__=='__main__':
    app.run()
 
