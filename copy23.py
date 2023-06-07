import boto3

source_account_id = 'YOUR_SOURCE_ACCOUNT_ID'
source_role_name = 'YOUR_SOURCE_ROLE_NAME'
target_account_id = 'YOUR_TARGET_ACCOUNT_ID'
target_role_name = 'YOUR_TARGET_ROLE_NAME'
region = 'YOUR_REGION'

# Assume the source role
sts_client = boto3.client('sts')
source_role_arn = f'arn:aws:iam::{source_account_id}:role/{source_role_name}'
source_credentials = sts_client.assume_role(
    RoleArn=source_role_arn,
    RoleSessionName='AssumeRoleSession'
)['Credentials']

# Create a session with the assumed source role
source_session = boto3.Session(
    aws_access_key_id=source_credentials['AccessKeyId'],
    aws_secret_access_key=source_credentials['SecretAccessKey'],
    aws_session_token=source_credentials['SessionToken'],
    region_name=region
)

# List the AMIs in the source account
ec2_source_client = source_session.client('ec2')
source_amis = ec2_source_client.describe_images(Owners=['self'])['Images']

# Assume the target role
target_role_arn = f'arn:aws:iam::{target_account_id}:role/{target_role_name}'
target_credentials = sts_client.assume_role(
    RoleArn=target_role_arn,
    RoleSessionName='AssumeRoleSession'
)['Credentials']

# Create a session with the assumed target role
target_session = boto3.Session(
    aws_access_key_id=target_credentials['AccessKeyId'],
    aws_secret_access_key=target_credentials['SecretAccessKey'],
    aws_session_token=target_credentials['SessionToken'],
    region_name=region
)

# Copy the AMIs to the target account
ec2_target_client = target_session.client('ec2')
for ami in source_amis:
    response = ec2_target_client.copy_image(
        SourceImageId=ami['ImageId'],
        SourceRegion=region,
        Name=ami['Name'],
        Description=ami['Description']
    )
    print(f"Copied AMI: {response['ImageId']}")
