from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', place=request.form.get('place', 'Helsinki'))

@app.route('/documentation.html')
def documentation():
   return render_template('documentation.html')

@app.route('/survey.html')
def survey():
   return render_template('survey.html')

if __name__ == '__main__':
  app.run(debug=True)
