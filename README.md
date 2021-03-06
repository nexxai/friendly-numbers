# friendly-numbers

As described on [Numberphile](https://www.youtube.com/watch?v=KZ1BVlURwfI), this script will attempt to find friendly numbers for a given integer.

## Installation
Install the dependencies:

```python
pip3 install -r requirements.txt
```

## Usage
Update the `index_search`, `search_space_start`, and `search_space_end` variables in the `friendly.py` file to appropriate values if you don't want to use the defaults, and then simply run:

```sh
python3 friendly.py
```

Progress will be reported on screen every 10,000 checks and written to a checkpoint file for easy resuming if the script is stopped for whatever reason.

## Contributions
All pull requests are welcome.  This script was whipped up in about 30 minutes by a very non-Python developer.  There are almost certainly many ways it could be improved, either from a coding quality or performance perspective.