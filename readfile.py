import re

from main import binary_search_tree

def read_alldata():
  f = open("abc_emp_dataPS13.txt", "r")
  tree = binary_search_tree()
  for x in f:
    # print(x)
    chunks = x.split(',')
    # print(chunks)
    empdata = [chunks[0], int(chunks[1].strip()), chunks[2].strip()]
    print(empdata)
    # node = {"Name"+chunks[0],"Employee Number:"+chunks[1].strip(),"Employee Designation:"+chunks[2].strip()}
    tree.insert(empdata)
    read_prompts_data()
    # print(tree.height())
    # print(tree.find(1005).value)
    # print({"Name:"+chunks[0],"Employee Number:"+chunks[1].strip(),"Employee Designation:"+chunks[2].strip()})

def read_prompts_data():
  f = open("promptsPS13.txt", "r")
  tree = binary_search_tree()
  for x in f:
    # print(x)
    result = re.match(r"Search.*:", x)
    if(result.group()=="Search ID:"):
      print(type(int(x[11:])))
    elif(result.group()=="Search Name:"):
      print(result.group())
    elif(result.group()=="Search Designation:"):
      print(result.group())


    chunks = x.split('Search ID:')
    #print(x)
    #print(chunks)
    # empdata = [chunks[0], int(chunks[1].strip()), chunks[2].strip()]
    # print(empdata)
    # node = {"Name"+chunks[0],"Employee Number:"+chunks[1].strip(),"Employee Designation:"+chunks[2].strip()}
    #tree.insert(empdata)
    # print(tree.height())
    # print(tree.find(1005).value)
    # print({"Name:"+chunks[0],"Employee Number:"+chunks[1].strip(),"Employee Designation:"+chunks[2].strip()})
#read_alldata()
read_prompts_data()