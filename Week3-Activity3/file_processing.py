from ucimlrepo import fetch_ucirepo 
import pandas as pd
import numpy as np

def main():
    # Read the sample.txt file and print its contents
    data = open("sample.txt")
    lines = data.readlines()
    for line in lines:
        print(line[0:-1])  # Print each line without the newline character
    #data. Close()
    
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

    # Robust handling of target formats (1D labels, one-hot, or multi-col)
    y_arr = np.asarray(y)
    if y_arr.ndim > 1:
        # detect one-hot encoding (rows sum to 1 and entries are 0/1)
        if y_arr.shape[1] > 1 and np.all(np.logical_or(y_arr == 0, y_arr == 1)) and np.allclose(y_arr.sum(axis=1), 1):
            y_labels = y_arr.argmax(axis=1)
        else:
            # fallback: convert rows to tuples so unique works correctly
            y_labels = [tuple(row) for row in y_arr]
    else:
        y_labels = y_arr

    try:
        species_names = list(pd.unique(y_labels))
    except Exception:
        species_names = list(sorted(set(y_labels)))
    num_species = len(species_names)

    print(f"Total records: {total_records}")
    print(f"Number of different flowers: {num_species}")
    print(f"Flower names: {species_names}")

if __name__ == "__main__":
    main()