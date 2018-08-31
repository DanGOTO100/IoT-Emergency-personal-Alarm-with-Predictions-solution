# IoTAlarmsystem
A Easy to use IoT Alarm system using AWS IoT button and some services like Lambda, Connect, Step Functions,etc..

After clicking the AWS IoT button, a series of events will take place to get people the assistance they need.
Basically:

Once someone clicks the AWS IoT button, an ”alarm” state is set and actions will begin. 
First, we will call the designated phone and request to press “1” to deactivate the alarm (in case it was  clicked the button by mistake).
If it was not a mistake –  there is not answer or does not press “1”- then something is wrong bwe will call the relatives of the person who clicked the button or other designated phone to inform them ofthe situation. 

