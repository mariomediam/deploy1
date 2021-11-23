from django.db import connection
from collections import namedtuple

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def select_trabajador(field, valor_buscado):
    with connection.cursor() as cursor:
        cursor.execute('EXEC SIAM.dbo.SelectTrabajador %s, %s', [field, valor_buscado])
        return dictfetchall(cursor)        