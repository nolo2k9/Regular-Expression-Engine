import argparse
parser = argparse.ArgumentParser()
parser.add_argument("help", help= print("********************************************************************************"
"\nThis program was developed to tell you if a string is a regular expression or not. \n"
"\nYou have two options which are: \n"
"\n (1) To generate a random regular expression from a bank of premade regular expressions. \n"
"\n (2) Enter in your own regular expression and then a string which you want to compare it to. \n"
"\n The program will then inform you if the randomly generated expression or your own expression is infact a regular expression or not. \n"
"\n An example of a regular expression is A.B* BBBBBBBBBBBBBBBBB \n"
"\n Please Re-Run (python parser.py) on the command line to get started \n"
"\n*****************************************************************"))
args = parser.parse_args()
print (args.help)