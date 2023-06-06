from flask import Flask, render_template
import pandas as pd
import numpy as np
app = Flask(__name__)

@app.route('/')
def index():
    from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    df=pd.read_csv('trainer.csv')
    options=df['New Trainer'].unique()
    selected_option = options[1]  # Set the desired selected option 
    return render_template('index1.html',options=options,selected_option=selected_option)

@app.route('/trainer',methods=['GET'])
def trainer():
    df=pd.read_csv('trainer.csv')
    return render_template('index.html',df=df)





if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)

