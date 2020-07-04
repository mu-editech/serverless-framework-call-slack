import json
import requests
import boto3

ssm = boto3.client("ssm", region_name="ap-northeast-1")

def get_ssm_params(ssm_parameter_key):
    param_dict = ssm.get_parameter(Name=ssm_parameter_key)
    return param_dict.get('Parameter').get('Value')


def post_message(url, message):
    """Post a message to slack using a webhook url."""
    data = {'text': message}
    response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    return response.status_code


def hello(event, context):
    return post_message(
        url=get_ssm_params('Slack-WebHook'),
        message='This is test message from AWS Lambda and serverless-framework'
    )