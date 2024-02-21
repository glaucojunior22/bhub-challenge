import boto3

sqs = boto3.client('sqs')


def send_sqs_message(name, message):
    queue_name = f'bhub-{name}'
    try:
        result = sqs.get_queue_url(QueueName=queue_name)
    except sqs.exceptions.QueueDoesNotExist:
        result = sqs.create_queue(QueueName=queue_name)
    return sqs.send_message(QueueUrl=result['QueueUrl'], MessageBody=message)
