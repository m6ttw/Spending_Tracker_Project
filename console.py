from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.tag import Tag
import repositories.tag_repository as tag_repository

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository

merchant_repository.delete_all()
tag_repository.delete_all()
transaction_repository.delete_all()

merchant_1 = Merchant("Asda")
merchant_repository.save(merchant_1)
merchant_2 = Merchant("Vodafone")
merchant_repository.save(merchant_2)
merchant_3 = Merchant("Adidas")
merchant_repository.save(merchant_3)

tag_1 = Tag("Finances")
tag_repository.save(tag_1)
tag_2 = Tag("Groceries")
tag_repository.save(tag_2)
tag_3 = Tag("Shopping")
tag_repository.save(tag_3)

transaction_1 = Transaction(50, merchant_1, tag_2)
transaction_repository.save(transaction_1)
transaction_2 = Transaction(65, merchant_3, tag_3)
transaction_repository.save(transaction_2)
transaction_3 = Transaction(20, merchant_2, tag_1)
transaction_repository.save(transaction_3)


merchant_repository.select_all()
tag_repository.select_all()
transaction_repository.select_all()


merchant_1.name = "Tesco"
merchant_repository.update(merchant_1)

tag_1.category = "Bills"
tag_repository.update(tag_1)


