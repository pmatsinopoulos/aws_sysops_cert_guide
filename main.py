import boto3

ec2 = boto3.resource('ec2')
my_instance = ec2.Instance('i-02d2a1b455e163e30')
print(my_instance.image_id)
my_instance.terminate()
