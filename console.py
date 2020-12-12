import pdb

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.tag import Tag
import repositories.tag_repository as tag_repository

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository


merchant_1 = Merchant("Asda")
merchant_repository.save(merchant_1)
merchant_2 = Merchant("Amazon")
merchant_repository.save(merchant_2)
merchant_3 = Merchant("Adidas")
merchant_repository.save(merchant_3)

tag_1 = Tag("Finances")
tag_repository.save(tag_1)
tag_2 = Tag("Charity")
tag_repository.save(tag_2)
tag_3 = Tag("Entertainment")
tag_repository.save(tag_3)
tag_4 = Tag("Groceries")
tag_repository.save(tag_4)
tag_5 = Tag("Misc")
tag_repository.save(tag_5)
tag_6 = Tag("Shopping")
tag_repository.save(tag_6)
tag_7 = Tag("Transport")
tag_repository.save(tag_7)

transaction_1 = Transaction(50, merchant_1, tag_4)
transaction_repository.save(transaction_1)
transaction_2 = Transaction(65, merchant_3, tag_6)
transaction_repository.save(transaction_2)


merchant_repository.select_all()
tag_repository.select_all()
transaction_repository.select_all()


merchant_1.name = "Tesco"
merchant_repository.update(merchant_1)

tag_1.category = "Bills"
tag_repository.update(tag_1)

transaction_1.amount = 40
transaction_repository.update(transaction_1)


merchant_repository.delete_all()
tag_repository.delete_all()
transaction_repository.delete_all()

pdb.set_trace()
