"""
Write a function that accepts 2 lists as arguments. 
Both these 2 lists must be already sorted in the ascending order
This function should combine the lists into a sorted order and return the
resulting list. This function should not use any built-in sort function
or method.

- Write a test function that will test that the sorted list is correct. 
After successfully testing your program, 
    pass the following 2 lists as arguments to your function 
    and print the sorted result.

    - left  = [4, 17, 21, 47, 69, 75, 91, 97]
   - right = [3, 10, 11, 14, 18, 21, 44, 55, 76,97]
"""
import unittest

def get_combine_sort_lst(frst,sec):
    tot=frst+sec
    length=len(tot)
    res=list()
    for i in range(length):
        for j in range(length):
            if tot[i]<tot[j]:
                tot[i],tot[j]=tot[j],tot[i]
    [res.append(x) for x in tot if x not in res]
    #print(tot)
    return res


class Sorting(unittest.TestCase):

    def setUp(self):
        self.alist  = [4, 3, 1, 2, 0]
        self.sorted = [0, 1, 2, 3, 4]
        list.sort(self.alist)
    
    def test_order(self):
        self.assertTrue(self._is_ordered(), 'List is not in order')
    
    def test_permutation(self):
        self.assertCountEqual(self.alist,self.sorted,
                              'List is not a permutation of the original')
    
    def _is_ordered(self):
        for i in range(len(self.alist)-1):
            if self.alist[i] > self.alist[i+1]:
                return False
        return True
    
#main starts from here
##if __name__=="__main__":
##    frst_lst=[4, 17, 21, 47, 69, 75, 91, 97]
##    sec_lst=[3, 10, 11, 14, 18, 21, 44, 55, 76,97]
##    get_combine_sort_lst(frst_lst,sec_lst)
if __name__ == '__main__':
    unittest.main()
