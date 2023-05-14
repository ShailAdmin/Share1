import boto3

# Initialize SES client
ses = boto3.client('ses')

def send_email(body):
    # Set sender and recipient
    sender = 'sender@example.com'
    recipient = 'recipient@example.com'
    
    # Set email subject
    subject = 'Script finished execution'
    
    # Create email message
    message = {
        'Subject': {
            'Data': subject
        },
        'Body': {
            'Text': {
                'Data': body
            }
        }
    }
    
    # Send email
    response = ses.send_email(
        Source=sender,
        Destination={
            'ToAddresses': [recipient]
        },
        Message=message
    )
    
    # Print success message
    print(f"Email sent to {recipient}. Message ID: {response['MessageId']}")

if __name__ == '__main__':
    # Your script goes here
    print("Hello, world!")
    
    # Call send_email function with print output as body
    send_email(body='Hello, world!')
