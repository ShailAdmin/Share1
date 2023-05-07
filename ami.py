import boto3

# Set up client for EC2 service
ec2 = boto3.client('ec2', region_name='us-west-2')  # Change to the source region

# Create the AMI
response = ec2.create_image(InstanceId='i-0123456789abcdef0', Name='My server AMI')

# Get the ID of the new AMI
ami_id = response['ImageId']

# Set up client for the EC2 Copy Image service
ec2_client = boto3.client('ec2', region_name='us-east-1')  # Change to the destination region

# Copy the AMI to the destination region
response = ec2_client.copy_image(
    Name='My server AMI', 
    SourceImageId=ami_id, 
    SourceRegion='us-west-2'
)

# Get the ID of the new AMI in the destination region
copied_ami_id = response['ImageId']

# Print the IDs of the original and copied AMIs
print(f"Original AMI ID: {ami_id}")
print(f"Copied AMI ID: {copied_ami_id}")
