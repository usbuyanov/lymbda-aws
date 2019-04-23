import boto3

# Region 
region = 'us-east-1'
# Instances ID 
instances = ['i-05b31358f50b1586e']

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)
    print 'started your instances: ' + str(instances)
