import re


class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None  # pointer to parent node in tree


class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value[1] < cur_node.value[1]:
            if cur_node.left_child == None:
                cur_node.left_child = node(value)
                cur_node.left_child.parent = cur_node  # set parent
            else:
                self._insert(value, cur_node.left_child)
        elif value[1] > cur_node.value[1]:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node  # set parent
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value already in tree!")

    def print_name(self,empname,file1,outputdataname):
        if self.root != None:
            data = self._print_name(self.root,empname,file1,outputdataname)
        return data
    def _print_name(self, cur_node,empname,file1,outputdataname):
        data=[]
        if cur_node != None:
            self._print_name(cur_node.left_child,empname,file1,outputdataname)
            if empname in cur_node.value[0]:
                outputdataname.append(cur_node.value[0]+"\n")
            self._print_name(cur_node.right_child,empname,file1,outputdataname)
        return outputdataname

    def print_designation(self, empdeg, file1,outputdatadeg):
        if self.root != None:
            data = self._print_designation(self.root, empdeg, file1,outputdatadeg)
        return data
    def _print_designation(self, cur_node, empdeg, file1,outputdatadeg):
        if cur_node != None:
            self._print_designation(cur_node.left_child, empdeg, file1,outputdatadeg)
            if empdeg in cur_node.value[2]:
                outputdatadeg.append(cur_node.value[0] +", "+str(cur_node.value[1])+ "\n")
            self._print_designation(cur_node.right_child, empdeg, file1,outputdatadeg)
        return outputdatadeg


    def print_id(self, value):
        if self.root != None:
            return self._print_id(value, self.root)
        else:
            return False

    def _print_id(self, value, cur_node):
        if value == cur_node.value[1]:
            opdata=str(cur_node.value[0])
            return opdata
        elif value < cur_node.value[1] and cur_node.left_child != None:
            return self._print_id(value, cur_node.left_child)
        elif value > cur_node.value[1] and cur_node.right_child != None:
            return self._print_id(value, cur_node.right_child)
        return "not found"

    def read_alldata(self):
        f = open("abc_emp_dataPS13.txt", "r")
        for x in f:
            chunks = x.split(',')
            empdata = [chunks[0], int(chunks[1].strip()), chunks[2].strip()]
            tree.insert(empdata)

    def print_alldata(self):
        f = open("promptsPS13.txt", "r")
        file1 = open("outputPS13.txt", "w")
        outputdataid=[]
        outputdataname = []
        outputdatadeg = []
        for x in f:
            if(x!="\n" and "Search" in x):
                result = re.match(r"Search.*:", x)
                if (result.group() == "Search ID:"):
                    if(len(x)!=11 and x[11:-1].isnumeric()):
                        empname= tree.print_id(int(x[11:-1]))
                        opdata=str(int(x[11:]))+" "+empname+"\n"
                        outputdataid.append(opdata)
                    else:
                        opdata = x[11:-1] + " Type Error\n"
                        outputdataid.append(opdata)
                elif (result.group() == "Search Name:"):
                    outputdataname.append(x)
                    tree.print_name(x[13:-1],file1,outputdataname)
                elif (result.group() == "Search Designation:"):
                    outputdatadeg.append(x)
                    tree.print_designation(x[20:-1],file1,outputdatadeg)
        file1.write("------------- Search by ID ---------------\n")
        for iddata in outputdataid:
            file1.write(iddata)

        for namedata in outputdataname:
            result = re.match(r"Search Name:.*", namedata)
            if(result):
                file1.write("-----------------------------------------------\n-------------------- Search by Name: " + result.group()[13:] + "  -----------\n")
            else:
                if(namedata):
                    file1.write(namedata)

        for degdata in outputdatadeg:
            result = re.match(r"Search Designation:.*", degdata)
            if(result):
                file1.write("-----------------------------------------------\n--------------------- List Employees by Designation: " + result.group()[20:] + "  -----------\n")
            else:
                file1.write(degdata)
        file1.write("-----------------------------------------------")
        file1.close()
        f.close()

if __name__ == '__main__':
    tree = binary_search_tree()
    tree.read_alldata()
    tree.print_alldata()