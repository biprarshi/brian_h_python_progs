print('Enter 10 scores:')
nums1 = []
extra_num1 = {}

for i in range(10):
    num1 = eval(input())
    nums1.append(num1)
    if num1 > 100:
        extra_num1[i] = num1
for index1, value1 in extra_num1.items():
    print(f'Value over 100 entered at index: {index1}:{value1}')

print("Highest score is: {}, and lowest score is: {}.".format(max(nums1), min(nums1)))
print(f'The average of the scores is: {sum(nums1)/len(nums1)}')
nums2 = nums1.copy()
nums2.remove(max(nums2))
print(f"The second largest score is: {max(nums2)}")

nums2 = nums1.copy()
nums2.remove(min(nums2))
nums2.remove(min(nums2))
# print('The average of',end=' ')
# for num1 in nums2:
#     print(num1,end=' ')
# print(f'is: {sum(nums2)/len(nums2)}')

print('The average of', *nums2, f'is: {sum(nums2)/len(nums2)}')
print(' '.join(str(i) for i in nums1))