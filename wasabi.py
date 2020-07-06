import boto3
import wasabiconfig as cfg


endpoint = cfg.s3["endpoint_url"]
aws_access_key = cfg.s3["aws_access_key_id"]
aws_secret_key = cfg.s3["aws_secret_access_key"]

s4 = boto3.client('s3',
endpoint_url = endpoint,
aws_access_key_id = aws_access_key,
aws_secret_access_key = aws_secret_key)

# if uploading tar.gz set type to application/gzip
#Upload a file and make it publicly available

def wasabiuploadfile(localfile,remotefile,bucket):
    s4.upload_file(
        localfile, bucket, remotefile,
        ExtraArgs={
            'ACL': 'public-read', 
            'Metadata': 
            {
                'chain': 'waxtestnet',
                'version': '2.0.6'
            
            },
            'ContentType': 'text/plain'
            }
    )

wasabiuploadfile('test.txt','test11.txt','waxtest2')
# Create the latest Snapshot
def createlatest(remotefile,bucket):
    s3 = boto3.resource('s3',
    endpoint_url = endpoint,
    aws_access_key_id = aws_access_key,
    aws_secret_access_key = aws_secret_key)
    s3.Object(bucket,'snapshot-latest').copy_from(CopySource=bucket+"/"+remotefile)

createlatest('test11.txt','waxtest2')

