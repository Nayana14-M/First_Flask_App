from flask import Flask, render_template, request, Response, redirect, url_for, session

app=Flask(__name__)
app.secret_key = 'nayana'

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('checkprofile'))
    else:
        return render_template('login.html')

@app.route('/checkprofile')
def checkprofile():
    username = session.get('username')
    if username:
        return render_template('dashboard.html', username=username)
    return redirect(url_for('login'))

#Dynamic Routing
@app.route('/user/<name>')
def welcome(name):
    return f" Hello {name}"
    
#Request -Handling 
@app.route('/requestsubmit', methods=['POST', 'GET'])
def reqHandle():
    #Handling methods
    if request.method == 'POST':
        age=request.form['age']
        name=request.form['name']
        #return f"Name : {name} & Age: {age}"
        return render_template('profile.html', age=age, name=name)
    else:
        return "Hello redirect"

#Response - Handling
@app.route('/custom')
def custom_response():
    return Response("Custom response", status=202, mimetype='text/plain')

#Redirect -redirecting to another route
@app.route('/redirectroute')
def redirectroute():
    return redirect('requestsubmit')

#URL_FOR 

@app.route('/dashboard')
def dashboard():
    return "I am in dashboard"

@app.route('/urlforuse')
def urlfor():
    return redirect(url_for('dash'))

@app.route('/logout')
def logout():   
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == "__main__" :
    app.run(port=5005, debug=True)
    