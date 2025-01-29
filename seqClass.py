#!/usr/bin/env python

import sys
import re  
from argparse import ArgumentParser  

# Initialize argument parser
parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

# Print help message if no arguments are provided
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# Convert sequence to uppercase
args.seq = args.seq.upper()

# Ensure the sequence contains only valid nucleotide characters
if re.fullmatch(r'[ACGTU]+', args.seq):
    if 'T' in args.seq and 'U' in args.seq:  
        print('Error: Sequence cannot contain both T (DNA) and U (RNA).')
    elif 'T' in args.seq:
        print('The sequence is DNA.')
    elif 'U' in args.seq:
        print('The sequence is RNA.')
    else:
        print('The sequence can be DNA or RNA.')
else:
    print('Error: The sequence contains invalid characters. It is neither DNA nor RNA.')

# Motif search functionality
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end='')
    if re.search(args.motif, args.seq):
        print("FOUND MOTIF")
    else:
        print("MOTIF NOT FOUND")

