from flask import *
from aps_listing_and_routing import funk
from closest_furthest_2 import closest_furthest
from aps_per_continent_by_src import find_continent
from counting import filter_and_count
# from mapping import filter_and_map

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/flight_routing', methods=['GET'])
def flight_routing():   
   country = request.args.get("country")      
   return redirect(url_for('flight_routing_place', country=country))

@app.route('/flight_routing/<country>')
def flight_routing_place(country):
   funk(country)
   return render_template("flight_routing.html", country=country)

@app.route('/furthest_closest', methods=['GET'])   
def furthest_closest():
   id = request.args.get('id')
   return redirect(url_for('furthest_closest_id', id=id))

@app.route('/furthest_closest/<id>')
def furthest_closest_id(id):   
   source, closest, furthest = closest_furthest(int(id))
   closest_id = closest[0]
   closest_d = closest[1]
   furthest_id = furthest[0]
   furthest_d = furthest[1]
   return render_template("furthest_closest.html", source=source, closest_id=closest_id, closest_d=closest_d,
                           furthest_d=furthest_d, furthest_id=furthest_id)
   
@app.route('/documentation.html')
def documentation():
   return render_template('documentation.html')

@app.route('/survey.html', methods=["POST", "GET"])
def survey():
   return render_template('survey.html')

@app.route('/aps_per_continent_by_src', methods=['GET'])
def redirect_aps_per_continent_by_src():
   source_city = request.args.get('source_city')
   return redirect(url_for('aps_per_continent_by_src', source_city = source_city))
@app.route('/aps_per_continent_by_src/<source_city>')
def aps_per_continent_by_src(source_city):
   find_continent(source_city)
   return render_template('aps_per_continent_by_src.html', source_city=source_city)

@app.route('/counting', methods=['GET'])
def redirect_counting():
   source_ap = request.args.get('source_ap')
   return redirect(url_for('counting', source_ap=source_ap))
@app.route('/countring/<source_ap>')
def counting(source_ap):
   filter_and_count(source_ap)
   return render_template('counting.html', source_ap=source_ap)

# @app.route('/mapping', methods=['GET'])
# def redirect_mapping():
#    country = request.args.get('country')
#    return redirect(url_for('mapping', country=country))
# @app.route('/mapping/<country>')
# def mapping(country):
#    filter_and_map(country)
#    return render_template('mapping.html', country=country)

if __name__ == '__main__':
  app.run(debug=True)
