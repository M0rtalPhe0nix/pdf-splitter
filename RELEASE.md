# Release History

## [0.1.0] - 2025-03-08

### Added
- Initial release of PDF Splitter
- Core functionality to split PDFs by table of contents
- Command-line interface with level selection
- Support for Python 3.10+
- Poetry package management integration
- PyPI publishing workflow

### Features
- Split PDF files using table of contents structure
- Configurable splitting levels (1-3)
- Automatic clean filename generation
- Directory organization for split files

### Dependencies
- PyMuPDF (v1.25.3)
- Poetry core build system

### Known Limitations
- Requires PDF files with table of contents
- Only supports splitting by TOC levels
