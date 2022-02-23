import argparse
import nastools.music as musictools

# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("--album", help="Define album")
parser.add_argument("--process", help="Define process")
 
# Read arguments from command line
args = parser.parse_args()
 
if args.process:
    if args.album:
        print("Processing", args.process, "on", args.album)