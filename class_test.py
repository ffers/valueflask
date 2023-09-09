class EvoClientExample(object):

    def __init__(self, token):
        self.token = token

    def print_token(self):
        print(f"Token: {self.token}")

# Створюємо об'єкт класу з передачею токену
evo_client = EvoClientExample("your_token_here")

# Викликаємо метод для виведення токену на екран
evo_client.print_token()
