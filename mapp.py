from flask import Flask
from flask import request, url_for, render_template, redirect
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def my_maps():

  mapbox_access_token = 'pk.eyJ1IjoibWFyYWgtenVraGEiLCJhIjoiY2xjZzQzeTdsMG5wdTNxcWgydDVyY2UxYiJ9.5fl6hXtBEmL7FLjo6-rIUA'

  return render_template('index.html',
        mapbox_access_token=mapbox_access_token)





if __name__ == '__main__':
    app.run(debug=True)