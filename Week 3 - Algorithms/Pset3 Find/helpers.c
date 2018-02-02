/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */

#include <cs50.h>

#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
 //    if (search(needle, haystack, size))
bool search(int value, int values[], int n)
{
    // TODO: implement a searching algorithm - This is binary search algo
    // declare variables
    int min = 0, max = n - 1;

    // checking to see if the size of the array n, is less than one
    while (n > 0)
    {
        // look at middle of list
        int midIndex = (max - min) / 2 + min;
        // if number found, return true
        if (values[midIndex] == value)
        {
            return true;
        }
        // if number is higher, search left
        else if (values[midIndex] > value)
        {
            max = midIndex - 1;
        }
        // if number is lower, search right
        else if (values[midIndex] < value)
        {
            min = midIndex + 1;
        }
        // set new size of elements
        n = max - min + 1;
    }
    // if # is not found then return false (didn't find need in haystack)
    return false;
}

/**
 * Sorts array of n values.
 */
 //     sort(haystack, size);
void sort(int values[], int n)
{
    // TODO: implement a sorting algorithm - this is selection sort
    // loop through each element in the unsorted array
    for(int i = 0; i < n - 1; i++)
    {
        // set current element to be min
        int indexMin = i;

        // check the element to be minimum
        for(int j = i + 1; j < n; j++)
        {
            {
                if(values[j] < values[indexMin])
                    indexMin = j;
            }
        }
        // if indexMin has changed then exchange i w/ lowest value
        if(indexMin != i)
        {
            int exchange = values[indexMin];
            values[indexMin] = values[i];
            values[i] = exchange;
        }
    }
    return;
}
