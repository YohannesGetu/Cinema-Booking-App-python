from ticket import Ticket


class User:
    """Represents a user that can buy a cinema Seat
    """

    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        """Buys the ticket if the card is valid
        """
        if seat.is_free():
            if card.validate(price=seat.get_price()):
                seat.occupy()
                ticket = Ticket(user=self, price=seat.get_price(), seat_number=seat.seat_id)
                ticket.to_pdf()
                return "Purchase successful!"
            else:
                return "There was a problem with you card!"
        else:
            return "Seat is taken!"