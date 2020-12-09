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
                #print(value,cur_node,cur_node.value)
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

                #print(outputdataname)
                #file1.write(cur_node.value[0]+"\n")
            self._print_name(cur_node.right_child,empname,file1,outputdataname)
        #print("op",outputdataname)
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
                #file1.write(cur_node.value[0] +", "+str(cur_node.value[1])+ "\n")
            self._print_designation(cur_node.right_child, empdeg, file1,outputdatadeg)
        return outputdatadeg

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None: return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value[1]:
            return cur_node
        elif value < cur_node.value[1] and cur_node.left_child != None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value[1] and cur_node.right_child != None:
            return self._find(value, cur_node.right_child)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):

        ## -----
        # Improvements since prior lesson

        # Protect against deleting a node not found in the tree
        if node == None or self.find(node.value) == None:
            #print("Node to be deleted not found in the tree!")
            return None

        ## -----

        # returns the node with min value in tree rooted at input node
        def min_value_node(n):
            current = n
            while current.left_child != None:
                current = current.left_child
            return current

        # returns the number of children for the specified node
        def num_children(n):
            num_children = 0
            if n.left_child != None: num_children += 1
            if n.right_child != None: num_children += 1
            return num_children

        # get the parent of the node to be deleted
        node_parent = node.parent

        # get the number of children of the node to be deleted
        node_children = num_children(node)

        # break operation into different cases based on the
        # structure of the tree & node to be deleted

        # CASE 1 (node has no children)
        if node_children == 0:

            # Added this if statement post-video, previously if you
            # deleted the root node it would delete entire tree.
            if node_parent != None:
                # remove reference to the node from the parent
                if node_parent.left_child == node:
                    node_parent.left_child = None
                else:
                    node_parent.right_child = None
            else:
                self.root = None

        # CASE 2 (node has a single child)
        if node_children == 1:

            # get the single child node
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child

            # Added this if statement post-video, previously if you
            # deleted the root node it would delete entire tree.
            if node_parent != None:
                # replace the node to be deleted with its child
                if node_parent.left_child == node:
                    node_parent.left_child = child
                else:
                    node_parent.right_child = child
            else:
                self.root = child

            # correct the parent pointer in node
            child.parent = node_parent

        # CASE 3 (node has two children)
        if node_children == 2:
            # get the inorder successor of the deleted node
            successor = min_value_node(node.right_child)

            # copy the inorder successor's value to the node formerly
            # holding the value we wished to delete
            node.value = successor.value

            # delete the inorder successor now that it's value was
            # copied into the other node
            self.delete_node(successor)

    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def searchname(self, value):
        if self.root != None:
            return self._search_name(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        #print(value,cur_node)
        if value == cur_node.value[1]:
            #print("into if")
            opdata=str(cur_node.value[0])
            return opdata
        elif value < cur_node.value[1] and cur_node.left_child != None:
            #print("into elif value <")
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value[1] and cur_node.right_child != None:
            #print("into elif value >")
            return self._search(value, cur_node.right_child)
        return "not found"

    def _search_name(self, value, cur_node):
        print(value,cur_node)

        if value in cur_node.value[0]:
            print("into if")
            opdata=str(cur_node.value[0])
            return opdata
        elif value < cur_node.value[0] and cur_node.left_child != None:
            print("into elif value <")
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value[0] and cur_node.right_child != None:
            print("into elif value >")
            return self._search(value, cur_node.right_child)
        return "not found"

    def read_alldata(self):
        f = open("abc_emp_dataPS13.txt", "r")
        for x in f:
            chunks = x.split(',')
            # print(chunks)
            empdata = [chunks[0], int(chunks[1].strip()), chunks[2].strip()]
            # print(empdata)
            # node = {"Name"+chunks[0],"Employee Number:"+chunks[1].strip(),"Employee Designation:"+chunks[2].strip()}
            tree.insert(empdata)

    def read_prompts_data(self):
        f = open("promptsPS13.txt", "r")
        file1 = open("outputPS13.txt", "w")
        outputdataid=[]
        outputdataname = []
        outputdatadeg = []
        for x in f:
            if x != None:
                result = re.match(r"Search.*:", x)
                if (result.group() == "Search ID:"):
                    #print(int(x[11:]))
                    empname= tree.search(int(x[11:]))
                    #print(empid,type(empid))
                    #print(empname,empid)
                    opdata=str(int(x[11:]))+" "+empname+"\n"
                    outputdataid.append(opdata)
                    #file1.write(opdata)
                elif (result.group() == "Search Name:"):
                    outputdataname.append(x)
                    dataname=tree.print_name(x[13:-1],file1,outputdataname)
                    #print("opname",dataname)
                elif (result.group() == "Search Designation:"):
                    outputdatadeg.append(x)
                    datadeg = tree.print_designation(x[20:-1],file1,outputdatadeg)
                    #print(datadeg)
                #print(x[20:-1])
        file1.write("------------- Search by ID ---------------\n")
        for iddata in outputdataid:
            file1.write(iddata)

        for namedata in outputdataname:
            result = re.match(r"Search Name:.*", namedata)
            if(result):
                #print(result.group())
                file1.write("------------------------------------------------------------ Search by Name: " + result.group()[13:] + "  -----------\n")
            else:
                file1.write(namedata)
        for degdata in outputdatadeg:
            result = re.match(r"Search Designation:.*", degdata)
            if(result):
                #print(result.group())
                file1.write("------------------------------------------------------------- List Employees by Designation: " + result.group()[20:] + "  -----------\n")
            else:
                file1.write(degdata)

        file1.close()


tree = binary_search_tree()

tree.read_alldata()
#tree.print_tree("Rajesh")
tree.read_prompts_data()
#print(tree.search(1004))
# tree.insert(['Rajesh Sharma',1004, ' CEO\n'])
# tree.insert(['Rajesh Sharma',1003, ' CEO\n'])
# tree.insert(['Rajesh Sharma',1005, ' CEO\n'])
# tree.insert(['Rajesh Sharma',1001, ' CEO\n'])
# tree.insert(['Rajesh Sharma',1000, ' CEO\n'])
# print(tree.height())
# print(tree.find(1005).value)

# f = open("abc_emp_dataPS13.txt", "r")
# tree = binary_search_tree()
# for x in f:
#   #print(x)
#   chunks = x.split(',')
#   #print(chunks)
#   empdata= [chunks[0],int(chunks[1].strip()),chunks[2].strip()]
#   #print(empdata)
#   #node = {"Name"+chunks[0],"Employee Number:"+chunks[1].strip(),"Employee Designation:"+chunks[2].strip()}
#   tree.insert(empdata)

#print(tree.height())
#print(tree.search(1004))