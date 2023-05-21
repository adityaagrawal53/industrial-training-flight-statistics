from flask import *
from database2graph import funk
from determineClosestFurthest import closest_furthest
# import "database-to-graph.py"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flight_routing', methods=['GET', 'POST'])
def flight_routing():
   if request.method == 'POST':
      result = request.form         
      funk(result)
      return render_template("flight_routing.html", result=result)
   
@app.route('/furthest_closest', methods=['GET', 'POST'])
def furthest_closest():
   if request.method == 'POST':
      closest, furthest = closest_furthest(int(request.form["id"]))
      closest_id = closest[0]
      closest_d = closest[1]
      furthest_id = furthest[0]
      furthest_d = furthest[1]
      return render_template("furthest_closest.html", source=request.form["id"], closest_id=closest_id, closest_d=closest_d,
                             furthest_d=furthest_d, furthest_id=furthest_id)
   
@app.route('/documentation.html')
def documentation():
   return render_template('documentation.html')

@app.route('/survey.html')
def survey():
   return render_template('survey.html')

if __name__ == '__main__':
  app.run(debug=True)
