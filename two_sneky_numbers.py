
from collections import Counter
def sneky_numbers(lst):
    counter=Counter(lst) 


    for x, count in counter.items():
        if count==2:
            print(x) 
            
# Main function #            