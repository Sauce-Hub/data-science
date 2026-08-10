from load_data import load_data
from preprocessing import process_data

def main():
    data = load_data()
    
    data = process_data(data)
    