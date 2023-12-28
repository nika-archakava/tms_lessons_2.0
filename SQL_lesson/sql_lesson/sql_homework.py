import sqlite3

from sql_lesson.sql_lesson.random_character import create_random_character

DB_NAME = "my_database.db"
TABLE_NAME = "Gryffindor"

characters = [
    ('Harry', 'Potter', 'Half-blood', 1980),
    ('Ronald', 'Weasley', 'Pure-blood', 1979),
    ('Hermione', 'Granger', 'Muggle-born', 1979),
    ('Neville', 'Longbottom', 'Pure-blood', 1980),
    ('Rubeus', 'Hagrid', 'Half-breed', 1928)
]


def create_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    return connection, cursor


def create_table(connection, cursor):
    cursor.execute(
        f"create table {TABLE_NAME} ("
        "first_name text, "
        "last_name text, "
        "blood_status text, "
        "born int"
        ");"
    )
    connection.commit()


def connect_to_db():
    return create_database()


def write_to_db(connection, cursor, some_data, write_many=True):
    if write_many:
        cursor.executemany(f'insert into {TABLE_NAME} values (?, ?, ?, ?)', some_data)
    else:
        cursor.execute(f'insert into {TABLE_NAME} values (?, ?, ?, ?)', some_data)
    connection.commit()


def assert_availability_in_db(cursor, some_data):
    try:
        result = cursor.execute(f'SELECT * FROM {TABLE_NAME} '
                                f'WHERE first_name = ? AND last_name = ? AND blood_status = ? AND born = ?',
                                some_data).fetchone()
        assert result is not None, 'Волшебник отсутствует в базе!'
    except Exception as e:
        print(f"\nОшибка при выполнении запроса: {e}")


def delete_from_db(connection, cursor, some_data):
    cursor.execute(f'delete from {TABLE_NAME} where first_name = ? AND last_name = ? AND blood_status = ? AND born = ?',
                   some_data)
    connection.commit()


def main():
    connection, cursor = create_database()
    create_table(connection, cursor)
    write_to_db(connection, cursor, characters)


class TestSql:
    def test_find_characters_born_in_1980(self):
        connection, cursor = connect_to_db()
        characters_born_in_1980 = cursor.execute(f"select * from {TABLE_NAME} where born=1980;").fetchall()
        actual_number_of_characters = len(characters_born_in_1980)
        expected_number_of_characters = 2
        assert actual_number_of_characters == expected_number_of_characters, \
            f"Ожидалось {expected_number_of_characters} волшебника, родившихся в 1980 году, но получено {actual_number_of_characters}"

    def test_find_oldest_character(self):
        connection, cursor = connect_to_db()
        actual_oldest_person = cursor.execute(f"select * from {TABLE_NAME} order by born limit 1;").fetchone()
        actual_oldest_person_name = actual_oldest_person[0]
        expected_oldest_person_name = 'Rubeus'
        assert actual_oldest_person_name == expected_oldest_person_name, \
            f"Ожидалось, что самый старший волшебник - {expected_oldest_person_name}, но получено - {actual_oldest_person_name}"

    def test_add_and_delete_random_character(self):
        connection, cursor = connect_to_db()
        new_character = create_random_character()
        write_to_db(connection, cursor, new_character, write_many=False)
        assert_availability_in_db(cursor, new_character)
        delete_from_db(connection, cursor, new_character)
        assert_availability_in_db(cursor, new_character)


if __name__ == "__main__":
    main()
