class ClientVendor:
    def __init__(self, client_vendor_id, name, type):
        self.client_vendor_id = client_vendor_id
        self.name = name
        self.type = type
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def display_client_vendor_info(self):
        return f"ID: {self.client_vendor_id}, Name: {self.name}, Type: {self.type}"

class ClientVendorManagement:
    def __init__(self):
        self.clients_vendors = {}

    def add_client_vendor(self, client_vendor):
        self.clients_vendors[client_vendor.client_vendor_id] = client_vendor

    def generate_client_vendor_report(self):
        for client_vendor in self.clients_vendors.values():
            print(client_vendor.display_client_vendor_info())
