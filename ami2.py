# Create the AMI in the source region
response = ec2.create_image(
    InstanceId='i-0123456789abcdefg',
    Name='My server image',
    Description='An AMI for my server',
    NoReboot=True
)
ami_id = response['ImageId']

print(f"Created AMI {ami_id} in {source_region}")

# Copy the AMI to the destination region
ec2_src = boto3.client('ec2', region_name=source_region)
ec2_dest = boto3.client('ec2', region_name=dest_region)

response = ec2_src.describe_images(ImageIds=[ami_id])
src_image = response['Images'][0]
src_name = src_image['Name']

response = ec2_dest.copy_image(
    Name=src_name,
    Description='Copy of ' + src_name,
    SourceImageId=ami_id,
    SourceRegion=source_region
)
dest_ami_id = response['ImageId']

print(f"Copied AMI {ami_id} from {source_region} to {dest_region}, new AMI ID: {dest_ami_id}")
