

def add_all(*args):
    sum_all = 0

    for num in args:
        sum_all += num

    return sum_all



def print_all(**kwargs):
    
    for key, value in kwargs.items():
        print(key + ': ' + str(value))

print_all(name= 'dumbledore', job='headmaster', age=18)
print(add_all(1,2,3,4,5,6))



spells = ["protego", "accio", "expecto patronum", "legilimens"]

shout_spells = map(lambda item: item + '!!!', spells)
print(list(shout_spells))




fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member) > 6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Print result_list
print(result_list)






# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)
