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
            d=tuple()   #After this, csv file is stored in a list of nested lists.
        bookdict={}
        for x in F:     #Used to create a dictionary of desired format.
            bookdict[x[0]]=[x[2].split(','),x[1],x[3]]
    return bookdict

    
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
                        weight+=2
                    else:
                        weight+=1
            if weight > 0:
                final_lst.append((person, neighbor, weight))

    return final_lst

def addNodes(G, nodes):
    for item in nodes:
        G.update({item : []})
    return


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

G = {'A':{1: True, 2:True, 5: False},
'B':{2:False, 1: False, 5:False}
}
a = WeightedEdge_Create(G)
print(a)
