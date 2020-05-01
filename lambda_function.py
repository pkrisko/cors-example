import json

def lambda_handler(event, context):
    # stageVariables will be passed in request from API Gateway when we configure
    # it as "lambda proxy".
    allowed_origin = event['stageVariables']['allowedOrigin']
    return {
        'headers': {
            "Access-Control-Allow-Origin": allowed_origin,
            "Access-Control-Allow-Methods": "GET,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
            "Content-Type":"application/json"
        },
        'statusCode': 200,
        'body': json.dumps('COORS > CORS')
    }
