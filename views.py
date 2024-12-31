from flask import render_template 
 
def render_data(data): 
    return render_template('index.html', users=data) 