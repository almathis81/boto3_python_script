#!/usr/bin/env python3.7 # Create a Standard SQS Queue using Python and Boto3

import boto3 # This imports the boto3 library and enables interaction with AWS services

sqs = boto3.resource('sqs') # This creates the SQS client using the Boto3 library

queue = sqs.create_queue( # This sets the SQS Queue variable
    QueueName='Wk15_SQS_lambda' # This is the name of the SQS Queue
)

print('SQS Queue Successfully Created')
print(queue.url)