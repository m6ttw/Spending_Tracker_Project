class Transaction():

    def __init__(self, amount, merchant, tag, time_created, id=None):
        self.amount = amount
        self.merchant = merchant
        self.tag = tag
        self.time_created = time_created
        self.id = id
