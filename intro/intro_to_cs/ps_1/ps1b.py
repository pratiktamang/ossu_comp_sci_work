"""
    Part B: Saving, with a raise
    Background 

    In Part A, we unrealistically assumed that your salary didn’t change.  But you are an MIT graduate, and
    clearly you are going to be worth more to your company over time! So we are going to build on your
    solution to Part A by factoring in a raise every six months. 

    In ps1b.py, copy your solution to Part A (as we are going to reuse much of that machinery).

    Modify your program to include the following
        1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)
        2. After the 6th month, increase your salary by that percentage.  Do the same after the 12th month, the 18  month, and so on. 
 
    Write a program to calculate how many months it will take you save up enough money for a down
    payment.  LIke before, assume that your investments earn a return of r = 0.04 (or 4%) and the
    required down payment percentage is 0.25 (or 25%).  Have the user enter the following variables:

        1. The starting annual salary (annual_salary)
        2. The percentage of salary to be saved (portion_saved)
        3. The cost of your dream home (total_cost)
        4. The semi­annual salary raise (semi_annual_raise)

"""

import unittest

def calculate_months_to_save(annual_salary, portion_saved, total_cost, semi_annual_raise):
    current_savings = 0
    r = 0.04 # Annual return rate of 4%
    portion_down_payment = 0.25 * total_cost # 25%

    months = 0
    while current_savings < portion_down_payment:
        if months != 0 and months % 6 == 0: 
            annual_salary += annual_salary * semi_annual_raise

        monthly_portion_saved = (annual_salary /12) * portion_saved
        additional_savings = current_savings * r / 12
        current_savings += monthly_portion_saved + additional_savings

        months += 1

    return months 

class TestCalculateMonthsToSave(unittest.TestCase):
    """
        Test Case 1 
        >>>  
        Enter your starting annual salary: 120000
        Enter the percent of your salary to save, as a decimal: .05
        Enter the cost of your dream home: 500000
        Enter the semi­annual raise, as a decimal: .03
        Number of months: 142 
        >>>
        Test Case 2 
        >>>  
        Enter your starting annual salary: 80000
        Enter the percent of your salary to save, as a decimal: .1
        Enter the cost of your dream home: 800000
        Enter the semi­annual raise, as a decimal: .03
        Number of months: 159 
        >>>
        Test Case 3 
        >>>  
        Enter your starting annual salary: 75000
        Enter the percent of your salary to save, as a decimal: .05
        Enter the cost of your dream home: 1500000
        Enter the semi­annual raise, as a decimal: .05
        Number of months: 261 
        >>>
    """

    def test_calculate_months_for_case_one(self):
        self.assertEqual(calculate_months_to_save(120000, 0.05, 500000, 0.03), 142)

    def test_calculate_months_for_case_two(self):
        self.assertEqual(calculate_months_to_save(80000, 0.1, 800000, 0.03), 159)

    def test_calculate_months_for_case_three(self):
        self.assertEqual(calculate_months_to_save(75000, 0.05, 1500000, 0.05), 261)


if __name__ == "__main__":
    unittest.main()