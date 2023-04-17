import boto3

# Create a Boto3 client for the AWS resource
resource_client = boto3.client('resourcegroupstaggingapi')

# Get a list of all the AWS regions
aws_regions = [region['RegionName'] for region in boto3.client('ec2').describe_regions()['Regions']]

# Initialize an empty list to store the AWS resources
aws_resources = []

# Iterate through each region
for region in aws_regions:

    # Create a Boto3 client for the region
    client = boto3.client('ec2', region_name=region)

    # Get a list of all the EC2 instances in the region
    ec2_instances = client.describe_instances()['Reservations']

    # Add the EC2 instances to the list of AWS resources
    aws_resources.extend(ec2_instances)

    # Get a list of all the S3 buckets in the region
    s3_buckets = client.list_buckets()['Buckets']

    # Add the S3 buckets to the list of AWS resources
    aws_resources.extend(s3_buckets)

# Print the list of AWS resources
print(aws_resources)


aws configservice get-aggregate-discovered-resources --resource-type AWS::AllSupported --region us-east-1

