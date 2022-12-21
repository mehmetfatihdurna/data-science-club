#Loops
nums = [12, 8, 9, 10, 15]
print(nums)
new_nums = [num + 1 for num in nums]
print(new_nums)


#Nested loops
pairs_1 = [(num1, num2) for num1 in range(0,2) for num2 in range(6,8)]
print(pairs_1)


#IF ELSE CONDITIONS

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
new_fellowship = [member for member in fellowship if len(member) >= 7]
print(new_fellowship)


new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]

print(new_fellowship)



#Dict comprehension

new_dict = {member: len(member) for member in fellowship}


#Generator object
generator_1 = (i for i in range(10**10000000))

print(next(generator_1)




#Build a generator function

def num_sequence(n):
    """Generate values from 0 to n."""
    i = 0
    while i < n:
        yield i
        i += 1

