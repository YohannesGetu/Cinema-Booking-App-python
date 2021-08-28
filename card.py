import sqlite3


class Card:
    """Represents a bank card needed to finalize a Seat purchase
    """

    database = "banking.db"

    def __init__(self, card_type, number, cvc, holder):
        self.type = card_type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self, price):
        """Checks if card id valid and has balance.
        Subtracts price from balance.
        """

        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "balance" FROM "Card" WHERE "number"=? and "cvc"=?
        """, [self.number, self.cvc])
        result = cursor.fetchall()

        if result:
            balance = result[0][0]
            if balance >= price:
                cursor.execute("""
                UPDATE "Card" SET "balance"=? WHERE "number"=? and "cvc"=?
                """, [balance - price, self.number, self.cvc])
                connection.commit()
                connection.close()
                return True