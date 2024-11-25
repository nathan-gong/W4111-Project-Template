import pymysql
from sqlalchemy import create_engine


def get_connection(
        user="root", pw="dbuserdbuser", host="localhost",
        port=3306, autocommit=True, cursorclass=pymysql.cursors.DictCursor
):
    conn = pymysql.connect(
        user=user, password=pw, host=host,
        port=port, autocommit=autocommit, cursorclass=cursorclass
    )

    return conn


def get_engine(url="mysql+pymysql://root:dbuserdbuser@localhost"):
    engine = create_engine(url)
    return engine


def run_sql(sql, args=None, fetch=True):

    con = None

    try:
        con = get_connection()
        cur = con.cursor()
        res = cur.execute(sql, args)
        if fetch:
            res = cur.fetchall()
    except Exception as e:
        if con:
            con.close()
        res = None

    return res





