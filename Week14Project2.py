import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Cartoons') 

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'Cartoon': 'Smurfs',
            'Year': '1981'
            }
        )
    batch.put_item(
        Item={
            'Cartoon': 'Snorks',
            'Year': '1984'
            }
        )
    batch.put_item(
        Item={
             'Cartoon': 'CareBears',
            'Year': '1985'
            }
        )
    batch.put_item(
        Item={
             'Cartoon': 'Jem',
            'Year': '1985'
            }
        )
    batch.put_item(
        Item={
            'Cartoon': 'ThunderCats',
            'Year': '1985'
            }
        )
    batch.put_item(
        Item={
             'Cartoon': 'DuckTales',
            'Year': '1987'
            }
        )
    batch.put_item(
        Item={
            'Cartoon': 'Rugrats',
            'Year': '1990'
            }
        )
    batch.put_item(
        Item={
             'Cartoon': 'Doug',
            'Year': '1991'
            }
        )
    batch.put_item(
        Item={
             'Cartoon': 'Anamaniacs',
            'Year': '1993'
            }
        )
    batch.put_item(
        Item={
             'Cartoon': 'Gargoyles',
            'Year': '1994'
                        }
        )
       
    print("Items_Successfully_Added") 