import unittest
import backend.db_connection

class Test_database(unittest.TestCase):
    def setUp(self):
        self.db = backend.db_connection.DBConnect()

    def test_fetch(self):
        query = 'select * from sign_up'
        x = self.db.fetch(query)
        self.assertEqual(('Dilip', 'Basnet', '__basnet.4', '1234567Ab', 9840174208, '4-Jul-2000', 'Male'), x)
        print(x)

    def test_insert(self):
        query = "insert into sign_up(first_name, sur_name, user_name, pass_word, mob_no, d_ob, gen_der) values " \
                "(%s, %s, %s, %s, %s, %s, %s)"
        values = ('Bikash', 'Dumrakoti', 'bikash.01', '1234', 9840939395, '7-Mar-1992', 'Male')
        insertedRow = self.db.insert(query, values)
        if (insertedRow > 0):
            print("Data inserted !")
            self.test_fetch()
        else:
            print("Failed to insert data !")

    def test_nfetch(self):
        query = "select * from sign_up where user_name='bikash.01'"
        x = self.db.fetch(query)
        if (x is not None):
            print("Newly inserted data :", x)
        else:
            print("No record found previously !")

    def test_update(self):
        username = 'bikash.01'
        password = 'hello'
        query = "update sign_up set pass_word=%s where user_name=%s"
        values = (password, username)
        x = self.db.update(query, values)
        self.assertNotEqual(('Bikash', 'Dumrakoti', 'bikash.01', '1234', 9840939395, '7-Mar-1992', 'Male'), x)
        print("password has been updated.", x)

    def test_delete(self):
        username = 'bikash.01'
        query = "delete from sign_up where user_name=%s"
        values = (username,)

        d = self.db.delete(query, values)
        self.assertNotEqual((''), d)
        print("User has been deletd", d)


if __name__ == '__main__':
    obj = Test_database()
