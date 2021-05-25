import lithops
from ibm_botocore.client import Config, ClientError
import ibm_boto3

from config import lithops_config

"""
def hello_world(name):
    return 'Hello {}!'.format(name)

if __name__ == '__main__':
    fexec = lithops.FunctionExecutor(config=lithops_config.config)
    fexec.call_async(hello_world, 'World')
    fexec.call_async(hello_world, '1')
    fexec.call_async(hello_world, '2')
    print(fexec.get_result())
"""

# Constants for IBM COS values
COS_ENDPOINT = lithops_config.config['ibm_cos']['endpoint_url'] # Current list avaiable at https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints
COS_API_KEY_ID = lithops_config.config['ibm_cos']['api_key'] # eg "W00YixxxxxxxxxxMB-odB-2ySfTrFBIQQWanc--P3byk"
COS_INSTANCE_CRN = lithops_config.config['ibm_cos']['resource_instance_id'] # eg "crn:v1:bluemix:public:cloud-object-storage:global:a/3bf0d9003xxxxxxxxxx1c3e97696b71c:d6f04d83-6c4f-4a62-a165-696756d63903::"

# Create resource
cos = ibm_boto3.resource("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_INSTANCE_CRN,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)


def upload_object(bucket_name):
  cos.Bucket(bucket_name).upload_file('README.md', 'README.md')
  

if __name__ == '__main__':
  upload_object('urv.sd.task2')