from flask import Flask,render_template,url_for,request,redirect

app = Flask(__name__)
print(__name__)

@app.route('/')
def hello():
		return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
		return render_template(page_name)

def write_to_file(data):
	with open('database.txt',mode='a') as database:
		name=data["name"]
		email=data["email"]
		code=data["code"]
		time=data["time"]
		people=data["people"]

		file=database.write(f'\n name:{name}\n email:{email} \ncode:{code}\n time:{time}\npeople:{people}\n\n')
		


@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_file(data)
		return render_template('./invitation.html',name=data["name"],time=data["time"])
	else:
		return 'something went wrong'
	

app.run(debug=True)
