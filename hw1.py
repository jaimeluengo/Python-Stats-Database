#String formatting (Python 2.7), tuples and dictionaries
print("STSCI 4060 HW1 \nName: Jaime Luengo Rozas \nNetID: jl3752 \n***** Question 1 ***** \n"
      "This program is to manipulate a string using a format string, string methods, and a tuple.\n" 
         "\nA. Define a string variable, story, to hold the content of the story including its layout.")
story="Once upon a time, deep in an ancient \njungle, there lived a tiger. This tiger \nliked to eat fish, but the " \
      "jungle had\nvery little fish to offer. One day, an \nexplorer found the tiger and discovered \n " \
      "it liked fish. The explorer took the \n tiger back to NYC, where it could \neat as much fish as it wanted." \
      " However,\nXiaolong Yang© 2018 Page 2 of 3 \nthe tiger became homesick, so the \nexplorer brought it back to" \
      " the jungle,\nleaving a large supply of fish.\n-- The End of the Story --\n"

print("1.A. Print the story stored in String \"story\" \n")
print(story)
print(type(story))
story = story.replace("fish","%(1)s")
story = story.replace("tiger","%(2)s")
print("1.B. Replace \"tiger\" and \"fish\" with a format symbol and print the story again\n")
print(story)
print("1.C. Create tupple with words \"tiger\" and \"fish\" and restore the story to its original condition. Display:\n")
t1=("fish","tiger")
print(story % {'1':t1[0],'2':t1[1]})
#story.format(1=t1[0],2=t1[1]) ask whether is it ok to use python 3 format

#story = story.replace("%(1)s",t1[1])
#story = story.replace("%(2)s",t1[0])

print("1.D. Change from \"tiger\" and \"fish\" to \"monkey\" and \"bananas\":")
t2=("bananas","monkey")
print(story % {'1':t2[0],'2':t2[1]})
#story = story.replace(t1[0],t2[0])
#story = story.replace(t1[1],t2[1])
#print(story)

print("2.A. Change from \"monkey\" to \"%(animal)s\" , \"bananas\" to \"%(food)s\" and \"NYC\" to \"%(city)s\":\n")

story = story.replace("%(1)s","%(animal)s")
story = story.replace("%(2)s","%(food)s")
story = story.replace("NYC","%(city)s")
print(story)

print("2.B. Create a dictionary, display it, and apply to the story with the string format operator")
myDict={"animal":"cat","food":"mice","city":"Beijing"}
print("The dictionary is" +str(myDict)+"\n")
print(story % myDict)

print("3. Compute the dot product between two vectors. Show them and the result")
u=[10,-2,3,44]
v=[20,3,-2,11]
print("vector u: \n" +str(u)+ "\nvector v:\n" + str(v))

sum=0
for i in range(len(u)):
    sum=sum+v[i]*u[i]
print("\nThe resulting dot product is:\n"+str(sum))

