import psycopg2

db_info={
    'host': 'localhost',
    'port': 5432,
    'database':'cristiano',
    'user':'postgres',
    'password':'abdulaziz09'
}

@staticmethod
def get_all_user():
    try:
        with psycopg2.connect(**db_info) as conn:
            with conn.cursor() as cur:
                query='''select * from person'''
                cur.execute(query)
    except psycopg2.Error as e:
        print(e)


@staticmethod

def get_person_by_id(person_id):
    with psycopg2.connect(**db_info) as conn:
        with conn.cursor() as cur:
            query = '''select * from person where id = %s'''
            data=(person_id,)
            cur.execute(query,data)
            return cur.fetchone()
print(get_person_by_id(1))


