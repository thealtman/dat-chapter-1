 #Write a function that takes a list of numbers numbers and returns a sublist of numbers
 # with only those numbers that are divisible by 33.
def div_33( numbers ):
  to_return = []
  for num in numbers:
    if num % 33 == 0:
      to_return.append( num )
  return to_return

numbers = [ x for x in range( 1, 400) ]
print div_33( numbers )