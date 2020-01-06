import random


class ApiClient:
    def __init__(self, client_factory=None):
        self.api_factory = client_factory

    def get_api(self):
        api = self.api_factory()
        print(f"""Connect to {api}""")
        print(f"""Get api key: {api.get_key()}""")


class GoogleClient:
    def get_key(self):
        return "GOOGLE_API_KEY"

    def __str__(self):
        return "GoogleClient"


class AwsClient:
    def get_key(self):
        return "AWS_API_KEY"

    def __str__(self):
        return "AwsClient"

def random_client():
    return random.choice([GoogleClient, AwsClient])()


if __name__ == "__main__":
    google_client = ApiClient(GoogleClient)
    google_client.get_api()
