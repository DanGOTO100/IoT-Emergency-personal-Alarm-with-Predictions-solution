import boto3
import datetime

#Lambda funcion to check if the alarm is active in DynameDB and if so, call the relatives designated phone
#to be used inside an Step Function loop, right after the initial lambda that called the designated phone of the person who clicked the button


dynamodb = boto3.resource('dynamodb', region_name='your region', endpoint_url="your endpoint")
client = boto3.client('connect')

#Get devide and date/time
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
hour = now.strftime("%H:%M")
deviceid = "your device id"


def lambda_handler(event, context):

    table = dynamodb.Table('your table name')
    
    try:
        response = table.get_item(
            Key={
                'deviceid': deviceid,
                'time': date
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']
        CallActive = item['CallActive']
    print("Call Active indicator: ", CallActive)

    
    #If call is still active after 1 minute in StepFunction
    #we need to call relatives
    
    if CallActive ==  'Y':
        response = client.start_outbound_voice_contact(
            DestinationPhoneNumber='relatives desginated phone number',
            ContactFlowId='Amazon Connect flow id',
            InstanceId='Amazon Connect instance id',
            SourcePhoneNumber='Amazon Connect Source Number',
        )
        
    #let's get out, call was not active OR
    #if it was active we called the relatives and retry the workflow
    
    return 'We checked and called relatives when alarm was ON applicable'

