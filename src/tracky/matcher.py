import sys
import json

def main():
    good_json_file_path = sys.argv[1]
    bad_json_file_path = sys.argv[2]

    good_frames = []
    with open(good_json_file_path, mode='r') as f:
        lines = f.readlines()
        for line in lines:
            good_frames.append(json.loads(line))

    bad_frames = []
    with open(bad_json_file_path, mode='r') as f:
        lines = f.readlines()
        for line in lines:
            bad_frames.append(json.loads(line))

    if good_frames == bad_frames:
        print("SAME")

if __name__ == "__main__":
    main()