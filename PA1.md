# 2. In this markdown, provide a short description of the approach you used to solve the problem.

The approach I used in this assignment firstly I alligned the sequences index by index and store it in a variable and then compare them and calculate the score. And for maximum contiguous chain I store the indexes whre theses sequences are matched and with the help of that indexes I checked whether the matched sequence is contiguous or not. 

# 3. List the source code, and a list of at least one example per approach, along with the contents of the file you used:

## Code:

```python




from curses.ascii import NUL


#DNS similarity class
class DNSSemilarity:

    def __init__(self,s1,s2,shift):
        #member variable
        # 
        # sequences variable 
        self.seq1=s1
        self.seq2=s2

        # max score
        self.max_score=0
        self.max_shift=shift

        #all contignous chain list
        self.continous_chain=list()
        self.contigous_chain_list=list()

        #score list
        self.score_list=list()


    #calculate the max contiguous chain for approach two
    def fetchContigousChain(self,seq1,seq2):

        self.continous_chain=list()
        index_chain=list()
        try:
            for i in range(0,len(seq1)):
            
                if(seq1[i]==seq2[i]):
                    
                    index_chain.append(i)
        except NameError:
            raise


        try:
            for i in range(0,len(index_chain),2):
                if i+1 <len(index_chain):

                    if(index_chain[i+1]-(index_chain[i])==1):
                        self.continous_chain.append(seq1[index_chain[i]])
                        self.continous_chain.append(seq1[index_chain[i+1]])
                    
        except NameError:
            raise

        

        




    #calculate score for the approach one
    def scoreCalculation(self,sq1,sq2):


        score=0
        
        for i in range(0,len(sq1)):
            if sq1[i]==sq2[i]:
                score+=1
            
        
        return score



    # for alignment of the sequences s1 and s2 are alignement axis s1 indicate the string number
    #  and s2 indicate the number of indexes to be aligned


    def DoAllignment(self,s1,s2):

        seq3=''
        seq4=''
        try:
            if s1==0:

                
                for i in range(0,s2):
                    seq3+='-'
                
                seq4+=self.seq2
                seq4+=seq3

                seq3+=self.seq1
                

                

            elif s1==1:
                for i in range(0,s2):
                    seq4+='-'
                
                seq3+=self.seq1
                seq3+=seq4

                seq4+=self.seq2

        except NameError:
                raise 

        return seq3,seq4


    #comparing two sequences algorithm 
    def compareSequences(self):

        try:
            if len(self.seq1)>self.max_shift:
                shift_possible=self.max_shift
            else:
                shift_possible=len(self.seq1)

        except NameError:
                    raise 
            
        Aseq1=[]
        Aseq2=[]

        # range(0,2) because there will be two sequences and it will execute for both strings like
        #(0,0)
        #(0,1)
        #(0,2)
        #(1,0)
        #(1,1)
        #(1,2)

        for i in range(0,2):
            for j in range(0,shift_possible):
                #make allignment by passing i and j. i will be sequence number and j will be the index to be alligned
                sq1,sq2=self.DoAllignment(i,j)
                
                self.score_list.append(self.scoreCalculation(sq1,sq2))
                Aseq1.append(sq1)
                Aseq2.append(sq2)

                self.fetchContigousChain(sq1,sq2)
                
                self.contigous_chain_list.append(self.continous_chain)
                        

        choice=input("Enter approach you want to choose:\nmax score or max chain : ")


        if choice=="max score":

            self.max_score=max(self.score_list)
            print("Max Score: ",self.max_score)
            print("Found at the following sequences: ")
            print(Aseq1[self.score_list.index(max(self.score_list))])
            print(Aseq2[self.score_list.index(max(self.score_list))])

            

        elif choice=="max chain":

            max_list=max(self.contigous_chain_list)
            
            print("Max chain : ",max_list)
            print("Found at the following sequences: ")
            print(Aseq1[self.contigous_chain_list.index(max(self.contigous_chain_list))])
            print(Aseq2[self.contigous_chain_list.index(max(self.contigous_chain_list))])
            

        

    def printSequences(self):
        print("Sequence 1-> ",self.seq1)
        print("Sequence 2-> ",self.seq2)
    
        

    
def main():
    file1=input("Enter file 1 name: ")
    file2=input("Enter file 2 name: ")

    #read both files and store sequences in variables

    f = open(file1, "r")
    seq1=f.read()
    f.close()

    f = open(file2, "r")
    seq2=f.read()
    f.close()


    #call constructor
    DNS=DNSSemilarity(seq1,seq2,int(input("Enter Max Shift: ")))

    #print sequences
    DNS.printSequences()


    try:
        if len(seq1)!=len(seq2):
            print("both sequences have different size")
        
            exit()
    except NameError:
        raise 

    #call compare funcion
    DNS.compareSequences()    

if __name__ == "__main__":
    main()
```

## file1.txt
```
ACTGATCAC
```

## file2.txt
```
TTAGCTCGA
```

# 4. Discuss the hurdles and benefits of developing each approach, and how did you handle them:

The hurdle I face by implementing approaches are below:
Max score:
This approach is simple in this task I just compare aligned sequence one after the other.

Maximum contiguous Chain:
To implement this task I face some difficulty because I have to find contiguous chain between two sequences one after the other. Initially it looks hard but at the end I solve the problem by doing dry run and then implement the algorithm.

