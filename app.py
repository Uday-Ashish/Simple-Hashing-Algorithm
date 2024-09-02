from flask import Flask ,render_template , request , redirect , url_for
import os
from finalized_modified import calculate,calculate_binary 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/submit', methods = ['POST'])
def result():

    result = None    
    option = request.form.get('option')

    if (option == 'text'):
        
        data = request.form.get('textinput')
        if(data):
            result = calculate(data)
            print(result)
    
    if (option == 'file'):
        
        file = request.files.get('fileinput')
        if(file):
            print('file present')
            try:
                data = file.read().decode('utf-8')
                result = calculate(data)
            except UnicodeDecodeError:
                result = "UnicodeDecodeError - currently only text based files are supported!!"
                file.seek(0)
                data= file.read()
                result = calculate_binary(data)
            
            print(result)
    
    return render_template('result.html',ans=result)

# if __name__ == '__main__' :
#     app.run()