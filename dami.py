import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    # Get all AMIs
    response = ec2.describe_images(Owners=['self'])

    # Loop through all AMIs
    for ami in response['Images']:
        
        # Check if name ends with "ami"
        if ami['Name'].endswith('ami'):
            
            # Get AMI ID
            ami_id = ami['ImageId']
            
            # Deregister AMI
            ec2.deregister_image(ImageId=ami_id)
            
            # Print success message
            print(f"AMI {ami_id} deleted.")
    
    # Return response
    return {
        'statusCode': 200,
        'body': "All AMIs with name ending in 'ami' have been deleted."
    }
