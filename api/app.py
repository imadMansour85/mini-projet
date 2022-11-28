from flask import Flask, jsonify, request , redirect, url_for
import numpy as np

import pickle5 as pickle




# creating a Flask app
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'POST'):

        name = 'model.pkl'

        with open(name,'rb') as file:
            model = pickle.load(file)

        Arr = np.array([request.form['A1'],request.form['A2'],request.form['A3'],request.form['A4'],request.form['A5'],request.form['A6'],request.form['A7'],request.form['A8']]).reshape(1,-1)


        a = model.predict(Arr)
        
        #request.form['URL']
    
  
        
        return jsonify({'data': a[0]})
  
  


# driver function
if __name__ == '__main__':

  
    app.run(debug = True)
