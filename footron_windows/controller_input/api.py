import requests

_ENDPOINT_CURRENT_EXPERIENCE = "/current"


class LastControllerInputApi:
    def __init__(self, url):
        self.url = url
        self.last_input_time = None

    def _url_with_endpoint(self, endpoint) -> str:
        return f"{self.url}{endpoint}"

    def set_last_input(self, last_input):
        if last_input != self.last_input_time:
            print(last_input)
            self.last_input_time = last_input
            # response = requests.patch(
            #     self._url_with_endpoint(_ENDPOINT_CURRENT_EXPERIENCE),
            #     json={"last_interaction": last_input},
            # )
        else:
            print("no change")

        return True