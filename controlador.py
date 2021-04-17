from flask import Flask, render_template, request, redirect
#import sentimientos as sentimientos

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'contacto@eabmodel.com' or request.form['password'] != 'eabmodel':
            error = 'Tu usuario o contraseña no coinciden'
        else:
            return redirect('http://127.0.0.1:5000/inicio')
    return render_template('login.html', error=error)

@app.route ("/inicio")
def inicio():
    return render_template ('inicio.html') 

@app.route ("/lugar")
def lugar():
    return render_template ('lugar.html') 
    
@app.route ("/login_vendedor")
def login_vendedor():
    error=None
    if request.method == 'POST': 
        if request.form['username'] != 'contacto@eabmodel.com' or request.form['password'] != 'eabmodel':
            error = 'Tu usuario o contraseña son incorrectos'
        else:
            return redirect(url_for('http://127.0.0.1:5000/inicio_vendedor'))
    return render_template ('login_vendedor.html') 

@app.route ("/inicio_vendedor")
def inicio_vendedor():
    return render_template ('inicio_vendedor.html') 


if __name__=="__main__":
    app.run(debug=True)