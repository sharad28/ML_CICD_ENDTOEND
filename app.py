from flask import Flask, render_template, request, jsonify
from flask_cors import CORS,cross_origin
import os
import numpy as np
#from src import train_and_evaluate

webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

@app.route('/',methods= ['GET'])
@cross_origin()
def homepage():
    #print(train_and_evaluate.scores)
    return render_template("index.html")


if __name__ == '__main__':
    app.run()