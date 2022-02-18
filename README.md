# Oystercard Challenge

## Motivation
This project was originally completed using [Ruby](https://github.com/marcusventin/oystercard2). I have repeated it in Python to gain experience with the language.  

The project enables a user to simulate an Oystercard system to pay for and log journeys on public transport. It is intended to satisfy the following user stories:  

> In order to use public transport,  
> As a customer,  
> I want money on my card.  

> In order to keep using public transport,  
> As a customer,  
> I want to add money to my card.  

> In order to protect my money,  
> As a customer,  
> I don't want to put too much money on my card.  

> In order to pay for my journey,  
> As a customer,  
> I need my fare deducted from my card.  

> In order to get through the barriers,  
> As a customer,  
> I need to touch in and out.  

> In order to pay for my journey,  
> As a customer,  
> I need to have the minimum amount for a single journey.  

> In order to pay for my journey,  
> As a customer,  
> I need to pay for my journey when it's complete.  

> In order to pay for my journey,  
> As a customer,  
> I need to know where I've travelled from.  

> In order to know where I have been,  
> As a customer,  
> I want to see to all my previous trips.

> In order to know how far I have travelled,  
> As a customer,  
> I want to know what zone a station is in.  

> In order to be charged correctly,  
> As a customer,  
> I need a penalty charge deducted if I fail to touch in or out.  

> In order to be charged the correct amount,  
> As a customer,  
> I need to have the correct fare calculated.  


## How to Use
#### Set-Up
1. Fork this repository and clone it to your machine.
2. Run `pipenv --python 3.10` to create a new project using Python 3.10.  
3. Run `pipenv shell` to create a virtual environment.  
4. Run `python -m pytest tests` to ensure the program is running correctly - the tests should all pass.  