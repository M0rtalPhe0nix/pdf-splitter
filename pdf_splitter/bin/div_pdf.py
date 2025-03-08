#!/usr/bin/env python3
import sys
import os
from pdf_splitter.src.pdf import split_pdf_by_toc
import argparse
arg_parser = argparse.ArgumentParser(description='Split a PDF file by its table of contents')
arg_parser.add_argument('pdf_file', help='The PDF file to split')
arg_parser.add_argument('--level', type=int, default=1, help='The level of the table of contents to split')
def main():
    args = arg_parser.parse_args()
    split_pdf_by_toc(args.pdf_file, args.level)
    return 0
# def main():
#     if len(sys.argv) != 2:
#         print("Usage: pdf-splitter <pdf_file> [level]")
#         return 1
#     split_pdf_by_toc(sys.argv[1])
#     return 0

if __name__ == '__main__':
    sys.exit(main())