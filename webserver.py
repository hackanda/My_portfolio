from flask import Flask, render_template, url_for , request , redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<text>')
def Page(text):
	try:
		return render_template(text)
	except:
		return f'Improper URL'

def Write_to_file(data):
	with open('Data.txt' , 'a') as file:
    		file.write(str(data))
    		file.write('\n')

# This function allows to write the data into a text file . But ideally we want to save 
# the data in csv file. for that we will be using CSV module (inbuilt).

def Write_to_csv(data):
	message = data['Message']
	email = data['Email']
	subject = data['Subject']
	with open('database.csv' , 'a' ,newline = '') as file:
		csv_writer = csv.writer(file , delimiter = ',' , quotechar = '"' , quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	print(data)
    	#Write_to_file(data)
    	Write_to_csv(data)	
    	return redirect('/thanks.html') # If we use this The contents of the html page will change with the redirected url.
    	# return render_template('/thanks.html')  If we use this then the url will stay same and only the contents of the html page will change
    else:
    	return 'Something Went wrong...'

# This change will be reflected in github .