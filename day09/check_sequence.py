import argparse
import re 
from Bio import SeqIO


def find_longest_duplicate(sequence):
    length = 1
    result = ''
    while True:
        regex = r'([GATC]{' + str(length) + r'}).*\1'
        match = re.search(regex, sequence)
        if match:
            result = match.group(1)
            length += 1
        else:
            break
    return result


def find_ssrs(sequence):
    ssr_patterns = [
        r'([GATC]{2,6})\1{2,}',  # Repeats of 2 to 6 nucleotides, repeated at least three times
    ]
    ssrs = []
    for pattern in ssr_patterns:
        matches = re.findall(pattern, sequence)
        for match in matches:
            if match not in ssrs:
                ssrs.append(match)
    return ssrs


def main():
    parser = argparse.ArgumentParser(description="Analyze DNA sequences to find duplications and microsatellites")
    parser.add_argument('--path', help="Path to FASTA/GeneBank file", required=True)
    parser.add_argument('--duplicate', '-dp', action="store_true", help="Find the longest duplicated sequence")
    parser.add_argument('--ssr', action="store_true", help="Find simple sequence repeats (SSRs)")
    args = parser.parse_args()
    
    if not args.duplicate and not args.ssr:
        parser.error("please insert a request: --duplicate or --ssr")

    if args.path.endswith(".gb") or args.path.endswith(".gbk"):
        file_format = "genbank"
    elif args.path.endswith(".fasta") or args.path.endswith(".fa"):
        file_format = "fasta"
    else:
        raise ValueError("Unsupported file format. Please provide a FASTA or GeneBank file.")
    
    for sequence in SeqIO.parse(args.path, file_format):
        sequence = str(sequence.seq)
        if args.duplicate:
            longest_dup = find_longest_duplicate(sequence)
            print(f"Longest duplicate subsequence: {longest_dup}")
        
        if args.ssr:
            ssrs = find_ssrs(sequence)
            print(f"Simple sequence repeats found: {ssrs}")



if __name__ == "__main__":
    main()