import requests


class LastControllerInputApi:
    LAST_CONTROLLER_INPUT_ENDPOINT = "last_controller_input"

    def __init__(self, url):
        self.last_input_time = None
        # stuff
        True

    def set_last_input(self, last_input):
        # print("last input updated")
        # print(last_input)
        if last_input[0] != self.last_input_time:
            print(str(last_input[0]) + ", holding = " + str(last_input[1]))
            self.last_input_time = last_input[0]
        else:
            print("no change")
        # response = requests.put(
        #     # endpoint,
        #     headers={"Content-Type": "application/json"},
        #     json={"timestamp" : last_input[0].timestamp, #time in seconds, might just be last_input[0]
        #             "holding" : last_input[1]},
        # )

        # error codes

        return True

        #         # TODO check HTTP code before updating internal state
        # response = requests.put(
        #     self._current_endpoint,
        #     headers={"Content-Type": "application/json"},
        #     json={"id": current.id},
        # )

        # if response.status_code == 429:
        #     logging.warning("Tried to set current experience too soon after user")
        #     return False

        # self._last = self._current
        # self._current = current
        # return True
