# pip install psycopg2
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
password = os.getenv('password')

def create_table():
    try:
        connection = psycopg2.connect(
            database='postgres',
            user='postgres',
            password=password,
            host='127.0.0.1',
            port=5432
        )
        cursor = connection.cursor()

        query = '''
        create table if not exists logs (
            id serial primary key,
            text varchar(100),
            status varchar(20),
            date_create timestamp)
        '''
        cursor.execute(query)
        connection.commit()
        print("Соединение выполнено успешно!")
    except:
        print("Ошибка!")
    finally:
        connection.close()
        print("Соединение завершено!")


def request_query(text, status, date_create):
    if status in ('Активна', "Редактирована"):
        try:
            connection = psycopg2.connect(
                database='postgres',
                user='postgres',
                password=password,
                host='127.0.0.1',
                port=5432
            )
            cursor = connection.cursor()

            query = '''
                insert into logs (text, status, date_create) values (%s, %s, %s)
            '''
            cursor.execute(query, (text, status, date_create))
            connection.commit()
            print("Соединение выполнено успешно!")
        except:
            print("Ошибка!")
        finally:
            connection.close()
            print("Соединение завершено!")
    else:
        try:
            connection = psycopg2.connect(
                database='postgres',
                user='postgres',
                password=password,
                host='127.0.0.1',
                port=5432
            )
            cursor = connection.cursor()

            query = '''
                update logs set status = 'Удалена' where text = 'text'
            '''
            cursor.execute(query)
            connection.commit()
            print("Соединение выполнено успешно!")
        except:
            print("Ошибка!")
        finally:

            connection.close()
            print("Соединение завершено!")


def get_active_notes():
    try:
        connection = psycopg2.connect(
            database='postgres',
            user='postgres',
            password=password,
            host='127.0.0.1',
            port=5432
        )
        cursor = connection.cursor()

        query = '''
            select text from public.logs
            where status != 'Удалена'
            order by date_create desc
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        print("Соединение выполнено успешно!")
    except:
        print("Ошибка!")
    finally:
        connection.close()
        print("Соединение завершено!")
    return result