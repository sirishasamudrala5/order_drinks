from flask import Flask, jsonify, abort,make_response, request ,url_for
from flask_httpauth import HTTPBasicAuth
import sys
import json
import db
 
auth = HTTPBasicAuth()
app = Flask(__name__)

cur = db.get_connection()

@auth.get_password
def get_password(username):
    if username == 'username':
        return 'password'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
    # if the client is a web browser the above line trows an error and 
    # asks the user to enter login credentials
    # to avoid this we can change the error code to 403 - forbidden error
    # return make_response(jsonify({'error': 'Unauthorized access'}), 403)

# handling 404 status (sending json instead of html response)
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/FetchAds', methods=['POST'])
@auth.login_required
def fetch_ads():
    if not request.json:
        abort(400)
    print "SELECT * FROM Ads WHERE geo_hash={geo_hash} AND category={category} and offer_id>{offer_id}".format(geo_hash=json.dumps(request.json['Fetch'][0]),category=json.dumps(request.json['Fetch'][1]),offer_id=json.dumps(request.json['Fetch'][2]))
    rows = cur.execute("SELECT * FROM Ads WHERE geo_hash={geo_hash} AND category={category} and offer_id>{offer_id}".format(geo_hash=json.dumps(request.json['Fetch'][0]),category=json.dumps(request.json['Fetch'][1]),offer_id=json.dumps(request.json['Fetch'][2])))
    if rows<=0:
        abort(400)
    else:
        return json.dumps(cur.fetchall(), indent=2)
    

@app.route('/PushAd', methods=['POST'])
@auth.login_required
def push_add():
    if not request.json:
        abort(400)
    print "INSERT INTO Ads(merchant_id,category,valid_till_date,valid_till_month,valid_till_year,ad_img_url,item_desc,offer_code) VALUES({merchant_id},{category},{valid_till_date},{valid_till_month},{valid_till_year},{ad_img_url},{item_desc},{offer_code}) RETURNING ad_id".format(merchant_id =json.dumps(request.json['Ad'][0]), category=json.dumps(request.json['Ad'][1]),valid_till_date=json.dumps(request.json['Ad'][2]),valid_till_month=json.dumps(request.json['Ad'][3]),valid_till_year=json.dumps(request.json['Ad'][4]),ad_img_url=json.dumps(request.json['Ad'][5]),item_desc=json.dumps(request.json['Ad'][6]),offer_code=json.dumps(request.json['Ad'][7]))
    inserted_id = cur.execute("INSERT INTO Ads(merchant_id,category,valid_till_date,valid_till_month,valid_till_year,ad_img_url,item_desc,offer_code) VALUES({merchant_id},{category},{valid_till_date},{valid_till_month},{valid_till_year},{ad_img_url},{item_desc},{offer_code}) RETURNING ad_id".format(merchant_id =json.dumps(request.json['Ad'][0]), category=json.dumps(request.json['Ad'][1]),valid_till_date=json.dumps(request.json['Ad'][2]),valid_till_month=json.dumps(request.json['Ad'][3]),valid_till_year=json.dumps(request.json['Ad'][4]),ad_img_url=json.dumps(request.json['Ad'][5]),item_desc=json.dumps(request.json['Ad'][6]),offer_code=json.dumps(request.json['Ad'][7])))
    print inserted_id
    return jsonify({'OfferId': inserted_id}), 200

    
@app.route('/AddMerchant', methods=['POST'])
@auth.login_required
def add_merchant():
    if not request.json:
        abort(400)
    print "INSERT INTO Merchants(lat,lng,landmark,area,city,state,country,registered_on,is_active,last_ad_on,geo_hash,mechant_name,merchant_img_url) VALUES({lat},{lng},{landmark},{area},{city},{state},{country},{registered_on},{is_active},{last_ad_on},{geo_hash},{mechant_name},{merchant_img_url}) RETURNING id".format(lat=json.dumps(request.json['Merchant'][0]),lng=json.dumps(request.json['Merchant'][1]),landmark=json.dumps(request.json['Merchant'][2]),area=json.dumps(request.json['Merchant'][3]),city=json.dumps(request.json['Merchant'][4]),state=json.dumps(request.json['Merchant'][5]),country=json.dumps(request.json['Merchant'][6]),registered_on=json.dumps(request.json['Merchant'][7]),is_active=json.dumps(request.json['Merchant'][8]),last_ad_on=json.dumps(request.json['Merchant'][9]),geo_hash=json.dumps(request.json['Merchant'][10]),mechant_name=json.dumps(request.json['Merchant'][11]),merchant_img_url=json.dumps(request.json['Merchant'][12]))
    inserted_id = cur.execute("INSERT INTO Merchants(lat,lng,landmark,area,city,state,country,registered_on,is_active,last_ad_on,geo_hash,mechant_name,merchant_img_url) VALUES({lat},{lng},{landmark},{area},{city},{state},{country},{registered_on},{is_active},{last_ad_on},{geo_hash},{mechant_name},{merchant_img_url}) RETURNING id".format(lat=json.dumps(request.json['Merchant'][0]),lng=json.dumps(request.json['Merchant'][1]),landmark=json.dumps(request.json['Merchant'][2]),area=json.dumps(request.json['Merchant'][3]),city=json.dumps(request.json['Merchant'][4]),state=json.dumps(request.json['Merchant'][5]),country=json.dumps(request.json['Merchant'][6]),registered_on=json.dumps(request.json['Merchant'][7]),is_active=json.dumps(request.json['Merchant'][8]),last_ad_on=json.dumps(request.json['Merchant'][9]),geo_hash=json.dumps(request.json['Merchant'][10]),mechant_name=json.dumps(request.json['Merchant'][11]),merchant_img_url=json.dumps(request.json['Merchant'][12])))
    print inserted_id
    return jsonify({'MerchantId': inserted_id}), 200


if __name__ == '__main__':
    app.run(host='35.185.66.137',port='5557',debug=True)