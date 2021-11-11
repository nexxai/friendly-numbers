# friendly-numbers

As described on [Numberphile](https://www.youtube.com/watch?v=KZ1BVlURwfI), this script will attempt to find friendly numbers for a given integer.

## Installation
Install the dependencies:

```python
pip3 install -r requirements.txt
```

## Usage
Update the `index_search`, `where_to_start`, and `where_to_end` variables in the `friendly.py` file to appropriate values if you are not using the defaults, and then simply run:

```sh
python3 friendly.py
```

Progress will be reported on screen every 10,000 checks and written to a checkpoint file for easy resumption if the script is stopped for whatever reason.