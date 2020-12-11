from db.run_sql import run_sql
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

def save(transaction):
    sql = "INSERT INTO transactions (description, amount, merchant_id, tag_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [transaction.description, transaction.amount, transaction.merchant.id, transaction.tag.id]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction


def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)
