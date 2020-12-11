class Transaction():

    def __init__(self, description, amount, merchant, tag, id=None):
        self.description = description
        self.amount = amount
        self.merchant = merchant
        self.tag = tag
        self.id = id