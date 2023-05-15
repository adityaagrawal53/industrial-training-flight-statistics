from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flight_routing', methods=['GET', 'POST'])
def flight_routing():
   if request.method == 'POST':
      result = request.form     
      return render_template("flight_routing.html", result=result)

@app.route('/documentation.html')
def documentation():
   return render_template('documentation.html')

@app.route('/survey.html')
def survey():
   return render_template('survey.html')

if __name__ == '__main__':
  app.run(debug=True)
