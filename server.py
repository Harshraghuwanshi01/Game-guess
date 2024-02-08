from flask import Flask,request,jsonify
import project_dao
from sql_connection import get_sql_connection

app=Flask(__name__)
connection=get_sql_connection()
@app.route('/getProducts',methods=['GET'])
def get_products():
    products=project_dao.get_all_products(connection)
    response=jsonify(products)
    
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
#@app.route('/hello')
#def hello():
    #return "hello how are you"
if __name__=="__main__":
    print("starting flask server")
    app.run(port=5000)
 