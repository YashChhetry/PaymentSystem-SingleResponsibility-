# SOLID Principles Payment System with Interactive Menu

class PaymentGateway:
    def process_payment(self, amount, payment_info):
        pass

class CreditCardPaymentGateway(PaymentGateway):
    def process_payment(self, amount, credit_card):
        print(f"Processing credit card payment of ${amount} using card ending in {credit_card.card_number[-4:]}")

class PayPalPaymentGateway(PaymentGateway):
    def process_payment(self, amount, paypal_account):
        print(f"Processing PayPal payment of ${amount} using account {paypal_account.email}")

class PaymentProcessor:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def process_payment(self, amount, payment_info):
        self.payment_gateway.process_payment(amount, payment_info)

class PaymentInfo:
    pass

class CreditCardInfo(PaymentInfo):
    def __init__(self, card_number, expiration_date, cvv):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

class PayPalInfo(PaymentInfo):
    def __init__(self, email):
        self.email = email

class DisplayablePayment:
    def display_payment(self, payment_info):
        pass

class CreditCardPayment(DisplayablePayment):
    def display_payment(self, credit_card):
        print(f"Card ending in {credit_card.card_number[-4:]}, Expiry: {credit_card.expiration_date}")

class PayPalPayment(DisplayablePayment):
    def display_payment(self, paypal_account):
        print(f"PayPal account: {paypal_account.email}")

class PaymentApplication:
    def __init__(self, payment_processor, displayable_payment):
        self.payment_processor = payment_processor
        self.displayable_payment = displayable_payment

    def complete_payment(self, amount, payment_info):
        self.payment_processor.process_payment(amount, payment_info)
        self.displayable_payment.display_payment(payment_info)

# Interactive menu
def main():
    while True:
        print("\n=== Payment Menu ===")
        print("1. Pay with Credit Card")
        print("2. Pay with PayPal")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter payment amount: "))
            card_number = input("Enter credit card number: ")
            expiration = input("Enter expiration date (MM/YY): ")
            cvv = input("Enter CVV: ")

            credit_card_info = CreditCardInfo(card_number, expiration, cvv)
            processor = PaymentProcessor(CreditCardPaymentGateway())
            display = CreditCardPayment()
            app = PaymentApplication(processor, display)
            app.complete_payment(amount, credit_card_info)

        elif choice == "2":
            amount = float(input("Enter payment amount: "))
            email = input("Enter PayPal email: ")

            paypal_info = PayPalInfo(email)
            processor = PaymentProcessor(PayPalPaymentGateway())
            display = PayPalPayment()
            app = PaymentApplication(processor, display)
            app.complete_payment(amount, paypal_info)

        elif choice == "3":
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
