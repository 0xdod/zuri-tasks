
class Budget(object):
    def __init__(self, category_list):
        self.categories = dict()

        if type(category_list) is list or type(category_list) is tuple:
            self.list_category = category_list
            for category in category_list:
                if type(category) is not str:
                    raise TypeError('Category must be a valid string')
                category = category.lower()
                self.categories[category] = 0
        else:
            raise TypeError('Categories should be a list or tuple')

    def deposit(self, category, amount):
        if self._is_valid_category(category):
            self.categories[category] += amount
            print('Deposit of N%d successful.' % amount)

    def withdraw(self, category, amount):
        if self._is_valid_category(category):
            if self.categories[category] >= amount:
                self.categories[category] -= amount
                print('Withdrawal of N%d successful.' % amount)
            else:
                print('Insufficient funds.')

    def balance(self, category):
        if self._is_valid_category(category):
            return self.categories[category]

    def print_balance(self, category):
        bal = self.balance(category)
        print('Your balance is N%d' % bal)

    def _is_valid_category(self, category):
        category = category.lower()
        if category not in self.categories:
            raise LookupError('Category %s does not exist.' % category)

        return True

    def transfer(self, from_category, to_category, amount):
        if self._is_valid_category(to_category) and self._is_valid_category(from_category):
            if self.categories[from_category] >= amount:
                self.categories[to_category] += amount
                self.categories[from_category] -= amount
                message = f'You have successfully transferred N{amount} from {from_category} to {to_category}'
            else:
                message = 'Insufficient funds.'
            print(message)

    def display_categories(self):
        msg = '\n'
        for i in range(len(self.list_category)):
            msg += f'{i+1}\t{self.list_category[i]}\n'
        print(msg)

    def category_from_list_index(self, index):
        return self.list_category[index-1]

    def select_category(self, *args, **kwargs):
        msg = kwargs.get('message', '')
        print('Select category')
        self.display_categories()
        category_index = int(input(msg))
        return self.category_from_list_index(category_index)


asteriks = '*' * 20


def main():
    print(f'{asteriks}BUDGET APP{asteriks}')
    print('Create a new budget.')
    categories = []
    msg = '\nEnter new category for budget, Press # to end.\n'
    inp = input(msg)
    while inp and inp != '#':
        categories.append(inp)
        inp = input(msg)

    bud = Budget(categories)
    print(f'{asteriks}Budget created successfully{asteriks}')
    ans = 'y'
    while ans == 'y':
        run_operation(bud)
        ans = input(
            'Do you want to perform another operation?[y/n]\nPress y to continue, any other key to quit ')
        ans = ans.lower()
    print('Goodbye')


def run_operation(bud):
    inp = int(input('''\nWhat would you like to do ?

Press 1 for Deposit
Press 2 for Withdrawal
Press 3 for Balance
Press 4 for Transfer to other category\n
'''))

    if inp == 1:
        print(asteriks*3)
        print('Deposit')
        category = bud.select_category()
        amount = float(input('\nHow much would you like to deposit ?\n'))
        bud.deposit(category, amount)
    elif inp == 2:
        print(asteriks*3)
        category = bud.select_category()
        amount = float(input('\nHow much would you like to withdraw ?\n'))
        bud.withdraw(category, amount)
    elif inp == 3:
        print(asteriks*3)
        category = bud.select_category()
        bud.print_balance(category)
    elif inp == 4:
        print(asteriks*3)
        from_category = bud.select_category(message='Transfer from:\n')
        to_category = bud.select_category(message='Transfer to:\n')
        amount = float(input('How much do you want to transer?\n'))
        bud.transfer(from_category, to_category, amount)
    else:
        print('Invalid selection, please try again.')


if __name__ == '__main__':
    main()
