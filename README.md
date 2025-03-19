Little python scripts to convert [Pocket](https://getpocket.com/saves) data export csv file into [zotero](https://www.zotero.org/) importable CSV-JSON & BibTeX formats.

## Setup

`$ pip install -r requirements.txt`

## Usage

1. Convert Pocket CSV file to CSL-JSON json file

`$ python ./src/csv2csljson.py`

2. Convert CSL-JSON file to BiBTex file

`$ python ./src/csljson2bibtex.py`

3. Import `./out/bibtex.txx` to Zotero.
