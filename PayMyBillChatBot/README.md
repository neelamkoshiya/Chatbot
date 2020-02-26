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
