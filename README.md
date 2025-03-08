# PDF Splitter

A command-line tool to split PDF files based on their table of contents (TOC) entries. This tool creates separate PDF files for each level 1 heading in the document's table of contents.

## Features

- Splits PDF files using the table of contents structure
- Creates separate files for each major section (level 1 TOC entries)
- Automatically generates clean filenames from section titles
- Preserves PDF content and formatting

## Prerequisites

- Python 3.10 or higher
- Poetry package manager

## Installation

You can install the package using either of these two methods:

### Method 1: Direct Poetry Install

```bash
git clone https://github.com/M0rtalPhe0nix/pdf-splitter.git
cd pdf-splitter
poetry install
```

### Method 2: Build and Install with pip

```bash
git clone https://github.com/M0rtalPhe0nix/pdf-splitter.git
cd pdf-splitter
poetry build
pip install dist/*.whl
```

## Usage

After installation, you can use the tool directly from the command line:

```bash
pdf-splitter <path-to-pdf-file> [--level N]
```

The `--level` flag is optional (defaults to 1) and specifies the TOC level to split at:
- `--level 1`: Split at main chapters (default)
- `--level 2`: Split at subchapters
- `--level 3`: Split at sub-subchapters

The tool will:
1. Create a new directory named `divided_<original-filename>`
2. Split the PDF based on the specified TOC level
3. Save the split files with numbered prefixes and section titles as filenames

## Example

```bash
pdf-splitter textbook.pdf
```

This will create files like:
```
divided_textbook/
├── 01_Introduction.pdf
├── 02_Chapter_1.pdf
├── 03_Chapter_2.pdf
...
```

## Limitations

- The PDF must have a table of contents (TOC)

## License

MIT License

Copyright (c) 2024 M0rtalPhe0nix

For full license text, see [LICENSE](LICENSE)
