import requests

_ENDPOINT_CURRENT_EXPERIENCE = "/current"


class LastControllerInputApi:
    def __init__(self, url):
        self.url = url

    def _url_with_endpoint(self, endpoint) -> str:
        return f"{self.url}{endpoint}"

    def get_current(self):
        return requests.get(
            self._url_with_endpoint(_ENDPOINT_CURRENT_EXPERIENCE)
        ).json()

    def set_last_input(self, last_input):
        response = requests.patch(
            self._url_with_endpoint(_ENDPOINT_CURRENT_EXPERIENCE),
            json={"last_interaction": last_input},
        )
        return True
