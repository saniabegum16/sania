#Define two arrays(list)
array1=[1,2,3,4,5]
array2=[4,5,6,7,8]
#Convert arrays to sets and find intersection
common_values=set(array1).intersection(set(array2))
common_values=list(common_values)
print("common values between the two arrays:",common_values)
