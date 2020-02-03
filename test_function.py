"""
test function for dsum
"""
import sumops
import array
res=[]
num=[9,24,125,5892]
res_eval=[9,6,8,24]
for value in num:
    res.append(sumops.dsum(value))
if res==res_eval:
    print("""Tested
Ok""")
else:
    print("""Tested
Not Ok""")
