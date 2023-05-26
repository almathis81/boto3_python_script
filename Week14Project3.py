import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Cartoons')

# retrieves all items in the table and yields a dictionary of those items
response = table.scan() 

items = response['Items'] # stores the items variable

# This is a 'for' loop that iterates over items
for item in items:
    print(item)
    
print("Successful Table Scan")