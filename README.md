# Chatbot
Build Chatbot with Amazon Lex

Do you ever wonder how you would build a chatbot? Chatbot are conversational interface which can be accessed via text or speech. 
Below workshop highlights how you can have a chatbot for two usecases :

1) Pay my Bill
2) Reboot my system

We are assuming the system is a telecommincation device at customer's household or business which controls the service delivery like internet and television. On the other hand, "pay my bill" is more generic functionality. However since payment involves PCI complaince, we are assuming the pci data is handled in a different system and while performing the action for pay my bill, the customer is essentially providing "already saved" payment method. Just trying to keep it simple and decouple that part from this chatbot.

Well, without further ado, lets begin.

## Architecture Flow

Here is the architecture diagram:
![Arch diagram](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/CharterWorkshop-arch.jpg)

### About the AWS services used

Amazon Lex is a service for building conversational interfaces into any application using voice and text. Amazon Lex provides the advanced deep learning functionalities of automatic speech recognition (ASR) for converting speech to text, and natural language understanding (NLU) to recognize the intent of the text, to enable you to build applications with highly engaging user experiences and lifelike conversational interactions. 

AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume.

Amazon DynamoDB is a key-value and document database that delivers single-digit millisecond performance at any scale. It's a fully managed, multiregion, multimaster, durable database with built-in security, backup and restore, and in-memory caching for internet-scale applications. 

Amazon Simple Notification Service (SNS) is a highly available, durable, secure, fully managed pub/sub messaging service that enables you to decouple microservices, distributed systems, and serverless applications.

## Pre-requisite

#### 1) Dynamo DB - Customer Table
Login into your AWS account.In the search bar of the console, type Dynamodb.

Click "create table"

Type in the name of the table Customer and key as AccountID. Click on the create table button. 

Once the table is created, click "create item". In the left drop down, select "Text" and copy the payload from here. Now click "Save". 

You should see an entry for the customer with AccountID 1234.

#### 2) Lambda function creation
In the search bar of the console, type Lambda

 Create a new Lambda function. Name it "CustomerChatBot" and select the run time as python 3.7
Once function is created, ensure the function has right to write/read DynamoDB and access to SNS to send out notification.

The lambda function will act as the logic layer and orchestrator for the chatbot. It will interact with Lex, SNS and Dynamo DB in this example. However in the real world, it would interact/invoke  multiple APIs in order to fulfill the business requirement and functionality.

#### 3) SNS topic creation
In the search bar of the console, type SNS
Create a new topic. Name it CustomerPaymentNotification, keep all default and hit "Create". Once the topic is created note down the topic ARN.

Go to Lambda fucntion and Create environmental variable - SNS_TOPIC and copy the ARN which you had copied.


## "Pay my bill" Chatbot

## "Reboot my system" Chatbot

