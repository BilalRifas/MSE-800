from ucimlrepo import fetch_ucirepo 
import pandas as pd
import numpy as np

def main():
    # fetch dataset 
    iris = fetch_ucirepo(id=53) 
    
    # data (as pandas dataframes) 
    X = iris.data.features 
    y = iris.data.targets 

    # metadata 
    #print(iris.metadata) 
    
    # variable information 
    #print(iris.variables) 

    # --- Find counts and species names ---
    total_records = X.shape[0] if hasattr(X, "shape") else len(X)

    # Convert y to a numpy array for easier processing
    y_arr = np.asarray(y)
    if y_arr.ndim > 1:
        # Check if the array is one-hot encoded 
        if y_arr.shape[1] > 1 and np.all(np.logical_or(y_arr == 0, y_arr == 1)) and np.allclose(y_arr.sum(axis=1), 1):
            y_labels = y_arr.argmax(axis=1)
        else:
            # fallback: convert rows to tuples so unique works correctly
            y_labels = [tuple(row) for row in y_arr]
    else:
        y_labels = y_arr

    try:
        # Use pandas to get unique species names if possible
        species_names = list(pd.unique(y_labels))
    except Exception:
        # Fallback to using set and sorted if pandas fails
        species_names = list(sorted(set(y_labels)))
    num_species = len(species_names)

    print(f"Total records: {total_records}")
    print(f"Number of different flowers: {num_species}")
    print(f"Flower names: {species_names}")

if __name__ == "__main__":
    main()