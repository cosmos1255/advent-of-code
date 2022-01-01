# Day 8 Solution
# Problem found at https://www.adventofcode.com/2021/day/8

def parseInput(input):
    input_strings = []
    for line in input:
        new_line = line.split(' ')
        new_line.remove('|')
        input_strings.append(new_line)
    return input_strings

def partone(input):
    # 1 = len 2
    # 4 = len 4
    # 7 = len 3
    # 8 = len 8
    count = 0
    for arr in input:
        n = len(arr)
        for i in range(10, n):
            str_len = len(arr[i])
            if (str_len == 2 or str_len == 4 or str_len == 3 or str_len == 7):
                count += 1
        # print(count, ": ", arr[10:14])
    return count

# checks for letters from 'letStr' inside of 'strToCheck'
def checkForLets(strToCheck, letStr):
    numLets = 0
    for leti in strToCheck:
        for letj in letStr:
            if (leti == letj):
                numLets += 1
    if (numLets == len(letStr)):
        return True
    return False

def checkEqualStr(str1, str2):
    eq_cnt = 0
    if (len(str1) != len(str2)):
        return False
    for ch1 in str1:
        for ch2 in str2:
            if (ch1 == ch2):
                eq_cnt += 1
    if (eq_cnt == len(str1)):
        return True
    return False

def findNums(arr):
    # print(arr)
    i = 1
    nums = [""] * 10
    # step 1: find 1, 4, 7, 8
    for j in range(len(arr)):
        # print(arr)
        if (len(arr[j]) == 2): # 1 == 2 letters
            nums[1] += arr[j]
            arr[j] = ''
        elif (len(arr[j]) == 4): # 4 == 4 letters
            nums[4] += arr[j]
            arr[j] = ''
        elif (len(arr[j]) == 3): # 7 == 3 letters
            nums[7] += arr[j]
            arr[j] = ''
        elif (len(arr[j]) == 7): # 8 == 7 letters
            nums[8] += arr[j]
            arr[j] = ''
    arr.remove('')
    arr.remove('')
    arr.remove('')
    arr.remove('')
    # print(arr)
    # print(i, ": ",nums)
    # i+=1
    # step 2: find 3
    for num_str in arr:
        if (len(num_str) == 5):
            if (checkForLets(num_str, nums[1])):
                nums[3] += num_str
                arr.remove(num_str)
                break
    # print(i, ": ",nums)
    # i+=1
    # print(arr)
    # step 3: find 5 and 2
    in_four_not_one = ""
    for lets in nums[4]:
        if (not ((nums[1][0] == lets) or (nums[1][1] == lets))):
            in_four_not_one += lets
    # print(in_four_not_one)
    for num_str in arr:
        if (len(num_str) == 5):
            if (checkForLets(num_str, in_four_not_one)):
                nums[5] += num_str
                arr.remove(num_str)
                break
    for num_str in arr:
        if (len(num_str) == 5):
            nums[2] += num_str
            arr.remove(num_str)
            break
    # print(i, ": ",nums)
    # i+=1
    # print(arr)
    # step 4: find 0
    for num_str in arr:
        if (checkForLets(num_str, in_four_not_one)):
            nums[0] += num_str
            arr.remove(num_str)
            break
    # print(i, ": ",nums)
    # i+=1
    # print(arr)
    # step 5: find 9 and 6
    for num_str in arr:
        if (checkForLets(num_str, nums[1])):
            nums[9] += num_str
            arr.remove(num_str)
            break
    nums[6] += arr[0]
    # print(i, ": ",nums)
    # i+=1
    # print(arr)
    return nums

def parttwo(input):
    sum = 0
    for arr in input:
        # nums is a list of strings
        nums = findNums(arr[0:10])
        final_num = 0
        # print(nums)
        # print(arr[10:len(arr)])
        for output_num in arr[10:len(arr)]:
            # print(output_num)
            for i, num in enumerate(nums):
                if (checkEqualStr(output_num, num)):
                    final_num *= 10
                    final_num += i
                    break
        # print(final_num)
        sum += final_num
    return sum

def dayeight(input):
    # 0-9 is first 10; 10-13 is output
    input = parseInput(input)
    # print(input)
    print("Day 8 Solution:")
    print("PART1: Number of 1, 4, 7, and 8 values: ", partone(input))
    print("PART2: Sum of output digits: ", parttwo(input))