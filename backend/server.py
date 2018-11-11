from flask import Flask,json,Response
from flask_restful import Resource, Api
import db

app = Flask(__name__)
api = Api(app)

class ListProducts(Resource):
    def post(self):
        Cursor = db.get_connection()
        sql = "SELECT pid,pname,ptype,pdescription,pquantity,ppercentage,pimage FROM products WHERE pflag='0'"
        Cursor.execute(sql)
        row_headers=[x[0] for x in Cursor.description]
        rv = Cursor.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return json_data

api.add_resource(ListProducts, '/ListProducts')

if __name__ == '__main__':
    app.run(host='<server ip>',debug=True)

