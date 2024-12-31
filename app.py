from flask import Flask, render_template 
from models import fetch_data 
from views import render_data 
app = Flask(__name__) 
@app.route('/') 
def home(): 
    data = fetch_data() 
    return render_data(data) 
if __name__ == '__main__': 
    app.run(debug=True) 