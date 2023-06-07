import boto3

source_account_id = 'YOUR_SOURCE_ACCOUNT_ID'
destination_account_id = 'YOUR_DESTINATION_ACCOUNT_ID'
source_region = 'us-west-2'
destination_region = 'us-east-1'

def copy_ami(source_ami_id):
    ec2_client = boto3.client('ec2', region_name=destination_region)

    response = ec2_client.describe_images(
        ImageIds=[source_ami_id],
        Owners=[source_account_id]
    )

    source_image = response['Images'][0]

    block_device_mappings = source_image['BlockDeviceMappings']

    # Remove the encrypted flag from snapshots if it exists
    for block_device_mapping in block_device_mappings:
        if 'Ebs' in block_device_mapping:
            del block_device_mapping['Ebs']['Encrypted']

    response = ec2_client.copy_image(
        Name=source_image['Name'],
        Description=source_image['Description'],
        SourceImageId=source_ami_id,
        SourceRegion=source_region,
        Encrypted=False,
        DestinationRegion=destination_region
    )

    destination_ami_id = response['ImageId']

    ec2_client.modify_image_attribute(
        Attribute='launchPermission',
        ImageId=destination_ami_id,
        LaunchPermission={
            'Add': [{'UserId': destination_account_id}]
        }
    )

    return destination_ami_id

# List of AMIs to copy
source_ami_ids = ['ami-xxxxxxxx', 'ami-yyyyyyyy', 'ami-zzzzzzzz']

# Copy AMIs
for source_ami_id in source_ami_ids:
    destination_ami_id = copy_ami(source_ami_id)
    print(f"Successfully copied AMI {source_ami_id} to {destination_ami_id} in the destination account.")
