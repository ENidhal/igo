from flask import Flask ,render_template,url_for



app = Flask (__name__,template_folder='template')

@app.route('/')
def index():
	
	return render_template('index.html')

@app.route('/Timesheet.html')
def about():
	
	return render_template('Timesheet.html')

@app.route('/Service.html')
def service():
	
	return render_template('CRA.html')


@app.route('/login.html')
def login():
	
	return render_template('login.html')

@app.route('/register.html')
def registre():
	
	return render_template('register.html')

@app.route('/forgot-password.html')
def forgot():
	
	return render_template('forgot-password.html')





if __name__=="__main__":
	app.run(debug=True)
