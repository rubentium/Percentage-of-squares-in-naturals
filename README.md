# Percentage of squares in naturals

### Calculates the percentage of the square number from 1 upto and including the inputted value.


The function ```square_percentage``` takes in both ```int``` and ```float```. However, if the input ```float``` cannot be converted into a string without chnging the value, then a ```ValueError``` is raised. Similarly, if the input is nether an ```int``` nor ```float```. In case, if the value is less than 1, the same ```ValeError``` is raised as 1 is the infimum of the set of natural numbers.

### Examples
```
square_percentage(10)
>>> '3.0%'

square_percentage(100.00)
>>> '10.0%'

square_percentage('Hello World')
>>> ValueError: Input not a natural number

square_percentage(-10)
>>> ValueError: Input not a natural number
```
