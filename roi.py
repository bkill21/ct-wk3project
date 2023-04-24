#Purchase price 200,000

#(1) Estimated monthly income:

    # 2000  - rental income

#(2) Estimated monthly expenses: 

    # 150  - property tax 
    # 100  - insurence
    # 0    - utilities (electric,water,sewer,garbage,gas)
    # 0    - HOA
    # 0    - Lawn/snow
    # 100  - vacancy
    # 100  - repairs
    # 100  - capex [savings] (new roof, new carpets, big items)
    # 200  - property management
    # 860* - mortgage biggerpockets.com/calc

    # 1610 - total monthly expenses

#(3) Monthly Cash Flow

    # 2000 - 1610 = 390

# (4) Cash on cash ROI

# 40,000  - down payment
# 3,000   - closing costs
# 7,000   - rehad budget
# 0       - misc other

# 50,000  - total investment

# 4,680   - 390 monthly cash flow x 12 months

# 9.36%   - Annual cash on cash ROI = 4680 annual cash flow / 50,000 total investment


#  biggerpockets.com/analyzerentalproperty
#  biggerpockets.com/analysis

class ROI():

    def __init__(self):
        self.purchase_price = 0
        self.down_payment = 0
        self.closing_costs = 0
        self.rehab_budget = 0
        self.investment_total = 0
        self.income = 0
        self.expenses_dict = {}
        self.expenses_total = 0
        self.cash_flow = 0
        self.coc_roi = 0
    
    def roi_driver(self):
            command_prompt = input('Type a task command to start new property calculations\n[Property Info] [Expenses] [Display Info] [ROI] [Exit]').lower()
            if command_prompt == 'property info':
                self.enter_info()
            elif command_prompt == 'expenses':
                self.collect_expenses_data()
            elif command_prompt == 'display info':
                self.display_info()
            elif command_prompt == 'exit':
                print('Goodbye!')
            else:
                print(f'{command_prompt} is not a valid input. Please try again.')
#Collect basic info on the property           
    def enter_info(self):
        #Accepting inputs for monthly rental income/expenses
        input_command = input('Ok, lets collect some info about your proerty. Select a category:\n[purchase details] [income] [expenses] [back]').lower()
        #Take user input for purchase price in digit form only and set instance variable
        if input_command == 'purchase details':
            self.collect_costs_data()
        #Take user input for expected rental income in digit form only and set instance variable
        elif input_command == 'income': 
            input_income = input('What is your expected monthly income from renting this property?')
            if input_income.isdigit():
                self.income = input_income
            else:
                print(f'{input_income} is not a valid input.')
        #Navigate user to collect data about expense for a dictionary
        elif input_command == 'expenses': 
            self.collect_expenses_data()
        #Return to main task selector            
        elif input_command == 'back': 
            self.roi_driver()
        else:
            print(f'{input_command} is not a valid input. Please try again.')
        self.roi_driver()

    def collect_costs_data(self):
            input_purchase_price = input('How much does does this property cost?')
            if input_purchase_price.isdigit():
                self.purchase_price = input_purchase_price
                self.down_payment =  int(self.purchase_price) * 0.2
                print(f'Purchasing a new property requires 20 percent down payment:\nFor this property that will run you: {self.down_payment}')
            else:
                print(f'{input_purchase_price} is not a valid input.')
            
            input_closing_costs = input('Purchasing a property through an agency will cost you. Total additonal closing costs and enter here:\n')
            if input_closing_costs.isdigit():
                self.closing_costs = input_closing_costs
            else:
                print(f'{input_closing_costs} is not a valid input.')
            input_rehab_budget = input('If you plan to put some money into rehabing this property, total those expenses here or enter 0 if you plan to rent it as is:\n')
            if input_rehab_budget.isdigit():
                self.rehab_budget = input_rehab_budget
            else:
                print(f'{input_rehab_budget} is not a valid input.')
            self.calc_total_investment               

    def collect_expenses_data(self):
        print('Okay let\'s collect some info on monthly expenses...\n')

        input_property_tax = input('What is the monthly property tax payment for this\n')
        if input_property_tax.isdigit():
            self.expenses_dict['property taxes'] = input_property_tax
        else:
            print(f'{input_property_tax} is not a valid input.')

        input_insurence = input('Owner\'s insurence for the property varies. How much is your anticipated monthly owner\'s insurence payemnt?\n')
        if input_insurence.isdigit():
            self.expenses_dict['insurence'] = input_insurence
        else:
            print(f'{input_insurence} is not a valid input.')

        input_utilities = input('How much will monthly utitlities (gas/water/electric) total be? Enter 0 if your tenants will be paying these themselves.\n')
        if input_utilities.isdigit():
            self.expenses_dict['utilities'] = input_utilities
        else:
            print(f'{input_utilities} is not a valid input.')

        input_repairs = input('How much will you set aside monthly for surprise repairs? We recommend at least 100\n')
        if input_repairs.isdigit():
            self.expenses_dict['monthly repairs'] = input_repairs
        else:
            print(f'{input_repairs} is not a valid input.')

        input_management = input('Will you be managing the property yourself? If you are hiring a properry managment agency, enter monthly fee here:\n')
        if input_management.isdigit():
            self.expenses_dict['property management'] = input_management
        else:
            print(f'{input_management} is not a valid input.')

        input_mortgage = input('Mortgage payments vary depending on credit and negotiations with your lender. Enter your monthly mortgage payment here:\n')
        if input_mortgage.isdigit():
            self.expenses_dict['mortgage'] = input_mortgage
        else:
            print(f'{input_mortgage} is not a valid input.')

        self.calc_monthly_expenses()

    #Run calculations and show data/calculations for the property
    def calc_monthly_expenses(self):
        for key in self.expenses_dict:
            self.expenses_total += int(self.expenses_dict[key])
        print(f'Total monthly expenses are: {self.expenses_total}')
        self.calc_monthly_cash_flow
        
    def calc_total_investment(self):
        self.investment_total = self.down_payment + self.closing_costs + self.rehab_budget
        print(f'Your total investment for this property will be {self.investment_total}')
        self.roi_driver() 

    def calc_monthly_cash_flow(self):
        print(self.expenses_dict)
        self.cash_flow = self.income - self.expenses_total
        print(f'Your monthly cash flow was calculated as your anticipated monthly expenses subtracted from your expected monthly income from renting this property:\n{self.income} - {self.expenses_total} = {self.cash_flow}')
        self.roi_driver

    def display_info(self):
        print(f'Total investment:\n{self.investment_total}\n')
        print(f'Total monthly income:\n{self.income}\n')
        print(f'Itemized montly expenses:\n{self.expenses_dict}\n')
        print(f'Total monthly expenses:\n{self.expenses_total}\n')
        print(f'Total monthly cash flow:\n{self.cash_flow}\n')
        go_back = input('Type back to return to main menu\n').lower()
        if go_back == 'back':
            self.roi_driver()
        else:
            print(f'\n{go_back} is not a valid command.')

    def calc_coc_roi(self):
        self.coc_roi = (self.income * 12) / self.investment_total
        print(f'Based on the information you entered your annual cash on cash return on your investment will be {self.coc_roi}% annually.')