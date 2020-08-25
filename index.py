from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/blogs')
def blogs():
	return render_template('blogs.html')

@app.route('/recursos')
def recursos():
	return render_template('recursos.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/codeProgramacion')
def programacion():
	return render_template('codeProgramacion.html')

@app.route('/ciberseguridad')
def ciberseguridad():
	return render_template('cyberSeguridad.html')

@app.route('/login')
def login():		
	return render_template('login.html')

@app.route('/tipsSeguridadTech')
def tipsTecnologia():
	return render_template('tipsTecnologia.html')

@app.route('/blogContenidos')
def blog_contenidos():
	return render_template('formulario_blog.html')

@app.route('/crear_cuenta')
def crearCuenta():
	return render_template('crearCuenta.html')
if __name__ == '__main__':
	app.run(debug=True)

