from load_data import load_data
from process_data import process_data
from recommendation import get_recommendation

def main():
    data = load_data()
    
    data = process_data(data)
    
    # recommendation = get_recommendation(data,1)
    # print(recommendation)

if __name__ == "__main__":
    main()