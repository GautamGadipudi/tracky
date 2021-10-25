import inspect
import json
import time
import textwrap
from pathlib import Path
import util.io as io


class Tracker:
    '''
        Initialize tracker config
            Set tracker mode
            Set class level variables
    '''
    @staticmethod
    def init(args):
        Tracker.mode = args.mode
        Tracker.frame_id = 0

        # class level timestamp, used as a tag in output filename
        Tracker.timestamp = time.strftime(
            '%Y%m%dT%H%M%S%Z', time.localtime(time.time()))

        Tracker.verbose = args.verbose

        if Tracker.mode == 'match':
            Tracker.target_frames = get_metadata_from_file(args.targetfile)
        else:
            Tracker.output_directory = args.outputdirectory
            Tracker.output_filename = f"{args.outputdirectory}{args.jsoninputpath.split('/')[-1].split('.')[0]}-{Tracker.timestamp}.jsonl"

            # Create nested output directory if not exists
            Path(Tracker.output_directory).mkdir(parents=True, exist_ok=True)

        print_tracker_config()

    '''
        Triggered from overloaded methods
            Collect frame details
            Match frame details against target frame
    '''
    @staticmethod
    def track():
        prev_frame = inspect.currentframe().f_back
        prev_prev_frame = prev_frame.f_back

        metadata = get_frame_metadata(prev_frame, prev_prev_frame)

        if Tracker.verbose:
            print("Tracker triggered at frame:")
            print_frame(metadata, 'info')

        if Tracker.mode == 'collect':
            Tracker.collect(metadata)
        elif Tracker.mode == 'match':
            Tracker.match(metadata)

        Tracker.frame_id += 1

    @staticmethod
    def match(metadata):
        target_metadata = Tracker.target_frames[Tracker.frame_id]

        is_match = match_frames(metadata, target_metadata)
        if is_match:
            print(f'## Frame #{Tracker.frame_id} matched.')
        else:
            print(f'## Frame #{Tracker.frame_id} mismatched!')

            print('Got')
            print_frame(metadata, print_type='log')

            print('Expected')
            print_frame(target_metadata, print_type='log')

            raise Exception("Frame mismatched")

    @staticmethod
    def collect(metadata):
        io.append_to_file(Tracker.output_filename, json.dumps(metadata))


def match_frames(metadata, target_metadata):
    return metadata == target_metadata


def get_frame_metadata(prev_frame, prev_prev_frame):
    prev_frame_info = inspect.getframeinfo(prev_frame)
    prev_prev_frame_info = inspect.getframeinfo(prev_prev_frame)

    metadata = {
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

    return metadata


def get_metadata_from_file(filename):
    metadata_list = io.read_metadata(filename)

    return [json.loads(metadata) for metadata in metadata_list]


def print_tracker_config():
    print(textwrap.dedent(f'''
    ## Tracky config: 
        mode: \t\t{Tracker.mode}
        timestamp: \t\t{Tracker.timestamp} (this is a UUID for files when collecting data)
        output directory: \t{Tracker.output_directory} (for collect mode only)
    '''))


def print_frame(frame_details, print_type='log'):
    valid_print_types = ['info', 'log']
    if print_type not in valid_print_types:
        raise ValueError(
            f'print_frame: arg \"print_type\" must be one of {valid_print_types}')

    if print_type == 'info':
        print(
            f'''{Tracker.frame_id}: \tmodule \"{frame_details["previous_frame"]["module_name"]}\" in function \"{frame_details["previous_frame"]["function"]}\" at line {frame_details["previous_frame"]["line_no"]}''')

        for expression in frame_details['previous_frame']['code_context']:
            print(f'''\t"{expression.strip()}\""''')
    elif print_type == 'log':
        print(json.dumps(frame_details, indent=1, sort_keys=True))


def get_tracker():
    return Tracker
