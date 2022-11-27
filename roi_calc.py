

class Monopoly():
    
    def __init__(self):
        self.housesinfo = {}
        self.income_total = 0
        self.expenses_total = 0
        self.cash_flow_total = 0
        self.cash_on_cash_total = 0

    def incomes(self):
        self.property_name = input("What is the name for the property?\n")
        self.housesinfo[self.property_name] = {}

        rent = input("Does the property charge more than one rent? (i.e. duplex)?\n")
        if rent.lower().strip() in ('yes', 'y'):
            rental_income = input("How much rent is charged for the total of all units?\n")
            self.income_total += float(rental_income)
            self.housesinfo[self.property_name] = {"Rental income": float(rental_income)}
        else:
            rental_income2 = input("How much do you charge for rent?\n")
            self.income_total += float(rental_income2)
            self.housesinfo[self.property_name] = {"Rental income": float(rental_income2)}

        laundry = input("Does the property charge for laundry?\n")
        if laundry.lower().strip() in ('yes', 'y'):
            laundry_income = input("How much do you charge per month?\n")
            self.income_total += float(laundry_income)
            self.housesinfo[self.property_name]["Laundry Income"] = float(laundry_income)
        else:
            self.housesinfo[self.property_name]["Laundry Income"] = 0

        storage = input("Does the property charge for storage?\n")
        if storage.lower().strip() in ('yes', 'y'):
            storage_income = input("How much do you charge?\n")
            self.income_total += float(storage_income)
            self.housesinfo[self.property_name]["Storage Income"] = float(storage_income)
        else:
            self.housesinfo[self.property_name]["Storage Income"] = 0

        misc = (input("Does the property have any miscellaneous charges?\n"))
        if misc.lower().strip() in ('yes', 'y'):
            misc_income = input("How much do you charge per month?\n")
            self.income_total += float(misc_income)
            self.housesinfo[self.property_name]["Misc Income"] = float(misc_income)
        else:
            self.housesinfo[self.property_name]["Misc Income"] = 0

        now_income_total = input("Do you want to see your total income for this property?\n")
        if now_income_total.lower().strip() in ('yes', 'y'):
            print(self.income_total)
        else:
            print("You can view this information later within your house collections.")

    def expenses(self):
        tax_question = input("Do you pay any tax for this property?\n")
        if tax_question.lower().strip() in ('yes', 'y'):
            taxes = input("How much tax do you pay per calendar month?\n")
            self.housesinfo[self.property_name]["Taxes"] = float(taxes)
            self.expenses_total += float(taxes)
        else:
            self.housesinfo[self.property_name]["Taxes"] = 0

        lawn_question = input("Does this property require lawn care?\n")
        if lawn_question.lower().strip() in ('yes', 'y'):
            lawn = input("How much does the lawn service cost?\n")
            self.housesinfo[self.property_name]["Lawn Services"] = float(lawn)
            self.expenses_total += float(lawn)
        else:
            self.housesinfo[self.property_name]["Lawn Services"] = 0
        
        vacancy_question = input("Do you want to set aside money for vacancy?\n")
        if vacancy_question.lower().strip() in ('yes', 'y'):
            vacancy_coverage = input("How much would you like to put away to cover when the property is vacant?\n")
            self.housesinfo[self.property_name]["Vacancy"] = float(vacancy_coverage)
            self.expenses_total += float(vacancy_coverage)
        else:
            self.housesinfo[self.property_name]["Vacancy"] = 0

        repair_question = input("Do you want to set aside money for emergency repairs?\n")
        if repair_question.lower().strip() in ('yes', 'y'):
            repair = input("How much do you want to set aside?\n")
            self.housesinfo[self.property_name]["Repair Fund"] = float(repair)
            self.expenses_total += float(repair)
        else:
            self.housesinfo[self.property_name]["Repair Fund"] = 0

        capital_expen_question = input("Do you want to set aside money for future home improvements and repairs?\n")
        if capital_expen_question.lower().strip() in ('yes', 'y'):
            capital_expenditure = input("How much do you want to set aside?\n")
            self.housesinfo[self.property_name]["Capital Expenditure"] = float(capital_expenditure)
            self.expenses_total += float(capital_expenditure)
        else:
            self.housesinfo[self.property_name]["Capital Expenditure"] = 0

        property_man_question = input("(Will you) Are you paying someone to manage the property?\n")
        if property_man_question.lower().strip() in ('yes', 'y'):
            property_management = input("How much will this cost?\n")
            self.housesinfo[self.property_name]["Property Management"] = float(property_management)
            self.expenses_total += float(property_management)
        else:
            self.housesinfo[self.property_name]["Property Management"] = 0

        mortgage_question = input("(Will) Did this property require a mortgage?\n")
        if mortgage_question.lower().strip() in ('yes', 'y'):
            mortgage = input("How much is the monthly mortgage payment?\n")
            self.housesinfo[self.property_name]["Mortgage"] = float(mortgage)
            self.expenses_total += float(mortgage)
        else:
            self.housesinfo[self.property_name]["Mortgage"] = 0
        
        now_expense_total = input("Do you want to see your expenses total?\n")
        if now_expense_total.lower().strip() in ('yes', 'y'):
            print(self.expenses_total)
        else:
            print("You can view this information later within your house collections.")
    
    def cash_flow_(self):
        cash_flow = self.income_total - self.expenses_total
        self.cash_flow_total += cash_flow
        self.housesinfo[self.property_name]["Cash Flow"] = float(cash_flow)
        print(f'The cash flow for this property is (will be) {cash_flow}.')
        
    
    def cash_on_cash(self):
        dp_question = input("(Will) Did you put any money down?\n")
        if dp_question.lower().strip() in ('yes', 'y'):
            deposit = input("How much of a down payment (will) did you make?\n")
            self.housesinfo[self.property_name]["Down Payment"] = float(deposit)
            self.cash_on_cash_total += float(deposit)
        else:
            self.housesinfo[self.property_name]["Down Payment"] = 0

        closing_question = input("(Will) Did you pay closing costs?\n")
        if closing_question.lower().strip() in ('yes', 'y'):
            closing = input("How much (will) did you pay in closing costs?\n")
            self.housesinfo[self.property_name]["Closing Costs"] = float(closing)
            self.cash_on_cash_total += float(closing)
        else:
            self.housesinfo[self.property_name]["Closing Costs"] = 0

        rehab_question = input("(Will) Did you pay for any rehab?\n")
        if rehab_question.lower().strip() in ('yes', 'y'):
            rehab = input("How much (will) did you pay for rehab?\n")
            self.housesinfo[self.property_name]["Rehab Costs"] = float(rehab)
            self.cash_on_cash_total += float(rehab)
        else:
            self.housesinfo[self.property_name]["Rehab Costs"] = 0
        
        misc_question = input("(Will) Do you have any other expenses?\n")
        if misc_question.lower().strip() in ('yes', 'y'):
            misc = input("How much (will) did this cost?\n")
            self.housesinfo[self.property_name]["Misc Charges"] = float(misc)
            self.cash_on_cash_total += float(misc)
        else:
            self.housesinfo[self.property_name]["Misc Charges"] = 0

        now_cash_roi = input("Do you want to see your total investment?\n")
        if now_cash_roi.lower().strip() in ('yes', 'y'):
            print(self.cash_on_cash_total)
        else:
            print("You can view this information later within your house collections.")

    def roi(self):
        annual_cash_flow = self.cash_flow_total * 12
        total_investment = self.cash_on_cash_total
        roi = annual_cash_flow / total_investment
        roi_percentage = roi * 100
        self.housesinfo[self.property_name]["ROI"] = float(roi_percentage)
        print(f'Your ROI (Return on Investment) for {self.property_name} is {roi_percentage}%.\n')

    def houses(self):
        password = input("To see all your property information please enter your password. \n")

        if password.lower().strip() == 'cash money millionaire':
            
            print("""
            Inventory Options
            [1] See Properties
            [3] Exit""")

            while True:
                
                access_info = input("\nWhich properties would you like to view? \n")

                if access_info == '1':
                    print(f'These are your prospective properties {self.housesinfo}')
                elif access_info == '2':
                    print(f'These are the properties you own: {self.owned_properties}')
                elif access_info == '3':
                   break
                else:
                    print("That is not a valid option. Please try again.")

        else:
            print("You do not have permission to access this information or you have entered your password incorrectly.")
        print("Have a wonderful day.")
        exit()

    def quit(self):
        print("Thank you for using TM calculators.")
        exit()


