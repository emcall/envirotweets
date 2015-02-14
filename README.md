This was my contribution to a group project for a class on working with big datasets. Our project's theme was Twitter and the environment, analyzing the relationships users had with environmental organizations. 

For my part, I took the twitter accounts of 40 different environmental organizations, and grabbed 5000 random followers from each. Then I put them all together to see how many of these people followed multiple organizations on my list (ie, if someone who shows up on the list for both WWF and EPA). I made a network graph to show how linked various organizations are to one another, where each string is a person who follows both. 
I have since realized this may not have been the best way to go about it; if I were to do this project today, I would instead have gone through each user pulled from the initial organizations to ensure I didn't miss any multiple follows (since it is possible users listed later than the initial 5000 pulled were on multiple follower lists). I would also have been more careful with file and variable names. I don't know why I thought "af" and "ag were acceptable names for comprehensible code (I guess I thought since I was the only one looking at it, readability didn't matter, but I don't have a clue what those were for anymore). Live and learn.

The project was completed in December of 2013. It was my first experience working with Python; I thought it would be easier to work with an unfamiliar language than to find an alternate library for accessing Twitter APIs from the one my peers were using.

