import inspect
import json
from time import time
import textwrap

class Tracker:

    # output path
    output_directory = './output/'

    @staticmethod
    def init(args):
        Tracker.mode = args.mode
        Tracker.frame_id = 0

        # class level timestamp, used as a tag in output filename
        Tracker.timestamp = int(time())

        Tracker.verbose = args.verbose

        if Tracker.mode == 'match':
            Tracker.target_frames = get_traces(args.targetfile)

        print_tracker_config()

    @staticmethod
    def track():
        ########################
        # prev_frame: corresponds to the frame that called this method
        # prev_prev_frame: corresponds to the frame that called the method that we want to track
        ########################
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
                "code_context": list(map(lambda exp: exp.strip(), prev_prev_frame_info.code_context))
            },
            "datatype": type(prev_frame.f_locals['self']).__name__,
            "function": prev_frame_info.function,
            "frame_id": Tracker.frame_id
        }

        if Tracker.verbose:
            print_frame(details, 'info')

        if Tracker.mode == 'collect':
            output_file_name = f'{details["previous_frame"]["module_name"]}_{Tracker.timestamp}.jsonl'
            output_file_path = f'{Tracker.output_directory}{output_file_name}'
            with open(f'{output_file_path}', mode='a') as f:
                data = json.dumps(details)
                f.write(f'{data}\n')
        elif Tracker.mode == 'match':
            target_frame = Tracker.target_frames[Tracker.frame_id]
            if details == target_frame:
                print(f'## Frame #{Tracker.frame_id} matched.')
            else:
                print(f'## Frame #{Tracker.frame_id} mismatched!')
                print_frame(details, print_type='log', prefix='Got')


                print_frame(target_frame, print_type='log', prefix='Expected')
                raise Exception("Frame mismatched")

        Tracker.frame_id += 1

def get_traces(filename):
    traces = []
    lines = []
    with open(filename, mode='r') as f:
        lines = f.readlines()

    traces = [json.loads(line) for line in lines]
    return traces


def print_tracker_config():
    print(textwrap.dedent(f'''
    ## Tracky config: 
        mode: \t\t{Tracker.mode}
        timestamp: \t\t{Tracker.timestamp} (this is a UUID for files when collecting data)
        output directory: \t{Tracker.output_directory} (for collect mode only)
    '''))

def print_frame(frame_details, print_type='log', prefix='## Tracky Frame'):
    valid_print_types = ['info', 'log']
    if print_type not in valid_print_types:
        raise ValueError(f'print_frame: arg \"print_type\" must be one of {valid_print_types}')
    

    if print_type == 'info':
        print(prefix, f'''
                        {Tracker.frame_id}: module \"{frame_details["previous_frame"]["module_name"]}\" in function \"{frame_details["previous_frame"]["function"]}\" at line {frame_details["previous_frame"]["line_no"]}''')
        # print(f'''## {prefix} - 
        #                 {Tracker.frame_id}: module \"{frame_details["previous_frame"]["module_name"]}\" in function \"{frame_details["previous_frame"]["function"]}\" at line {frame_details["previous_frame"]["line_no"]}''')

        for expression in frame_details['previous_frame']['code_context']:
                print(f'''\t\t\t\t\"{expression.strip()}\""''')
    elif print_type == 'log':
        print(prefix, json.dumps(frame_details, indent=1, sort_keys=True))