import boto3

# create a boto3 session
session = boto3.Session()

# create a client for the AWS Config service
config_client = session.client('config')

# call the list_discovered_resources API to get the inventory
inventory = config_client.list_discovered_resources()

# print the inventory
print(inventory)
