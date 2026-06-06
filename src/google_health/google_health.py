from .client import Client

class GoogleHealth:
    def __init__(self) -> None:
        print("Hello from GoogleHealth!")
        self.client = Client()