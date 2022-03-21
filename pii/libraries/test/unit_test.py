from unittest import TestCase

from libraries.model.orm import proxy, MySQLDatabase_
from pii import Pii


class MyTestCase(TestCase):
    env = "/.env"

    connected_db_name = Pii.config.get("pii-unittest.mysql.database")
    db = None

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        print("================== start", methodName)

    def setUp(self):
        self.db = MySQLDatabase_(
            self.connected_db_name,
            host=Pii.config.get("pii.mysql.host"),
            port=3306,
            user=Pii.config.get("pii.mysql.username"),
            password=Pii.config.get("pii.mysql.password"),
            thread_safe=True,
        )

        proxy.initialize(self.db)

        print(f"unittest db:{self.connected_db_name}")

    def tearDown(self) -> None:
        print("================== end")
        if self.db:
            self.db.close()
        super().tearDown()
