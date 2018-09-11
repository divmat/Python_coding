#Write your function here
def reversed_list(lst1, lst2):
  count = 0
  for i in range(0, len(lst1)):
    if lst1[i] == lst2[-i - 1]:
      count += 1
  if count == len(lst1):
    return True
  return False

#Uncomment the lines below when your function is done
#print(reversed_list([1, 2, 3], [3, 2, 1]))
#print(reversed_list([1, 5, 3], [3, 2, 1]))
