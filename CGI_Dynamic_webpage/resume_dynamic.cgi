#!/usr/bin/python

''' Program to take input from webpage and use it to format another
template html file '''

import cgi

def main():
    form = cgi.FieldStorage()
    FirstName = form.getvalue('FirstName')
    LastName = form.getvalue('LastName')
    PhoneNumber = form.getvalue('PhoneNumber')
    Email = form.getvalue('Email')
    ResidentialAdress = form.getvalue('ResidentialAdress')
    CurrentUniversity = form.getvalue('ResidentialAdress')
    CurrentMajor = form.getvalue('ResidentialAdress')
    Skills = form.getvalue('ResidentialAdress')
    CareerInterests = form.getvalue('ResidentialAdress')
    UndergradMajor = form.getvalue('ResidentialAdress')
    UndergradUniveristy = form.getvalue('ResidentialAdress')
    Fields ={'FirstName':FirstName,'LastName':LastName,'PhoneNumber':PhoneNumber,
             'Email':Email}
    num = range(len(theList))
    for i in num:
        theList[i] =

def proccessInput(The List):

def filetoStr(fileName):
    fin = open(fileName);
    contents = fin.read();
    fin.close;
    return contents

def makePage(TemplateFileName, substitutions):
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
    cgi.print_exception
