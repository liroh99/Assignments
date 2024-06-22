# DNA Sequence Analysis Tool

This tool allows you to analyze DNA sequences from FASTA or GeneBank files. It provides functionalities to find the longest duplicated subsequence and simple sequence repeats (microsatellites).

## Features

1. **Find the Longest Duplicate Subsequence**: Identifies the longest subsequence that appears twice in the sequence.
2. **Find Simple Sequence Repeats (SSRs)**: Identifies repetitive sequences of 2-6 base pairs that are repeated multiple times in the sequence.

## What Are Microsatellites?

Microsatellites, also known as Simple Sequence Repeats (SSRs) or Short Tandem Repeats (STRs), are repetitive sequences of DNA, typically consisting of 1-6 base pairs repeated in tandem arrays. These sequences are distributed throughout the genome and are highly polymorphic, making them valuable markers for genetic studies. Their high mutation rate, due to DNA replication slippage, leads to variations in the number of repeat units, which contributes to genetic diversity.

Microsatellites are used in various applications including:
- **Genetic Mapping**: To locate genes associated with diseases or traits.
- **Forensic Analysis**: To identify individuals based on their unique genetic profiles.
- **Population Genetics**: To study genetic variation within and between populations.
- **Conservation Biology**: To assess genetic diversi



### Running the Program

To run the program, use the following command in the terminal:
```
python check_sequence.py --path FILE_PATH [--duplicate] [--ssr]
```


## Dependencies

To install the necessary dependencies, run:
```
pip install -r requirements.txt
```


