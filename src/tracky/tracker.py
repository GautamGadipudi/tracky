import inspect
import json
from time import time
import logging


class Tracker:

    # class level timestamp, used as a tag in output filename
    timestamp = int(time())

    # output path
    output_directory = './output/'

    # Write to file?
    is_log = True

    frame_id = 0

    frames = []

    @staticmethod
    def track():
        ########################
        # prev_frame: corresponds to the frame that called this method
        # prev_prev_frame: corresponds to the frame that called the method that we want to track
        ########################
        Tracker.frame_id += 1

        prev_frame = inspect.currentframe().f_back
        prev_prev_frame = prev_frame.f_back

        prev_frame_info = inspect.getframeinfo(prev_frame)
        prev_prev_frame_info = inspect.getframeinfo(prev_prev_frame)

        details = {
            "previous_frame": {
                "line_no": prev_prev_frame_info.lineno,
                "function": prev_prev_frame_info.function,
                "file_name": prev_prev_frame_info.filename,
                "module_name": inspect.getmodulename(prev_prev_frame_info.filename),
                "code_context": prev_prev_frame_info.code_context
            },
            "datatype": type(prev_frame.f_locals['self']).__name__,
            "function": prev_frame_info.function,
            "frame_id": Tracker.frame_id
        }

        print(f'{Tracker.frame_id}: module \"{details["previous_frame"]["module_name"]}\" in function \"{details["previous_frame"]["function"]}\" at line {details["previous_frame"]["line_no"]}')

        Tracker.frames.append(details)
        if Tracker.is_log:
            output_file_name = f'{details["previous_frame"]["module_name"]}_{Tracker.timestamp}.jsonl'
            output_file_path = f'{Tracker.output_directory}{output_file_name}'
            with open(f'{output_file_path}', mode='a') as f:
                data = json.dumps(details)
                f.write(f'{data}\n')
            
