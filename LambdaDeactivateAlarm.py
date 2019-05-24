#Lambda to be called from inside connect call flow if the person pressed "1" after being called in the inital 
#call to the designated phone


import boto3
import datetime



dynamodb = boto3.resource('dynamodb', region_name='your region', endpoint_url="your endpoint")

#Get devide and date/time
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
hour = now.strftime("%H:%M")
deviceid = "your device id"


def lambda_handler(event, context):

    table = dynamodb.Table('your table name')
    deviceid = "your device id"
    response = table.update_item(
        Key={
            'deviceid': deviceid,
            'time': date
             },
        UpdateExpression="set CallActive = :c",
        ExpressionAttributeValues={
            ':c': "N"
            },
        ReturnValues="UPDATED_NEW"
    )
    resultMap = {"Estado":"Alarm deactivated for: ","deviceid": deviceid};
    print("Update Item succeeded:")
    return resultMap;
    
