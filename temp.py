def binary_search(arr, key):
  #start in the middle
  index = len(arr) // 2

  #if index goes above or below, the key doesn't exist
  while index > -1 and index < len(arr):
    num = arr[index]
    if num == key: return index
    if num < key:
      if len(arr) - index <= 2: index += 1
      else:
        index += index // 2 
    if num > key: 
      if index <= 1: index = 0
      else:
        index = index // 2 
  return -1

def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()