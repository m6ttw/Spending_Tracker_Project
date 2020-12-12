from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (category) VALUES (%s) RETURNING id"
    values = [tag.category]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id


def select_all():
    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)
    for result in results:
        tag = Tag(result["category"], result["id"])
        tags.append(tag)
    return tags


def select(id):
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    tag = Tag(result["category"], result["id"])
    return tag


def update(tag):
    sql = "UPDATE tags SET category = %s WHERE id = %s"
    values = [tag.category, tag.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)
