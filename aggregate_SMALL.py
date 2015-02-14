"""
This program runs through the accumulated follower lists, and compares them to one another.
"""

#a dictionary containing the IDs of everyone following any of the accounts.
aggregate_followers = {};

#For this smaller version, I am manually listing the accounts we are looking at.
twitter_list = ['mothernaturenet', 'greenbiz', 'wwf', 'africanconserve', 'landintegrity', 'nature_org', 'nrdc', 'greenpeace',
'epa'];


#labels
label = ["ID"];



#i is the position of account in the array
i = 0;

#for each line in twitter_list
for account in twitter_list:

	#open the corresponding file
	#add to label
	account = account.rstrip();	
	label.append(account);
	follower_list = open((account + ".txt"), "r");	
	#for each follower of account
	for follower in follower_list:
		follower = follower.rstrip();
		#if this follower is new, add them to aggregate_followers
		if (follower not in aggregate_followers): 
			aggregate_followers[follower] = [0]*9;
		#mark the follower as following account's twitter
		aggregate_followers[follower][i] = 1;
	follower_list.close();
	i+= 1;
	
print("ok.");
#print(aggregate_followers);

#put into text file
output = open("tableSMALL.txt", "w");
#print labels
for name in label:
	output.write(name + "\t");
#output.write("\n");
for x in aggregate_followers:
	thing = str(x) + "\t";
	for y in aggregate_followers[x]:
		thing += str(y) + "\t"
	#print(thing)
	output.write("\n" + thing);