def handler(event, context):
2
            return {
3
        'statusCode': 200,
4
        'headers': {
5
            'Content-Type': 'application/json',
6
            'Access-Control-Allow-Origin': '*'
7
        },
8
        'body':'Hello from Lambda!'
9
        ,
10
        "isBase64Encoded": False
11
    }
