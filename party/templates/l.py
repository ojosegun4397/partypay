arr = [1,2,3,4,5,6,7,8,10]; 
def missing():
  missing_range=[x for x in range(arr[0],arr[-1]) if x not in arr]
  print(missing_range)
missing()

arr = [1,2,3,1,4,5,6,7,7,8,10]
def duplicate():
 duplicatenum=[x for x in arr if arr.count(x)>1]
 print( duplicatenum)

duplicate()