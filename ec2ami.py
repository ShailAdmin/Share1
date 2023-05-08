import boto3

# Define the EC2 client
ec2 = boto3.client('ec2')

# List of AMIs to use for instance creation
amis = ['ami-0c55b159cbfafe1f0', 'ami-0d8f6eb4f641ef691', 'ami-02eac2c0129f6376b']

# Loop through the AMIs and create an instance for each one
for ami in amis:
    # Define the instance parameters
    instance_params = {
        'ImageId': ami,
        'InstanceType': 't2.micro',
        'KeyName': 'my-key-pair',
        'SecurityGroupIds': ['sg-0123456789abcdefg'],
        'MinCount': 1,
        'MaxCount': 1
    }

    # Launch the instance
    response = ec2.run_instances(**instance_params)

    # Print the instance ID
    instance_id = response['Instances'][0]['InstanceId']
    print(f'Instance created with ID: {instance_id}')
