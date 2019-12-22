from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/home_2')
def home222():
	return render_template('home_2.html')

@app.route('/blogs')
def blogs():
	return render_template('blogs.html')

@app.route('/recursos')
def recursos():
	return render_template('recursos.html')

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)