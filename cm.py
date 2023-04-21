import json
import boto3
import random

def lambda_handler(event, context):
       
    serviceclient = boto3.client('servicediscovery')

    response = serviceclient.discover_instances(NamespaceName='dojoappnamespace', ServiceName='dataservices',  QueryParameters={ 'name': 'datatable' })
       
    tablename = response["Instances"][0]["Attributes"]["tablename"]
       
    dynamodbclient = boto3.resource('dynamodb')
       
    table = dynamodbclient.Table(tablename)
       
    response = table.put_item( Item={ 'id': str(random.randint(1,100)), 'todo': event } )
       
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