#------------------        control flow        ------------------------

class Main():

    def instructions():
        print("""

        The following ROI (return on investment) calculator will provide you the necessary information
        to determine if your investment in a certain property is finanical viable or not. 

        You will need to enter information in four sections to return your ROI percentage. The four
        sections are: 

            [1]. Income

            [2]. Expenses

            [3]. Cash flow

            [4]. Cash on Cash ROI

        Each section will gather various amounts of information from you. Please note that the ROI 
        returned is a calculation of the information you provided. The more accurate the information 
        and the more information you can provide, the closer to a realized ROI the calculation will 
        be. 

        Further, the ROI provided by this calculator is not a guarantee and should not be treated as
        such - your ROI can change based upon many factors that are not controllable by this app. 
        Always consult an investment advisor before making any investment, as the information provided
        to you by this calculator is just a calculation and does not constitute as investment advice.

        Thank you for choosing TM calculators.   

        Please select the from the following options:

        [1] Show instructinos
        [2] Incomes
        [3] Expenses
        [4] Cash Flow
        [5] Cash on Cash ROI
        [6] ROI
        [7] Houses
        [8] Exit

        """)

    def run():
        Main.instructions()
        top_hat = Monopoly()
        going_past_go = True
            
        while going_past_go:

            prompt_screen = input("What option would you like to choose from above?\n")

            if prompt_screen.strip() == '1':
                Main.instructions()

            elif prompt_screen.strip() == '2':
                top_hat.incomes()

            elif prompt_screen.strip() == '3':
                top_hat.expenses()

            elif prompt_screen.strip() == '4': 
                top_hat.cash_flow_()

            elif prompt_screen.strip() == '5':
                top_hat.cash_on_cash()

            elif prompt_screen.strip() == '6':
                top_hat.roi()

            elif prompt_screen.strip() == '7':
                top_hat.houses()

            elif prompt_screen.strip() == '8':
                top_hat.quit()

            else:
                print("That's not a valid option. Please try again.")
                

Main.run()
                



