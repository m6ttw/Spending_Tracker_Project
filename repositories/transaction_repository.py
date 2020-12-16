from db.run_sql import run_sql
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

def save(transaction):
    sql = "INSERT INTO transactions (amount, merchant_id, tag_id) VALUES (%s, %s, %s) RETURNING id"
    values = [transaction.amount, transaction.merchant.id, transaction.tag.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    transaction.id = id

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for result in results:
        amount = float(result["amount"])
        merchant = merchant_repository.select(result["merchant_id"])
        tag = tag_repository.select(result["tag_id"])
        transaction = Transaction(amount, merchant, tag, result["id"], result["time_created"])
        transactions.append(transaction)
        transactions.reverse()
    return transactions


def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        transaction = Transaction(result["amount"], result["merchant_id"], result["tag_id"], result["id"], result["time_created"])
    return transaction


def update(transaction):
    sql = "UPDATE transactions SET (amount, merchant_id, tag_id) = (%s, %s, %s) WHERE id = %s"
    values = [transaction.amount, transaction.merchant.id, transaction.tag.id, transaction.id, transaction.time_created]
    run_sql(sql, values)


def total():
    sql = "SELECT SUM(amount) FROM transactions"
    total = run_sql(sql)
    for amounts in total:
        for amount in amounts:
            return amount


def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)
