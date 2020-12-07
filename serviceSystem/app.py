from flask import Flask,request, redirect, url_for, abort
from flask import render_template


app = Flask(__name__)

@app.route('/index')
def hello_world():
    return render_template('index.html')

@app.route('/landing')
def hello_world3():
    return render_template('landing.html')
@app.route('/generic')
def hello_world4():
    return render_template('generic.html')
@app.route('/result')
def hello_world5():

    return ("일단은 이렇게 나옴 ")
    # return render_template('generic.html')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method=='POST':
        pass
    elif request.method=='GET':
        temp=request.args.get('demo-name')
        print(temp)
        return (temp)
    #arr=request.form.get('demo-name')
    # print(arr)
    # return arr

if __name__ == '__main__':
    app.run()
    