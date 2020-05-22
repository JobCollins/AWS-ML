s = [88, 92, 74, 48, 73] #student scores
print(sum(s)/len(s)) #calculating mean of the scores


s1 = [x ** 0.5 * 10 for x in s] #curves scores with sq root method and store in new list
print(sum(s1)/len(s1)) #print mean of curved scores




# without the comments it is hard to understand what is going on here