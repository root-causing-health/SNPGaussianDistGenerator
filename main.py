#!/usr/bin/env python3
import numpy as np
import pandas as pd

def main():
    df = pd.read_csv('snps.csv')  # CSV of Name, Mean, SD
    df["normal_dist"] = df.apply(generate_distribution, axis=1)  # Generate a random normal dist for each row
    df.to_csv('output.csv', index=False)  # Write the output to CSV

def generate_distribution(row):
    return np.random.normal(row["mean"], row["sd"], 1000)  # Generate dist. using mean/sd, 1000 values in the output

if __name__ == "__main__":
    main()