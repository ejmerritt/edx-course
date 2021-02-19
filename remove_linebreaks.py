import os
os.chdir("/Users/academic/Documents/Code/EdX_Research/Case Studies Lessons")

def remove_linebreaks(filepath):
  file = open(filepath, "r+")
  text = file.read()
  text = text.replace("\r", " ")
  text = text.replace("\n", " ")
  file.truncate(0)
  file.write(text)
  file.close()

remove_linebreaks("333 Majority Vote.txt")
