"""
####################################
#####Upload one file to AWS S3 #####
####################################

import boto3
import os
from dotenv import load_dotenv
import mimetypes

load_dotenv()
# # Make sure env.py runs first
# if os.path.isfile('env.py'):
#     import env  # noqa: F401

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
print("Bucket name:", AWS_STORAGE_BUCKET_NAME)
def upload_to_s3(file_path, bucket_name):

    s3= boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,

    )
    file_name = os.path.basename(file_path)
    content_type = mimetypes.guess_type(file_path)[0]

    if content_type is None:
 
        content_type = 'application/octet-stream'
        # content_type='/media2/'

    with open(file_path, 'rb') as file:
        s3.upload_fileobj(file, bucket_name, file_name, ExtraArgs={'ContentType': content_type})
        print('Going well till here 11111111111111')    

    bucket_location = s3.get_bucket_location(Bucket=bucket_name)
    region = bucket_location['LocationConstraint'] if bucket_location['LocationConstraint'] else 'eu-north-1'
    file_url = f"https://{bucket_name}.s3.{region}.amazonaws.com/{file_name.replace(' ','+' )}"

    # https://dealna-de-v1-3-bucket.s3.eu-north-1.amazonaws.com/un2050_logo_v1.4_bg.png
    return file_url

def main():

    file_path = 'loqta2050_v6.png' # same level of this file 
    file_url = upload_to_s3(file_path, AWS_STORAGE_BUCKET_NAME)
    print(f"File uploaded successfully. Access it at: {file_url}")

if __name__== '__main__':
    main()
 """

####################################
#####Upload Folder/*.* to AWS S3 ###
####################################

import boto3
import os
import mimetypes
# from dotenv import load_dotenv
# load_dotenv()

# Make sure env.py runs first
if os.path.isfile('env.py'):
    import env  # noqa: F401

 

 

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
print("Bucket name:", AWS_STORAGE_BUCKET_NAME)

def upload_to_s3(file_path, bucket_name, s3_folder=""):
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    # Preserve folder structure in S3
    if s3_folder:
        s3_key = os.path.join(s3_folder, os.path.relpath(file_path, s3_folder))
    else:
        s3_key = file_path

    file_name = os.path.basename(file_path)
    content_type = mimetypes.guess_type(file_path)[0] or 'application/octet-stream'

    with open(file_path, 'rb') as file:
        s3.upload_fileobj(file, bucket_name, s3_key, ExtraArgs={'ContentType': content_type})
        print(f"Uploaded: {file_path} -> {s3_key}")

    bucket_location = s3.get_bucket_location(Bucket=bucket_name)
    region = bucket_location['LocationConstraint'] or 'eu-north-1'
    file_url = f"https://{bucket_name}.s3.{region}.amazonaws.com/{s3_key.replace(' ','+')}"
    return file_url

def upload_folder(folder_path, bucket_name):
    uploaded_files = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            local_path = os.path.join(root, filename)
            # s3_key is relative to the folder_path
            relative_path = os.path.relpath(local_path, folder_path)
            uploaded_files.append(upload_to_s3(local_path, bucket_name, folder_path))
    return uploaded_files

def main():
    folder_path = 'media'  # folder to upload
    uploaded_files = upload_folder(folder_path, AWS_STORAGE_BUCKET_NAME)
    print("\nAll files uploaded:")
    for f in uploaded_files:
        print(f)

if __name__ == '__main__':
    main()
