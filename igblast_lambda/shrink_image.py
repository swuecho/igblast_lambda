from __future__ import print_function
import boto3
import os
import sys
import uuid
import zipfile
     
s3_client = boto3.client('s3')
     
def resize_image(image_path, resized_path):
    print(image_path)
    cmd = './igblastn -germline_db_V database/human_gl_V -germline_db_J database/human_gl_J -germline_db_D database/human_gl_D -organism human -domain_system imgt -query {} -auxiliary_data optional_file/human_gl.aux -show_translation -outfmt 3 -out {}'.format(image_path, resized_path)
    os.system(cmd)
    # TODO: make zip file work
    #with zipfile.ZipFile(resized_path + '.zip', 'w') as myzip:
    #    myzip.write(resized_path) 

def handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key'] 
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        upload_path = '/tmp/resized-{}'.format(key)
        
        s3_client.download_file(bucket, key, download_path)
        resize_image(download_path, upload_path)
        s3_client.upload_file(upload_path, '{}resized'.format(bucket), key)
