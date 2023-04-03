import boto3
import requests
import json
import pandas as pd

# set up S3 client
s3 = boto3.client('s3')

# make API request and load JSON data
response = requests.get('<api>')
data = json.loads(Json.txt)

# create pandas DataFrame from JSON data
df = pd.json_normalize(data)

# create Excel file from DataFrame
file_name = 'users.xlsx'
df.to_excel(file_name, index=False)

# upload Excel file to S3 bucket
bucket_name = '<s3_Bucket>'
s3.upload_file(file_name, bucket_name, file_name)

print(f'File {file_name} uploaded to S3 bucket {bucket_name}.')
