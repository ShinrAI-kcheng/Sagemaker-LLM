import boto3, json

def query_endpoint_with_json_payload(encoded_json, endpoint_name, access_key=None, secret_key=None, server_location=None):
    client = boto3.client("runtime.sagemaker")
    if (access_key == None): # Credentials Implied
        response = client.invoke_endpoint(
            EndpointName=endpoint_name, ContentType="application/json", Body=encoded_json
        )
    else: # Credenials Given
        response = client.invoke_endpoint(
            EndpointName=endpoint_name, ContentType="application/json", Body=encoded_json,
            aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=server_location
        )
    return response

def query_endpoint(encoded_text, endpoint_name, access_key=None, secret_key=None, server_location=None):
    client = boto3.client("runtime.sagemaker")
    if (access_key == None): # Credentials Implied
        response = client.invoke_endpoint(
            EndpointName=endpoint_name, ContentType="application/x-text",
            Body=encoded_text
        )
    else: # Credenials Given
        response = client.invoke_endpoint(
            EndpointName=endpoint_name, ContentType="application/x-text",
            Body=encoded_text,
            aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=server_location
        )
    return response