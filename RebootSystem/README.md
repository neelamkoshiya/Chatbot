The business case that we intent to solve with this chatbot for the customers to reboot their system remotely by self serving themselves. 

### Reboot System Chatbot

#### 1) Create Custom Bot
Login to your AWS console and search for "Lex"
Once you are on the landing page, click get started. 
![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.12.55%20AM.png)

Then select custom bot, provide a name and configurations as follows:

![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.16.41%20AM.png)

![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.17.02%20AM.png)


#### 2) Create an intent
Once the bot is created, create an intent "RebootSystem"

![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.17.43%20AM.png)

![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.17.51%20AM.png)

![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.18.01%20AM.png)
#### 3) Create Utterances

Type in following utterances - type one in text field and then click "+" to add more
![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.25.36%20AM.png)
```
reboot
```
```
restart
```
```
my system does not seems to work. I want to restart my system
```
```
I want to restart my system
```
```
I want to reboot my system
```

After entering all the utterances, lets do to next step

![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.28.55%20AM.png)

#### 4) Create slots
![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.31.53%20AM.png)

![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.32.01%20AM.png)

Create first slot for AccountID as following save and add it
![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.32.35%20AM.png)

In the slot, add in the question
![alt](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.35.11%20AM.png)
```
AccountID
```
```
What is your account number?
```

similarly create another slot for Acknowledgement
```
Acknowledgement
```
```
Do you agree with the terms and condition and permit us to restart your system on your behalf?
```

![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%207.06.22%20AM.png)

#### 5) Fulfillment 

For the fulfillment, we will select Lambda and select our lambda function in the drop down
![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.49.24%20AM.png)

We will grant access for Lex to invoke the Lambda function
![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.49.31%20AM.png)

#### 6) Build and test

Now save the intent at the bottom and click build at the top of the page
![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.49.48%20AM.png)

Once the build is complete you can open the test window on the right side and test using utterance you had configured

![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.51.58%20AM.png)

![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%206.53.31%20AM.png)

#### 7) Validation

You can check the Customer table to see if the "SystemLastRebooted" is updated to latest time

![](https://github.com/neelamkoshiya/Chatbot/blob/master/Artifacts/Images/Screen%20Shot%202020-02-26%20at%207.13.44%20AM.png)
