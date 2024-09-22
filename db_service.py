import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime

class DbService:
    def __init__(self):
        self.create_resource()

    time = datetime.now()

    def get_data(self, bank_name: str, currency: str):
        now = datetime.now()
        start_of_month = int(datetime(now.year, now.month, 1).timestamp())

        response = self.table.scan(
            FilterExpression=
            Key('timestamp').gte(start_of_month) & 
            Key('bank').eq(bank_name) & 
            Key('currency').eq(currency)
        )

        return response['Items']

    def create_resource(self):
        table_name ="curs-lambda"
        self.dynamodb = boto3.resource("dynamodb" )
        self.table = self.dynamodb.Table(table_name)