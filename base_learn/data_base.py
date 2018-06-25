#-*-coding:utf-8-*-
import mysql.connector

def mysql_test():
    print('----start----')
    conn = mysql.connector.connect(host='172.20.11.71',
                                   user='root',
                                   password='root',
                                   port=3306,
                                   database='test',
                                   use_unicode=True)
    cursor = conn.cursor()
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Kebi'])
    cursor.rowcount
    conn.commit()
    cursor.close()
    print('----create mysql database success----')


def insert_mysql():
    conn = mysql.connector.connect(host='172.20.11.71', user='root', password='root', port=3306, database='test',use_unicode=True)
    cursor = conn.cursor()
    cursor.execute('insert into user (id, name) values (%s, %s)', ['3', 'Jamse'])
    cursor.rowcount
    conn.commit()
    cursor.close()
    print('----insert success----')


def select_mysql():
    conn = mysql.connector.connect(host='172.20.11.71',user='root', password='root',port=3306, database='test', use_unicode=True)
    cursor = conn.cursor()
    cursor.execute('select * from user where id = %s', ('2',))
    values = cursor.fetchall()
    print(values)
    print('----select success----')

if __name__ == '__main__':
    select_mysql()
    # insert_mysql()
    # mysql_test()
