"""
Write a program that generates a HTML webpage. 
Prompt the user for webpage title and webpage body contents. 
 """
webpage_title=input('Enter the webpage title:')
main_header=input('Enter the main_header:')
sub_header=input('Enter the sub_header:')
para_1=input('first paragraph:')
para_2=input('sec paragraph:')
print()
print()
print()
print('{:^40s}'.format('\u0332'.join(webpage_title)))
print('{:^20s}'.format(main_header))
print('{:^10s}'.format(sub_header))
print()
print('{:<s}'.format(para_1))
print()
print('{:<s}'.format(para_2))
