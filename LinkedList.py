class N:
    def __init__(self, datav = None):
        self.datav = datav
        self.nextv = None

class LL:
    def __init__(self):
        self.headv = None

    def printlist(self):
        printv = self.headv
        while printv is not None:
            print(printv.datav)
            printv = printv.nextv

    def AtBegining(self,newv):
        NewN = N(newv)

# Update the new nodes next val to existing node
        NewN.nextv = self.headv
        self.headv = NewN

# Add nodes to the end
    def AtEnd(self,newv):
        NewN = N(newv)
        if self.headv is None:
            self.headv = NewN
            return
        laste = self.headv
        while(laste.nextv):
            laste = laste.nextv
        laste.nextv = NewN

    def InBetween(self,middle_node,newv):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewN = N(newv)
        NewN.nextv = middle_node.nextv
        middle_node.nextv = NewN

# Function to remove Nodes
"""
    def RemoveNode(self, Removekey):

        HeadVal = self.head

        if(HeadVal is not None):
            if(HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while(HeadVal is not None):
            if HeadVal.data == Removekye:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if(HeadVal == None):
            reutnr

        prev.next = HeadVal.next

        HeadVal = None
"""
        
        
List_Number_One = LL() # Create function member LL
List_Number_One.headv = N("Mon")
e2 = N("Tue")
e3 = N("Wed")

List_Number_One.headv.nextv = e2
e2.nextv = e3

List_Number_One.AtBegining("Sun") # Beginning
List_Number_One.AtEnd("Thu") # End
List_Number_One.InBetween(List_Number_One.headv.nextv,"Fri") # Between

List_Number_One.printlist() # Print list
