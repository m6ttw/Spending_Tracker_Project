import pdb

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.tag import Tag
import repositories.tag_repository as tag_repository

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository


merchant_repository.delete_all()
tag_repository.delete_all()

merchant_1 = Merchant("Tesco")
merchant_repository.save(merchant_1)

merchant_2 = Merchant("Amazon")
merchant_repository.save(merchant_2)

merchant_3 = Merchant("Adidas")
merchant_repository.save(merchant_3)

tag_1 = Tag("Groceries")
tag_repository.save(tag_1)

tag_2 = Tag("Electronics")
tag_repository.save(tag_2)

tag_3 = Tag("Clothing")
tag_repository.save(tag_3)

tag_4 = Tag("Bills")
tag_repository.save(tag_4)

transaction_1 = Transaction("Bought groceries from Tesco", 50, merchant_1, tag_1)
transaction_repository.save(transaction_1)


pdb.set_trace()
