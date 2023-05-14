import boto3
ecr_client = boto3.client(
    'ecr',
    region_name='eu-north-1',
    aws_access_key_id='',
    aws_secret_access_key='',
)

repository_name = "my_personal_page_app_image"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response ['repository']['repositoryUri']
print(repository_uri)