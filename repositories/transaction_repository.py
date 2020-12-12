from db.run_sql import run_sql
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

def save(transaction):
    sql = "INSERT INTO transactions (description, amount, merchant_id, tag_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [transaction.description, transaction.amount, transaction.merchant.id, transaction.tag.id]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction


def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        transaction = Transaction(row['description'], row['amount'], row['merchant_id'], row['tag_id'], row['id'] )
        transactions.append(transaction)
    return transactions

def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        transaction = Transaction(result['description'], result['amount'], result['merchant_id'], result['tag_id'], result['id'] )
    return transaction


def merchant(transaction):
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [transaction.merchant.id]
    results = run_sql(sql, values)[0]
    merchant = Merchant(results['name'], results['id'])
    return merchant

def tag(transaction):
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [transaction.tag.id]
    results = run_sql(sql, values)[0]
    tag = Tag(results['category'], results['id'])
    return tag


def update(transaction):
    sql = "UPDATE transactions SET (description, amount, merchant_id, tag_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [transaction.description, transaction.amount, transaction.merchant.id, transaction.tag.id, transaction.id]
    run_sql(sql, values)
    

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)
