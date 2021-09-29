import inspect
import json
from time import time


class Tracker:
    operations = []

    def track(self, is_log=True):
        current_frame = get_current_frame().f_back
        previous_frame = current_frame.f_back

        current_frame_info = get_frame_info(current_frame)
        previous_frame_info = get_frame_info(previous_frame)

        details = {
            "previous_frame": {
                "filename": previous_frame_info[0],
                "lineno": previous_frame_info[1],
                "function": previous_frame_info[2],
                "expression": previous_frame_info[3]
            },
            "datatype": type(self).__name__,
            "function": current_frame_info[2]
        }

        if is_log:
            Tracker.operations.append(details)

    @staticmethod
    def dump(dir='/', filename='output.json'):
        filepath = f'{dir}{filename}_{int(time())}.json'
        with open(filepath, 'w') as f:
            json.dump(Tracker.operations, f, indent=4)


def get_current_frame():
    return inspect.currentframe().f_back


def get_frame_info(frame):
    return inspect.getframeinfo(frame)
