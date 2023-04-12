import boto3
import json

def lambda_handler(event, context):
    # create a Boto3 client for each AWS service you want to inventory
    ec2_client = boto3.client('ec2')
    s3_client = boto3.client('s3')
    # add more clients for other services as needed

    # use the client to retrieve the inventory data
    ec2_inventory = ec2_client.describe_instances()
    s3_inventory = s3_client.list_buckets()
    # add more inventory calls for other services as needed

    # format the inventory data as JSON
    inventory_data = {
        "ec2": ec2_inventory,
        "s3": s3_inventory,
        # add more inventory data for other services as needed
    }
    inventory_json = json.dumps(inventory_data)

    # write the inventory data to an S3 bucket or other storage location
    # replace 'your-bucket-name' and 'inventory.json' with your desired values
    s3 = boto3.resource('s3')
    s3.Object('your-bucket-name', 'inventory.json').put(Body=inventory_json)

    # return a success message
    return {
        'statusCode': 200,
        'body': json.dumps('Inventory collected successfully!')
    }
