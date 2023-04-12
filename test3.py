import boto3
import json

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

# write the inventory data to an output file
# replace 'inventory.json' with your desired file name
with open('inventory.json', 'w') as f:
    f.write(inventory_json)
