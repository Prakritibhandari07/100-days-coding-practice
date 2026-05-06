def func1():
  try:
    L=[1,5,6,7]
    i=int(input("Enter the index: "))
    print(L[i])
    return 1
  except:
    print("some error occurred")
    return 0
  finally:
    print("I am always executed.")    