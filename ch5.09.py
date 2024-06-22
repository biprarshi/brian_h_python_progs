from math import cbrt, exp, log, sqrt


count1 = 0
nums1 = ''
count2 = 0
nums2 = ''
count3 = 0
nums3 = ''

for i in range(1, 1001):
    if sqrt(i) == round(sqrt(i)) and cbrt(i) == round(cbrt(i)) and exp(log(i)/5) == round(exp(log(i)/5)):
        count1 += 1
        nums1 += str(i)+' '
    elif sqrt(i) == round(sqrt(i)) or cbrt(i) == round(cbrt(i)) or exp(log(i)/5) == round(exp(log(i)/5)):
        count2 += 1
        nums2 += str(i)+' '
    else:
        count3 += 1
        nums3 += str(i)+' '

print(f"No of integers from 1 to 1000 that are perfect squares and perfect cubes and perfect fifth powers = {
      count1} as follows:", nums1, '\n')
print(f"No of integers from 1 to 1000 that are either perfect squares or perfect cubes or perfect fifth powers = {
      count2} as follows:", nums2, '\n')
print(f"No of integers from 1 to 1000 that are neither perfect squares nor perfect cubes nor perfect fifth powers = {
      count3} as follows:", nums3)
