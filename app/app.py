from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'airbnbData'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Airbnb Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM airbnbtbl')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, airbnb=result)


@app.route('/view/<int:airbnb_id>', methods=['GET'])
def record_view(airbnb_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM airbnbtbl WHERE id=%s', airbnb_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', airbnb=result[0])


@app.route('/edit/<int:airbnb_id>', methods=['GET'])
def form_edit_get(airbnb_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM airbnbtbl WHERE id=%s', airbnb_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', airbnb=result[0])


@app.route('/edit/<int:airbnb_id>', methods=['POST'])
def form_update_post(airbnb_id):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('City'), request.form.get('fldState'), request.form.get('ActiveRentals'),
                 request.form.get('AverageDailyRate'), request.form.get('OccupancyRate'),
                 request.form.get('Revenue'), airbnb_id)
    sql_update_query = """UPDATE airbnbtbl t SET t.City = %s, t.fldState = %s, t.ActiveRentals = %s, t.AverageDailyRate = 
    %s, t.OccupancyRate = %s, t.Revenue = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)

@app.route('/airbnb/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Airbnb City Form')


@app.route('/airbnb/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('City'), request.form.get('fldState'), request.form.get('ActiveRentals'),
                 request.form.get('AverageDailyRate'), request.form.get('OccupancyRate'),
                 request.form.get('Revenue'))
    sql_insert_query = """INSERT INTO airbnbtbl (City,fldState,ActiveRentals,AverageDailyRate,OccupancyRate,Revenue) VALUES (%s, %s, %s, %s, %s, %s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)

@app.route('/delete/<int:airbnb_id>', methods=['POST'])
def form_delete_post(airbnb_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM airbnbtbl WHERE id = %s """
    cursor.execute(sql_delete_query, airbnb_id)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/airbnb', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM airbnbtbl')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/airbnb/<int:airbnb_id>', methods=['GET'])
def api_retrieve(city_id) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM airbnbtbl WHERE id=%s', airbnb_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp

@app.route('/api/v1/airbnb', methods=['POST'])
def api_add() -> str:
    cursor = mysql.get_db().cursor()
    content = request.json
    inputData = (content['City'], content['fldState'], content['ActiveRentals'],
                 content['AverageDailyRate'], content['OccupancyRate'],
                 content['Revenue'])
    sql_insert_query = """INSERT INTO airbnbtbl (City,fldState,ActiveRentals,AverageDailyRate,OccupancyRate,Revenue) VALUES (%s, %s, %s, %s, %s, %s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=201, mimetype='application/json')
    return resp

@app.route('/api/v1/airbnb/<int:airbnb_id>', methods=['PUT'])
def api_edit(airbnb_id) -> str:
    cursor = mysql.get_db().cursor()
    content = request.json
    inputData = (content['City'], content['fldState'], content['ActiveRentals'],
                 content['AverageDailyRate'], content['OccupancyRate'],
                 content['Revenue'],airbnb_id)
    sql_update_query = """UPDATE airbnbtbl t SET t.City = %s, t.fldState = %s, t.ActiveRentals = %s, t.AverageDailyRate = 
        %s, t.OccupancyRate = %s, t.Revenue = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp

@app.route('/api/v1/airbnb/<int:airbnb_id>', methods=['DELETE'])
def api_delete(airbnb_id) -> str:
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM airbnbtbl WHERE id = %s """
    cursor.execute(sql_delete_query, airbnb_id)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)