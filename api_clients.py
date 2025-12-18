import requests

class APIClient:
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout

    def get(self, path: str, params: dict = None) -> dict:
        url = f"{self.base_url}/{path.lstrip('/')}"
        resp = requests.get(
            url,
            params=params,
            timeout=self.timeout,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )
        resp.raise_for_status()
        return resp.json()


