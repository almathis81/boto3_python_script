import boto3


dynamodb = boto3.resource('dynamodb')  


table = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Cartoon',
            'AttributeType': 'S',
        },
        {
            'AttributeName': 'Year',
            'AttributeType': 'S', 
        }
    ],
    KeySchema=[
        {
            'AttributeName': 'Cartoon',
            'KeyType': 'HASH',
        },
        {
            'AttributeName': 'Year',
            'KeyType': 'RANGE'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    },
    TableName='Cartoons', 
)

print("Table created")