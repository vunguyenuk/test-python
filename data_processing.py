# File: data_processing.py
def process_data(data):
    return [
        item * 2 if isinstance(item, int) and item > 0 else 0
        for item in data
    ]
