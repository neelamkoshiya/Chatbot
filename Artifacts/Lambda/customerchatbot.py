"""
This sample demonstrates an implementation of the Lex Code Hook Interface
in order to serve a sample bot which manages orders for flowers.
Bot, Intent, and Slot models which are compatible with this sample can be found in the Lex Console
as part of the 'OrderFlowers' template.

For instructions on how to set up and test this bot, as well as additional samples,
visit the Lex Getting Started documentation http://docs.aws.amazon.com/lex/latest/dg/getting-started.html.
"""
import math
import dateutil.parser
import datetime
import time
import os
import logging
import boto3
import decimal
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


""" --- Helpers to build responses which match the structure of the necessary dialog actions --- """


def get_slots(intent_request):
    return intent_request['currentIntent']['slots']


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': message
        }
    }


def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }

    return response


def delegate(session_attributes, slots):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }


""" --- Helper Functions --- """


def parse_int(n):
    try:
        return int(n)
    except ValueError:
        return float('nan')


def build_validation_result(is_valid, violated_slot, message_content):
    if message_content is None:
        return {
            "isValid": is_valid,
            "violatedSlot": violated_slot,
        }

    return {
        'isValid': is_valid,
        'violatedSlot': violated_slot,
        'message': {'contentType': 'PlainText', 'content': message_content}
    }


def isvalid_date(date):
    try:
        dateutil.parser.parse(date)
        return True
    except ValueError:
        return False







""" --- Functions that control the bot's behavior --- """



def billinquiry(intent_request):
   
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('CustomerBill')
    AccountID=get_slots(intent_request)["AccountID"]
   

    responsedb = table.query(
        KeyConditionExpression=Key('AccountID').eq(AccountID)
    )
    customerresponse=""
   
    for i in responsedb['Items']:
        customerresponse="The Bill amount for last month is "+ i['BillAmount']+". The Break down is as follows: InternetCharge is "+ i['InternetCharge']+" Television Charges is "+i['TelevisionCharge']+" Taxes and Fees is "+ i['TaxandFee'] + " Previous Balance Amount is "+i['PreviousBalance']+". Total balance amount is "+i['TotalBalanceAmount']+". The due date for payment is "+i['BillDueDate']
    return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': customerresponse})

def billpayment(intent_request):
   
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('CustomerBill')
    AccountID=get_slots(intent_request)["AccountID"]
    PaymentMethod=get_slots(intent_request)["PaymentMethod"]
    PaymentAmount=get_slots(intent_request)["PaymentAmount"]
    Acknowledgement=get_slots(intent_request)["Acknowledgement"]
   #You can call your payment api here
   
    client = boto3.client('sns')
    client.publish(
        TopicArn = os.environ['SNS_TOPIC'],
        Subject='Bill payment',
        Message = 'Dear Customer, Your payment has been successfully processed'
    )
    customerresponse="Your payment is submitted. You shall receive a notification once it is completed. Thank you!"
    
    return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': customerresponse})
                  
def rebootsystem(intent_request):
   
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('CustomerBill')
    AccountID=get_slots(intent_request)["AccountID"]
    Acknowledgement=get_slots(intent_request)["Acknowledgement"]
    #You can call your reboot api here


    now = datetime.now() 
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print("date and time:",date_time)
    
    response = table.update_item(
        Key={
            'AccountID': AccountID
           
        },
        UpdateExpression="set SystemLastRebooted = :r",
        ExpressionAttributeValues={
            ':r': date_time
           
        },
        ReturnValues="UPDATED_NEW"
    )
  
    customerresponse="Your system has been successfully rebooted. Please can you try. Thank you!"
    
    return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': customerresponse})



def default_answer(intent_request):
    """
    Performs dialog management and fulfillment for ordering flowers.
    Beyond fulfillment, the implementation of this intent demonstrates the use of the elicitSlot dialog action
    in slot validation and re-prompting.
    """

    #product_type = get_slots(intent_request)["ProductStyle"]
    #itemid = get_slots(intent_request)["ItemId"]
    #itemid='5391020'

    return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': 'Sample Response from default answer Lambda function'})



""" --- Intents --- """


def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    logger.debug('dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))

    intent_name = intent_request['currentIntent']['name']

    # Dispatch to your bot's intent handlers
    
    if intent_name == 'BillInquiry':
        return billinquiry(intent_request)
    elif intent_name == 'billpayment': 
        return billpayment(intent_request)
    elif intent_name == 'RebootSystem': 
        return rebootsystem(intent_request)
    else:
        return default_answer(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')


""" --- Main handler --- """


def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    # By default, treat the user request as coming from the America/New_York time zone.
    os.environ['TZ'] = 'America/New_York'
    time.tzset()
    logger.debug('event.bot.name={}'.format(event['bot']['name']))

    return dispatch(event)
