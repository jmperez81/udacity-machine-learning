#!/usr/bin/python
from numpy import subtract, square, argmin, take, delete
import sys

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    
    # Calculation of square error
    sqe = square(subtract(predictions, net_worths))

    # Calculating target number of elements (90%)
    m = len(ages)
    desired_m = (90 * m) / 100
    print("Reducing training set from ", m, " to ", desired_m)

    # Iteration to keep 90 samples with smaller errors
    i = 0
    while i < desired_m:
        min_sqe_index = argmin(sqe)        
        min_sqe_value = take(sqe, min_sqe_index)
        print(min_sqe_value)
        sqe[min_sqe_index] = sys.maxint
        cleaned_data.append((ages[min_sqe_index], net_worths[min_sqe_index], min_sqe_value))
        i = i + 1

    return cleaned_data