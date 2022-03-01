# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 20:41:08 2022
Project 1 - Income Tax Calculator
@author: Nelissa Viera
"""
standard_deduction = 10000
additional_deduction = 3000

gross_income = float(input("Enter the gross income: "))
dependents = int(input("Enter the number of dependents: "))

income_tax = (gross_income - standard_deduction - dependents*(additional_deduction)) *0.20
print(f'The income tax is ${income_tax:.1f}')
