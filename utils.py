import pandas as pd
import numpy as np
import os

# function to generate random sales with a min value and max value , and a given size 
def generate_random_sales(min_val, max_val, size):
    #randint to generate random integers with min and max val and size for how many we want to generate
    return np.random.randint(min_val, max_val + 1, size)

def create_dataset():
    print("Generating data...")
    
    #generate monthly dates for the year 2025
    #freq='MS' means "Month Start"
    dates = pd.date_range(start='2025-01-01', periods=12, freq='MS')
    
    #generate sales for the 4 products using our helper function
    # We use a Python dictionary to structure the data easily before making a DataFrame
    data = {
        'Date': dates,
        'Product_A': generate_random_sales(50, 100, 12),
        'Product_B': generate_random_sales(30, 80, 12),
        'Product_C': generate_random_sales(20, 60, 12),
        'Product_D': generate_random_sales(10, 50, 12)
    }
    
    #creation of dataframe
    df = pd.DataFrame(data)
    
    #Define the output path
    # We assume the folder structure is project_sales/data/
    output_path = 'data/initial.csv'
    
    # create data folder 
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 6. Save as CSV (without the index numbers)
    df.to_csv(output_path, index=False)
    

    print("\nHere are the first 10 rows of your generated data:")
    print(df.head(10))

if __name__ == "__main__":
    create_dataset()