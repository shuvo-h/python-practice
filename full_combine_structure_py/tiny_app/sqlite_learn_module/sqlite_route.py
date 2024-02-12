from flask import jsonify, request
from tiny_app import send_email_bp
from . import sql_controller

@send_email_bp.post('/insert_a_people')
def simple_query():
    bodyDataDict = request.get_json()
    result, status_code = sql_controller.insertSingleDocCtl(bodyDataDict)
    return jsonify(result), status_code

@send_email_bp.get('/get_all_docs')
def get_all_doc():
    query_params  = dict(request.args) # convert dictionary
   
    result, status_code = sql_controller.getAllDocsCtl(query_params)
    return jsonify(result), status_code