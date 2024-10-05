from db_service import DbService

BANK_MONO = 'Mono'
BANK_PRIVAT = 'Privat'

CURRENCY_EUR = 'EUR'
CURRENCY_USD = 'USD'

def lambda_handler(event, context):
    bank = event['queryStringParameters']['bank']
    currency = event['queryStringParameters']['currency']

    validation_error = validate_parameters(bank, currency)
    if validation_error:
        return validation_error

    items = DbService().get_data(bank, currency)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': items
    }

def validate_parameters(bank, currency):
    if not bank or not currency:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': 'Missing bank or currency'
        }
    
    if bank not in [BANK_MONO, BANK_PRIVAT]:
        return {
            'statusCode': 422,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': 'Not supported bank'
        }
    
    if currency not in [CURRENCY_USD, CURRENCY_EUR]:
        return {
            'statusCode': 422,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': 'Not supported currency'
        }
    
    return None

if __name__ == '__main__':
    event = { 'queryStringParameters': { 'bank': 'Privat', 'currency': 'USD' } }
    lambda_handler(event, None)
