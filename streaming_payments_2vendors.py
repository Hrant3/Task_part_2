

def stream_payments(callback_fn):
    # Simulate streaming payments by calling the callback function with each payment.
    for i in range(10):
        callback_fn(i)  # Simulate a payment with values 0 to 9


# Simulate the store_payments function
def store_payments(amount_iterator):
      # Simulate storing payments by iterating over the payment amounts.
    for amount in amount_iterator:
        print(f"Storing payment: {amount}")  # Print the payment amount being stored


# First implementation using a list to accumulate payments
def payment_generator():
    # Generator to yield payments one by one.
    payment_queue = []

    def callback_fn(amount):
       # Callback function to be passed to stream_payments.
        payment_queue.append(amount)

    stream_payments(callback_fn)

    # Yield from the queue as we receive payments
    while payment_queue:
        yield payment_queue.pop(0)


def process_payments_2():
    # Process payments by streaming and then storing them.
    payments = payment_generator()

    store_payments(payments)


# Run the process to see it in action
process_payments_2()


