# File: data_processing.py
def process_data(data):
    result = []
    for i in range(len(data)):
        item = data[i]
        if isinstance(item, int) and item > 0:
            transformed_item = item * 2
            result.append(transformed_item)
        else:
            result.append(0)
    return result