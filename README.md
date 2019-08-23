## Unit Testing Assignment

by Bill Gates.


## Test Cases for unique

Write a table describing your test cases.

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 item list, items in same order  |
| what other test case?  |  what result?       |
| many items, no duplicate  |  list with many items  |
| many items, many times |  list with many items  |
| many items, many times, many list  |  list with many item and list  |
| argument not a list  |  raise TypeError |


## Test Cases for Fraction

## Test Cases for Str

| Test case              |  Expected Result    |
|------------------------|---------------------|
| positive numerator and denominator |  fraction as a string that display "positive numerator/positive denominator"  |
| positive numerator and negative denominator | fraction as a string that display "negative numerator/positive denominator" |
| numerator and denominator have common factors and numerator and denominator have common factors | fraction as a string that display "numerator that have no common factors/denominator that have no common factors" |
| only numerator | integer as a string that display "numerator" |
| numerator and 1 | integer as a string that display "numerator" |
| numerator and -1 | integer as a string that display "-numerator" |
| 1 and 0 (infinite number) | fraction as a string that display "1/0" |
| -1 and 0 (negative infinite) | fraction as a string that display "-1/0" |
| 0 and 0 (Nan) | fraction as a string that display "0/0" |

## Test Cases for init

| Test case              |  Expected Result    |
|------------------------|---------------------|
| positive numerator and denominator | positive numerator and denominator |
| positive numerator and negative denominator | negative numerator and positive denominator |
| only numerator | numerator and denominator = 1 |
| numerator = 1 and denominator = 0 | numerator = 1 and denominator = 0 |
| numerator and denominator have common factors | numerator and denominator have no common factors |
| numerator and negative denominator have common factors | negative numerator and denominator have common factors |
| -1 and 0 (infinite number) | numerator = -1 and denominator = 0 |
| 0 and 0 (Nan) | numerator = 0 and denominator = 0 |
| 0 and 0 (Nan) | numerator = 0 and denominator = 0 |
| argument not an integer | raise TypeError: type object cannot be interpreted as an integer |


## Test Cases for add

| Test case              |  Expected Result    |
|------------------------|---------------------|
| 2 positive fraction | sum of positive fraction |
| (numerator and denominator have no common factors) and (numerator and denominator have no common factors) | sum of positive fraction that have no common factors |
| (negative numerator and denominator)and (numerator and negative denominator)| sum of fraction that have sign as the sign of greater fraction |
| (numerator and denominator have common factors) and (numerator and denominator have common factors) | sum of positive fraction that have no common factors |
| (numerator and denominator have common factors) and (numerator and denominator have no common factors) | sum of positive fraction that have no common factors |
| 1/0 and 0/0 (infinity + Nan = Nan)  | 0/0 (nan) |
| positive fraction and 0/0 (number + Nan = Nan) | 0/0 (nan) |
| negative fraction and 0/0 (negative number + Nan = Nan) | 0/0 (nan) |
| 1/0 and 0/0 (infinity + Nan = Nan) | 0/0 (nan) |
| 0 and 1/0 (number + infinity = infinity) | 1/0 (infinity) |
| 1/0 and 1/0 (infinity  + infinity = infinity) | 1/0 (infinity) |
| 1/0 and -1/0 (infinity - infinity = Nan)  | 0/0 (nan) |
| (numerator is greater than 0 and denominator = 0) and (numerator is less than 0 and denominator = 0) | 0/0 (nan) |
| (numerator is greater than 0 and denominator = 0) and (numerator is greater than 0 and denominator = 0) | 1/0 (infinity) |


## Test Cases for multiply

| Test case              |  Expected Result    |
|------------------------|---------------------|
| 2 positive fraction | product of positive fraction |
| (numerator and denominator have no common factors) and (numerator and denominator have no common factors) | product of positive fraction that factors no common factors|
| (numerator and denominator have common factors) and (numerator and denominator have common factors) | product of positive fraction that factors no common factors |
| (numerator and denominator have common factors) and (numerator and denominator have no common factors) | product of positive fraction that factors no common factors |
| (numerator of fraction is negative) and (positive fraction) | product of fraction that have negative numerator and positive denominator |
| (positive fraction) and ( denominator of fraction is negative) | product of fraction that have negative numerator and positive denominator |
| positive fraction and 0/0 (number * Nan = Nan) | 0/0 (nan) |
| 0 and 1/0 (0 * infinity = Nan) | 0/0 (nan) |
| 0 and -1/0 (0 * negative infinity = Nan) | 0/0 (nan) |
| 1/0 and -1/0 (infinity  * negative infinity = negative infinity)  | -1/0 ( negative infinity) |
| (numerator is greater than 0 and denominator = 0) and (numerator is less than 0 and denominator = 0) | -1/0 ( negative infinity) |
| (numerator is greater than 0 and denominator = 0) and (numerator is greater than 0 and denominator = 0) | 1/0 ( positive infinity) |



## Test Cases for equal

| Test case              |  Expected Result    |
|------------------------|---------------------|
| 2 fraction that have same numerator and denominator | True |
| 2 fraction that have only same numerator | False |
| 2 fraction that have only same denominator | False |
| 2 fraction that have same numerator and denominator but sign is different | False |
| 2 fraction that have denominator equal 0 and sign is the same | True |
| -1/0 and 1/0 | False |
| 2 fraction that have denominator equal 0 but sign is the different | False |
| 0 and 0/0 (number ana Nan)| False |









