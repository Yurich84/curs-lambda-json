import json
from db_service import DbService

def lambda_handler(event, context):
    items = DbService().get_data('Privat', 'USD')
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': items
    }

if __name__ == '__main__':
    lambda_handler(None, None)
