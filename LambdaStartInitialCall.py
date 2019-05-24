import boto3
import datetime
import json
from botocore.vendored import requests

#init boto
client = boto3.client('connect',region_name='your region')
dynamodb = boto3.resource('dynamodb', region_name='your region', endpoint_url="your endpoint")


#Get devide and date/time

now = datetime.datetime.now()
print("time: ",now)
date = now.strftime("%Y-%m-%d")
hour = now.strftime("%H:%M")
deviceid = "your device id"  #It can be extracted from event.serialnumber, if you are using more than 1 device

def lambda_handler(event, context):
    
    # Call designated person because he/she pressed the button. Use Amazon Connect API
    
    response = client.start_outbound_voice_contact(
        DestinationPhoneNumber='designated phone number',
        ContactFlowId='contact flow number',
        InstanceId='Instance ID',
        SourcePhoneNumber='source number in Amazon Connet'
    )

    # Enrich with weather data
    response = requests.get("call a public api to get weather, like for example dark sky")
    data = response.json()
    weatherdata = data['currently']['summary']
    temperdata = int(data['currently']['temperature'])
    
    # Enrich with moon data 
    response = requests.get("call a public api to get moon data, like for example US Navy")
    data = response.json()
    moondata = data['closestphase']['phase']
   
    #Updating DynamoDB Table
    
    table = dynamodb.Table('your table name')
    response = table.put_item(
        Item={
            'deviceid': deviceid,
            'date': date,
            'hour': hour,    
            'CallActive': 'Y',
            'Weather': weatherdata,
            'Temperature': temperdata,
            'MoonPhase': moondata,
        }
        )
   
    
    return 'Call performed, DynamoDB alarm is active.'
