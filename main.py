from card import Card
from seat import Seat
from user import User

name = input("Your full name: ")
seat_id = input("Preferred seat number: ")
card_type = input("Your card type: ")
card_number = input("Your card number: ")
card_cvc = input("Your card cvc: ")
card_holder = input("Card holder name: ")

user = User(name=name)
seat = Seat(seat_id=seat_id)
card = Card(card_type=card_type, number=card_number, cvc=card_cvc, holder=card_holder)

print(user.buy(seat=seat, card=card))
