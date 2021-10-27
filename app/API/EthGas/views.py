try:
    from flask import Flask
    from flask_restful import Resource, Api
    from apispec import APISpec
    from marshmallow import Schema, fields
    from apispec.ext.marshmallow import MarshmallowPlugin
    from flask_apispec.extension import FlaskApiSpec
    from flask_apispec.views import MethodResource
    from flask_apispec import marshal_with, doc, use_kwargs
    import json
    import requests
    import string

    print("All imports are ok............")
except Exception as e:
    print("Error: {} ".format(e))

#class EthGasControllerSchema(Schema):
#    name = fields.String(required=True, description='name is required ')

class EthGasController(MethodResource, Resource):
    @doc(description='Eth Gas Prices API', tags=['EthGas Endpoint'])
#    @use_kwargs(EthGasControllerSchema, location=('json'))
    def get(self):

        '''
        Get method represents a GET API method
        '''
        resp = requests.get('http://ethgas.watch/api/gas').json()
        ids_str = json.dumps(resp)
        d = json.loads(ids_str)
        return d
        #return {'message': 'Eth Gas API'}, 200

#    def post(self):
#        _message = kwargs.get("name", "default")
#        response = {"message":_message}
#        return response
