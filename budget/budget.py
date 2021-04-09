
class Budget(object):
    def __init__(self, categories):
        self.categories = dict()

        if type(categories) is list or type(categories) is tuple:
            for category in categories:
                if type(category) is not str:
                    raise TypeError('Category must be a valid string')
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
