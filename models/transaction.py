class Transaction():

    def __init__(self, amount, merchant, tag, id=None, time_created=None):
        self.amount = amount
        self.merchant = merchant
        self.tag = tag
        self.id = id
        self.time_created = time_created
