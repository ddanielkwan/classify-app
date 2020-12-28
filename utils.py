import boto3
def get_session():
    return boto3.Session(aws_access_key_id="xxx", aws_secret_access_key= "xxx")

def get_polly_client():
    session = get_session()
    return session.client('polly', 'ca-central-1')


