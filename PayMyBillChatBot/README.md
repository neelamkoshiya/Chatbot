We are going to build the "Pay My Bill" Chat Bot functionality. I have split it up into two functionality
1) Bill Inquiry - This will help answer customer's query about their bill and provide visibility to them


2) Bill Payment - This will help with the payment process

## Bill Inquiry


#### 1) Create Custom Bot
Open the AWS console and search for Amazon Lex. Create a custom Bot. Name it "CustomerBill"
![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%207.28.36%20AM.png)

#### 2) Create Intent

Under left side, you can see "Intent", click on the "+" button and add an intent. Add the name of the intent as "BillInquiry"

#### 3) Add Utterances

Under the utterances add the following questions:
```
how much do I owe
Explain my bill
What is my bill breakdown
What is due amount
```

![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%207.35.06%20AM.png)

#### 4) Add the Slot
For the slot, we will be using AccountID(which we created in previous lab) from the drop down and add the question "what is your account id"

![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%207.37.56%20AM.png)

#### 5) Fulfillment
For the response and backend processing we will be referring to the same lambda function

![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%207.45.54%20AM.png)

There will be prompt for providing access to Lex to invoke Lambda , click yes.

#### 6) Build and test

Save the intent at the bottom of the screen and click on the build button

![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%207.48.50%20AM.png)

For testing, open the test window on the right side and type in the utterance 

![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%207.55.16%20AM.png)

You can add more data to customer table and validate if the response is inline with the data in customer table

### Bill Payment
Lets see the steps for adding another intent for bill payment. 

#### 1) Add Intent

Add the intent by clicking on "+" on the left side besides Intent
Create an intent "billpayment"
![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%208.00.03%20AM.png)

#### 2) Add utterance
Add the possible utterances 
```
pay my bill
payment help
bill payment
Please help me pay my bill
I want to pay my bill
```

![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%208.05.27%20AM.png)

#### 3) Add Slots
For this use case, we would be reusing the existing slots for AccountID and Acknowledgement. We will be creating two new slot : PaymentMethod and PaymentAmount

First lets add AccountID and pick the slot from drop down and have the question : "What is your account ID"

Then we add slot for payment method. You can specify the value like "boa" or "credit card" as sample value. Add slot.

![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%208.10.58%20AM.png)

Once the slot is created and added, change the name as PaymentMethod and add question "What payment method would you like to use"
![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%208.11.27%20AM.png)

Then we add slot for payment amount. You can specify the value like 100 as sample value. Add slot.
![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%208.14.38%20AM.png)

Once the slot is created and added, change the name as PaymentMethod and add question 
"What is the payment amount?"
![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%208.18.27%20AM.png)

Final slot would be acknowledgement of the customer that they agree with the terms and condition and they authorize this payment. Add the slot "Acknowledgement" and question "Do you agree with our terms and condition and authorize this payment"

![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%208.19.07%20AM.png)


#### 4) Fulfillment
For the backend and response, we would be using the lambda function. Under the fulfillment, select Lambda and pick CustomerChatBot lambda from the drop down
![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%208.22.39%20AM.png)

#### 5) Build and test
Save the intent at the bottom of the screen. Then click build on the top right. It might take few minutes to build. Once the build is completed, we can begin testing on the right side "Test Chatbot" window. Type in "pay my bill" and answer the questions along
![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%208.26.22%20AM.png)

In real world, you would call the bill payment api and post the payment. However, in this example, we are integrating it with SNS, which notifies the bill is paid. Check you cell phone for the SMS!

![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/IMG_9441.jpg)




