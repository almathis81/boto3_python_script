# Delete a DynamoDB table!

import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.delete_table(
    TableName="Cartoons",
)

print("Table Successfully Deleted")
