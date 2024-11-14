# removeDatedComments
This Python script removes comments containing dates in the format dd/dd/dddd from a given input file and writes the filtered content to an output file. It supports both single-line (//) and multi-line (/* */) comments. Createed for an assignment exploring parsing in programming languages.

## Features
Single-line comments: Removes lines starting with // if they contain a date.
Multi-line comments: Removes multi-line comments (/* */) that contain a date on any line.
Preserves comments and lines without dates.

## Usage
Command-line Arguments
The script requires two arguments:
- Input file: The file to process.
- Output file: The file to save the filtered content.
Command Example
python dcom_rm.py <input_file> <output_file>
Replace <input_file> with the path to your input file and <output_file> with the path where the cleaned file should be saved.

## Requirements
Python 3.12
