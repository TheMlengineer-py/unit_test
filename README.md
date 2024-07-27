# unit_test
# Adthena Data Engineer Technical Assignment
Project: Shopping Basket Pricing
Overview
This project involves creating a Python program that calculates the price of a basket of goods, taking into account some special offers. The program will be driven by unit tests and will provide a command-line interface for input.

Requirements
Language: Python
Duration: Estimated 4 to 6 hours, submit within 1 week
Submission: GitHub or BitBucket repository
Review Focus: Code structure, domain modeling, unit tests
Documentation: Clear instructions on how to install and run the code locally
Problem Statement
Write a program that prices a basket of goods with special offers:

Goods and Prices:
Soup: 65p per tin
Bread: 80p per loaf
Milk: £1.30 per bottle
Apples: £1.00 per bag
Special Offers:
Apples: 10% discount this week
Buy 2 tins of soup and get a loaf of bread for half price
The program should accept a list of items in the basket and output the subtotal, the special offer discounts, and the final price.

Input should be via the command line in the form PriceBasket item1 item2 item3 ...

For example:

Copy code
PriceBasket Apples Milk Bread
Output should be to the console, for example:

yaml
Copy code
Subtotal: £3.10
Apples 10% off: 10p
Total price: £3.00
If no special offers are applicable, the code should output:

yaml
Copy code
Subtotal: £1.30
(No offers available)
Total price: £1.30
