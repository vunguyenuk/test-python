def process_data(data): 
     if data is None: 
         raise ValueError('Input data cannot be None')  
     try: iter(data)  # Check if data is iterable 
     except TypeError: 
         raise TypeError('Input data must be iterable')  
     return [  
         item * 2 if isinstance(item, int) and item > 0 else 0
         for item in data 
     ]