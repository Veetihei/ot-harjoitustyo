import unittest
from repositories.users_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_testaaja = User("testaaja", "salis")
        self.user_kayttaja = User("Kayttaja", "salasana123")

    def test_register_one_new_user(self):

        user_repository.register(self.user_testaaja)
        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_testaaja.username)

    def test_find_all_2_new_users(self):
        user_repository.register(self.user_kayttaja)
        user_repository.register(self.user_testaaja)

        users = user_repository.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_kayttaja.username)
        self.assertEqual(users[1].username, self.user_testaaja.username)
        self.assertEqual(users[0].password, self.user_kayttaja.password)

    def test_find_by_username(self):
        user_repository.register(self.user_kayttaja)
        user_repository.register(self.user_testaaja)

        user = user_repository.find_by_username(self.user_testaaja.username)

        self.assertEqual(user.username, self.user_testaaja.username)
        self.assertEqual(user.password, self.user_testaaja.password)

    def test_delete_all(self):
        user_repository.register(self.user_kayttaja)
        user_repository.register(self.user_testaaja)

        user_repository.delete_all()

        users = user_repository.find_all()

        self.assertEqual(len(users), 0)
