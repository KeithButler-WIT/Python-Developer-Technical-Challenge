#!/usr/bin/env python3

import os
import json
import boto3
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_ddb_connection():
    ENV = os.environ['Environment']
    ddbclient=''
    if ENV == 'local':
        ddbclient = boto3.client('dynamodb', endpoint_url='http://dynamodb:8000/')
    else:
        ddbclient = boto3.client('dynamodb')
    return ddbclient

def lambda_handler(event, context):
    ddbclient = get_ddb_connection()
    try:
        response = ddbclient.batch_write_item(
        RequestItems={
            os.environ['DDBTableName']: [
                {
                    'PutRequest': {
                        'Item': {
                            'documentId': {'N': '0'},
                            'make': {'S': 'Nissan'},
                            'model': {'S': 'Micra'},
                            'year': {'N': '2004'},
                            'chassis_no': {'S': '12345A'},
                            'id': {'N': '1'},
                            'last_updated': {'S': '2017-02-01 00:00:00'},
                            'price': {'N': '500.0'},
                        }
                    }
                },
                {
                    'PutRequest': {
                        'Item': {
                            'documentId': {'N': '1'},
                            'make': {'S': 'Nissan'},
                            'model': {'S': 'Micra'},
                            'year': {'N': '2004'},
                            'chassis_no': {'S': '12425A'},
                            'id': {'N': '1'},
                            'last_updated': {'S': '2017-03-01 00:00:00'},
                            'price': {'N': '400.0'},
                        }
                    }
                },
                {
                    'PutRequest': {
                        'Item': {
                            'documentId': {'N': '2'},
                            'make': {'S': 'Ford'},
                            'model': {'S': 'Fiesta'},
                            'year': {'N': '2002'},
                            'chassis_no': {'S': '12345B'},
                            'id': {'N': '1'},
                            'last_updated': {'S': '2017-03-01 00:00:00'},
                            'price': {'N': '300.0'},
                        }
                    }
                },
                {
                    'PutRequest': {
                        'Item': {
                            'documentId': {'N': '3'},
                            'make': {'S': 'Audi'},
                            'model': {'S': 'A3'},
                            'year': {'N': ''},
                            'chassis_no': {'S': '12345C'},
                            'id': {'N': '3'},
                            'last_updated': {'S': '2017-04-01 00:00:00'},
                            'price': {'N': ''},
                        }
                    }
                },
                {
                    'PutRequest': {
                        'Item': {
                            'documentId': {'N': '4'},
                            'make': {'S': 'Nissan'},
                            'model': {'S': 'Micra'},
                            'year': {'N': '2004'},
                            'chassis_no': {'S': '12345D'},
                            'id': {'N': '4'},
                            'last_updated': {'S': '2017-05-01 00:00:00'},
                            'price': {'N': '200.0'},
                        }
                    }
                },
                {
                    'PutRequest': {
                        'Item': {
                            'documentId': {'N': '5'},
                            'make': {'S': 'Peugeot'},
                            'model': {'S': '308'},
                            'year': {'N': '1998'},
                            'chassis_no': {'S': '12345E'},
                            'id': {'N': '5'},
                            'last_updated': {'S': '2017-06-01 00:00:00'},
                            'price': {'N': '100.0'},
                        }
                    }
                },
            ]}
        )

        return {
            'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
            'body': json.dumps({
                'message': 'Filled DynamoDB',
            }),
        }

    except ddbclient.exceptions.ResourceNotFoundException as e:
        logging.error('Cannot do operations on a non-existent table')
        raise e
    except ClientError as e:
        logging.error('Unexpected error')
        raise e
