#bookfilename=input('Enter the excel file name here (csv) for the book data file.')
bookfilename='Booklist.csv'
def openbookfile(name):
    import csv
    with open(name) as csv_file:
        x=csv.reader(csv_file)
        d=tuple()
        F=[]
        for y in x:
            for z in y:
                d+=(z,)
            F.append(d)
            d=tuple()
        bookdict={}
        for x in F:   
            bookdict[x[0]]=[x[2].split(','),x[1],x[3]]
    return bookdict
##print(openbookfile(bookfilename))

def addNodes(G, nodes):
    for item in nodes:
        G.update({item : []})
    return


def userdataload(name):
    import csv
    with open(name) as csv_file:
        x=csv.reader(csv_file)
        d=tuple()
        F=[]
        for y in x:
            for z in y:
                d+=(z,)
            F.append(d)
            d=tuple()   
        bookdict2={}
        for x in F:    
            final={}
            for y in range(len(x)):
                if y!=0:
                    M=x[y].split(',')
                    o=M[1]
                    final[M[0]]=eval(o)
            bookdict2[x[0]]=final
        return bookdict2

datafile='Userdata.csv'
user_data=userdataload(datafile)


def addEdges(G, edges, directed=False):
    for i in range(len(edges)):
        for key in G.keys():
            if key == edges[i][0]:
                if not directed:
                    G[key] += (edges[i][1:],)
                    G[edges[i][1]] += (edges[i][:1]+edges[i][2:],)
                    break
                else:
                    G[key] += (edges[i][ 1:],)
                    break
    return

def WeightedEdge_Create(datadict):
    final_lst=[]
    alrdy_traversed = [] 
    for person in datadict.keys():
        alrdy_traversed.append(person)
        books_read=datadict[person]
        for neighbor in datadict.keys():
            weight=0
            if neighbor in alrdy_traversed:
                continue
            for n_books in datadict[neighbor].keys():
                if n_books in books_read.keys():
                    currentchoice=books_read[n_books]
                    neighborchoice=datadict[neighbor][n_books]
                    if currentchoice==neighborchoice:
                        weight+=1
                    else:
                        weight-=1
            final_lst.append((person, neighbor, weight))

    return final_lst

a = WeightedEdge_Create(user_data)
#print(a)


G = {}

def create_adjlst(G):
    pass

name=input('Your name?')
def GetMeADuo(a,name):
    Final=[]
    for x in a:
        if x[0]==name and x[2]>0:
            Final.append(x[1])
        elif x[1]==name and x[2]>0:
            Final.append(x[0])
    if Final==[]:
        print('You have no matches :c')
    else:    
        print('You should start hanging out with,')
    for x in Final:
        print(x)
    return Final
b=GetMeADuo(a,name)

