import io



def get_payments_storage():
    return io.BytesIO()  # In-memory bytes buffer, simulating storage



def stream_payments_to_storage(storage):
    # Simulate streaming some data to the storage
    storage.write(bytes([1, 2, 3, 4, 5]))
    storage.write(bytes([6, 7, 8]))
    storage.write(bytes([9]))


# Our StorageWrapper class to calculate the checksum
class StorageWrapper:
    def __init__(self, storage):
        self.storage = storage
        self.checksum = 0

    def write(self, buffer):
        self.checksum += sum(buffer)
        self.storage.write(buffer)

    def get_checksum(self):
        return self.checksum


# Our process_payments function
def process_payments():
    storage = get_payments_storage()
    wrapped_storage = StorageWrapper(storage)
    stream_payments_to_storage(wrapped_storage)
    print("Checksum:", wrapped_storage.get_checksum())


# Run the function to see the checksum
process_payments()
