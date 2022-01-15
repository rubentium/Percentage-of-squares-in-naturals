
def square_percentage(final) -> str:
  '''
  Gives the percentage of square
  numbers in the closed interval of
  [1, final]. If final is not a
  natural number, the function
  raises a ValueError.
  '''
  # if neither int nor float then can't be natural
  if isinstance(final, int) or isinstance(final, float):

    # if with some numbers (other than all 0's) after
    # decimal point then not a natural
    if int(final) - final != 0:

      raise ValueError('Input not a natural number')

    # if less than 1 than not a natural
    if final > 0:

      natural = 1
      count_origin = 0
      while natural**2 <= final:
        count_origin += 1
        natural += 1

      return f'{count_origin*100/final}%'

    else:
      raise ValueError('Input not a natural number')

  else:
    raise ValueError('Input not a natural number')


print(square_percentage(-10))
