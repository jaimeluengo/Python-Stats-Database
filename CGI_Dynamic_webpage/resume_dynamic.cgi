#!/usr/bin/python

''' Program to take input from a webpage and using cgi, format another template
webpage with this input. This program works for two types of data structures used
for formatting and methods getfirst and get value. So in total there are 4 methods to
parse the input into a formatting data structure:
- getDictFirst
- getDictValue
- getTupleFirst
- getTupleValue
The tuple methods have not been tested. Tuple methods required an html file with simple
formatting %s, whereas dictionary requires the key of each element in the formatting
%(key)s.
Dictionary is a more natural data structure used for this problem since the fields
that need to be format are equivalent to the keys of the dictionary and easy to reuse
and mantain without having to count the indexes , as in the tuple. Also getfirst is
more robust against not valid input than getvalue(), but less direct '''

import cgi

def main():
    form = cgi.FieldStorage()
    Fields = getDictValue(form)
			 
    newPage = makePage('resume.html',Fields) #resume2 for tuple and resume for dict
    
    print(newPage)

def getDictFirst(form):
    firstName = form.getfirst("firstName","")
    LastName = form.getfirst("LastName","")
    PhoneNumber = form.getfirst("PhoneNumber","")
    Email = form.getfirst("Email","")
    ResidentialAddress = form.getfirst("ResidentialAddress","")
    CurrentUniversity = form.getfirst("CurrentUniversity","")
    CurrentMajor = form.getfirst("CurrentMajor","")
    Skills = form.getfirst("Skills","")
    CareerInterests = form.getfirst("CareerInterests","")
    UndergradMajor = form.getfirst("UndergradMajor","")
    UndergradUniversity = form.getfirst("UndergradUniversity","")
    UndergradAddress = form.getfirst("UndergradAddress","")

    #Dictionary that has  as keys the name of the fields and values the values of these fields
    Fields ={'firstName':firstName,'LastName':LastName,'PhoneNumber':PhoneNumber,
             'Email':Email,'ResidentialAddress':ResidentialAddress,
             'CurrentUniversity':CurrentUniversity,'CurrentMajor':CurrentMajor,
             'Skills':Skills,'CareerInterests':CareerInterests,
             'UndergradMajor':UndergradMajor,'UndergradUniversity':UndergradUniversity,
             'UndergradAddress':UndergradAddress}
    return Fields

def getDictValue(form):
    firstName = form.getvalue("firstName")
    LastName = form.getvalue("LastName")
    PhoneNumber = form.getvalue("PhoneNumber")
    Email = form.getvalue("Email")
    ResidentialAddress = form.getvalue("ResidentialAddress")
    CurrentUniversity = form.getvalue("CurrentUniversity")
    CurrentMajor = form.getvalue("CurrentMajor")
    Skills = form.getvalue("Skills")
    CareerInterests = form.getvalue("CareerInterests")
    UndergradMajor = form.getvalue("UndergradMajor")
    UndergradUniversity = form.getvalue("UndergradUniversity")
    UndergradAddress = form.getvalue("UndergradAddress")

    #Dictionary that has  as keys the name of the fields and values the values of these fields
    Fields ={'firstName':firstName,'LastName':LastName,'PhoneNumber':PhoneNumber,
             'Email':Email,'ResidentialAddress':ResidentialAddress,
             'CurrentUniversity':CurrentUniversity,'CurrentMajor':CurrentMajor,
             'Skills':Skills,'CareerInterests':CareerInterests,
             'UndergradMajor':UndergradMajor,'UndergradUniversity':UndergradUniversity,
             'UndergradAddress':UndergradAddress}
    return Fields

def getTupleValue(form):
    firstName = form.getvalue("firstName")
    LastName = form.getvalue("LastName")
    PhoneNumber = form.getvalue("PhoneNumber")
    Email = form.getvalue("Email")
    ResidentialAddress = form.getvalue("ResidentialAddress")
    CurrentUniveristy = form.getvalue("CurrentUniveristy")
    CurrentMajor = form.getvalue("CurrentMajor")
    Skills = form.getvalue("Skills")
    CareerInterests = form.getvalue("CareerInterests")
    UndergradMajor = form.getvalue("UndergradMajor")
    UndergradUniversity = form.getvalue("UndergradUniversity")
    UndergradAddress = form.getvalue("UndergradAddress")
    
    Tuple = (firstName,LastName,PhoneNumber,
            Email,ResidentialAddress,
            CurrentUniversity,CurrentMajor,
            Skills, CareerInterests,
            UndergradMajor, UndergradUniveristy,
            UndergradAddress)
    return Tuple

def getTupleFirst(form):
    firstName = form.getFirst("firstName","")
    LastName = form.getFirst("LastName","")
    PhoneNumber = form.getFirst("PhoneNumber","")
    Email = form.getFirst("Email","")
    ResidentialAddress = form.getFirst("ResidentialAddress","")
    CurrentUniveristy = form.getFirst("CurrentUniveristy","")
    CurrentMajor = form.getFirst("CurrentMajor","")
    Skills = form.getFirst("Skills","")
    CareerInterests = form.getFirst("CareerInterests","")
    UndergradMajor = form.getFirst("UndergradMajor","")
    UndergradUniversity = form.getFirst("UndergradUniversity","")
    UndergradAddress = form.getFirst("UndergradAddress","")
    
    Tuple = (firstName,LastName,PhoneNumber,
            Email,ResidentialAddress,
            CurrentUniversity,CurrentMajor,
            Skills, CareerInterests,
            UndergradMajor, UndergradUniveristy,
            UndergradAddress)
    return Tuple

def fileToStr(fileName):
    fin = open(fileName);
    contents = fin.read();
    fin.close;
    return contents

def makePage(templateFileName, substitutions):
    pageTemplate = fileToStr(templateFileName)
    return pageTemplate % substitutions

def strToFile(text, fileName):
    output = file(fileName, "w")
    output.write(text)
    output.close()

def browseLocal(webPageText, fileName):
    strToFile(webPageText, fileName)
    import webbrowser
    webbrowser.open(fileName)

try:
    print "content-type: text/html\n\n"
    main()
except:
    cgi.print_exception()
