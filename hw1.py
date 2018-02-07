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
story = story.replace("fish","{1}")
story = story.replace("tiger","{2}")
print("1.B. Replace \"tiger\" and \"fish\" with a format symbol and print the story again\n")
print(story)
print("1.C. Create tupple with words \"tiger\" and \"fish\" and restore the story to its original condition. Display:\n")
t1=("fish","tiger")
#story.format(1=t1[0],2=t1[1]) ask whether is it ok to use python 3 format
print(story)
story = story.replace("%(1)s",t1[1])
story = story.replace("%(2)s",t1[0])
print(story)
print("1.D. Change from \"tiger\" and \"fish\" to \"monkey\" and \"bananas\":")
t2=("monkey","bananas")
story = story.replace(t1[0],t2[0])
story = story.replace(t1[1],t2[1])
print(story)

print("2.A. Change from \"monkey\" to \"%(animal)s\" , \"bananas\" to \"%(food)s\" and \"NYC\" to \"%(city)s\":\n")

story.replace("monkey","%(animal)s")
story.replace("bananas","%(food)s")
story.replace("NYC","%(city)s")
print(story)

myDict={"animal":"cat","food":"mice","city":"Beijing"}
print("The dictionary is" +str(myDict)+"\n")

