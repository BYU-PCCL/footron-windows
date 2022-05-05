import requests

_ENDPOINT_CURRENT_EXPERIENCE = "/current"


class LastControllerInputApi:
    def __init__(self, url):
        self.url = url
        self.last_input_time = None

    def _url_with_endpoint(self, endpoint) -> str:
        return f"{self.url}{endpoint}"

    def set_last_input(self, last_input):
        # print("last input updated")
        # print(last_input)
        if last_input[0] != self.last_input_time or last_input[1] == True:
            print(str(last_input[0]) + ", holding = " + str(last_input[1]))
            self.last_input_time = last_input[0]
            # response = requests.patch(
            #     self._url_with_endpoint(_ENDPOINT_CURRENT_EXPERIENCE),
            #     json={"last_interaction": last_input[0]},
            # )
        else:
            print("no change")

        # error codes
        # if response.status_code == x:
        #     #hmmmmm

        return True