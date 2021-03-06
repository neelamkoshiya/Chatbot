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

We will first work to create the backend of the application. We are leveraging lambda to orchestrate the flow and pull the customer data from dynamo DB table. We are leveraging SNS for customer notification

#### 1) Dynamo DB - Customer Table
Login into your AWS account. Please ensure you perform the lab in us-east-1 region(Virginia) only and the lab is case sensitive so ensure the case is correct for the name of the table and chat bot intent. In the search bar of the console, type Dynamodb.

Click "create table"
![Alt Text](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-25%20at%204.07.31%20PM.png)
Type in the name of the table Customer and key as AccountID. Click on the create table button. 
![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-25%20at%204.07.50%20PM.png)
Once the table is created, click "create item". In the left drop down, select "Text" and copy the payload from here. Now click "Save". 
![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-25%20at%204.09.23%20PM.png)

![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-25%20at%204.09.38%20PM.png)

You should see an entry for the customer with AccountID 1234.

```
{
  "AccountID": "1234",
  "BillAmount": "200",
  "BillDueDate": "3/5/2020",
  "CustomerCategory": "Residential",
  "CustomerName": "John Doe",
  "InternetCharge": "100",
  "PaymentMethod": "My Preferred Credit Card",
  "PreviousBalance": "0",
  "SubscriptionID": "XXX-ee4e-4806-XXX-63b101XXX",
  "SystemID": "S123",
  "SystemLastRebooted": "02/25/2020, 18:03:14",
  "TaxandFee": "50",
  "TelevisionCharge": "50",
  "TotalBalanceAmount": "200"
}
```

#### 2) Lambda function creation
In the search bar of the console, type Lambda

 Create a new Lambda function. Name it "CustomerChatBot" and select the run time as python 3.7. In the IAM role option, you can select create a new role. 
 ![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.38.50%20AM.png)
 
Once function is created, scroll down to tha role and ensure the function has right to write/read DynamoDB and access to SNS to send out notification.
![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-25%20at%204.15.46%20PM.png)
Open the role and click attach policy and attach role for DynamoDB and SNS

![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-25%20at%204.16.09%20PM.png)

You can copy the code [CustomerChatBot.py](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Lambda/CustomerChatBot.py)

Ensure you change the memory and timeout settings
![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.46.20%20AM.png)

The lambda function will act as the logic layer and orchestrator for the chatbot. It will interact with Lex, SNS and Dynamo DB in this example. However in the real world, it would interact/invoke  multiple APIs in order to fulfill the business requirement and functionality.

#### 3) SNS topic creation
In the search bar of the console, type SNS
![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-25%20at%204.12.46%20PM.png)
Create a new topic. Name it CustomerPaymentNotification, keep all default and hit "Create". Once the topic is created note down the topic ARN.
![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-25%20at%204.13.17%20PM.png)

Go to Lambda fucntion and Create environmental variable - SNS_TOPIC and copy the ARN which you had copied.
![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-25%20at%204.13.39%20PM%201.png)
![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%208.42.51%20AM.png)

Scroll down below the topic for subscription and add subscriber with your phone number 

![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-25%20at%204.13.49%20PM.png)

![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-25%20at%204.14.07%20PM%202.png)


#### 4) Testing the Lambda function.
At the top right corner of the lambda function, you will notice a test button. Click on it. We will be running 3 test case with three different inputs which is invoked later in chatbot. 

Click on configure test, paste the test data as in 1) and create test case. Then in the lambda function select that test case from the drop down and run the test. Repeat it for 2) and 3) mentioned below.

![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%203.07.34%20PM.png)

![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%203.07.21%20PM.png)

1) Reboot test data : [reboot test data] (https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/reboot-test-data.json)

2) Customer bill inquiry: [Bill inquiry data](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/BillInquiry.json)

3) Customer payment : [bill payment test data](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/billpayment.json)

There are two workshops:

## "Reboot my system" Chatbot
[Reboot my system](https://github.com/neelamkoshiya/Chatbot/tree/master/RebootSystem)

## "Pay my bill" Chatbot
[Customer Bill](https://github.com/neelamkoshiya/Chatbot/blob/master/PayMyBillChatBot)

