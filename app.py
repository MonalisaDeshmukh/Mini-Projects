from flask import Flask,request,render_template
from artifacts.utils import hpp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    data = request.form
    hpp_obj = hpp(data)
    result = hpp_obj.predict()
    return render_template('index.html', pred =result )

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = 8080)