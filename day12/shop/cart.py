# from payment import process_payment


from .payment import process_payment 
from shop.payment import process_payment
def checkout(total):
    message=process_payment(total)
    print(message)

