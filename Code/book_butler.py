from tkinter import *


#bookfilename=input('Enter the excel file name here (csv) for the book data file.')
##bookfilename='"C:\\Users\\Sony_i3\\Documents\\GitHub\\project-ammark\\Code\\Booklist.csv'
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
book_data=openbookfile(bookfilename)

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
##datafile= 'C:\\Users\\Sony_i3\\Documents\\GitHub\\project-ammark\\Code\\Userdata.csv'
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
            if weight != 0:
                final_lst.append((person, neighbor, weight))

    return final_lst

edge_list = WeightedEdge_Create(user_data)
##print(edge_list)


G = {}

def create_adjlst(G):
    addNodes(G, user_data.keys())
    addEdges(G,edge_list)
    return

create_adjlst(G)

name=input('Your name?')

def GetMeADuo(G,name):
    Final=[]
    a=G[name]
    t=0
    for x in a:
        if x[1]>t:
            Final.append(x[0])
            t=x[1]
    if Final==[]:
        print('You have no match :c')
    else:
        print('Your highest duo score is with ',end='')
    print(Final[0]+'.')
    return Final
#b=GetMeADuo(G,name)

def recommend_genre(bookdata,name,c):
    userbooks=c[name]
    for x,y in userbooks.items():
        if y==True:
            genre=bookdata[x][0]
            author=bookdata[x][1]
            price=bookdata[x][2]
            rec=[]
            for gen in genre:
                for i,j in bookdata.items():
                    if gen in j[0] and i not in rec and i!=x:
                        rec.append((i,j[2]))
            print('because you have read '+str(x)+' and liked it,we recommend you to read: ')
            for x in rec:
                print(x[0],' at the price ',x[1])
#recommend_genre(book_data,name,user_data)

def top_picks(G, name):
    global user_data
    links = G[name]
    counter = 0
    toplist = []                          #list maintained to track best edges
    
    while counter <2:
        maxval = 0
        max_index = None
        for person in range(len(links)):
            if links[person][1] > maxval:
                maxval = links[person][1]
                max_index = person
        if max_index:
            toplist.append(links.pop(max_index)[0])
            counter +=1
        else:
            break
    
    recommendation = []
    
    for connection in toplist:
        read_books = user_data[connection]
        for book in read_books.keys():
            if book not in user_data[name].keys() and read_books[book]:
                recommendation.append(book)

    return recommendation

def show_top_picks(G, name, book_data):    
    picks = top_picks(G, 'Ammar Khan')
    output = []
    for entry in picks:
        output.append((entry, book_data[entry]))
    
    return output

def display_main():
    window1 = Tk()
    window1.title('Book Butler')

    inputframe = LabelFrame(window1, width = 500, height = 300)
    inputframe.pack()

    outputframe = LabelFrame(window1, width = 500, height = 200)
    outputframe.pack()

    Entry1 = Entry(inputframe, bd = 3)
    Entry1.place(relx = 0.5, rely = 0.2)

    Addbutton = Button(inputframe, text = 'Add a new user')
    Addbutton.place(relx = 0.2, rely = 0.5)

    Bytaste_button = Button(inputframe, text = 'Top Picks for You')
    Bytaste_button.place(relx = 0.5, rely = 0.5)

    Bygenre_button = Button(inputframe, text = 'Books of similar genre')
    Bygenre_button.place(relx = 0.8, rely = 0.5)
    
    Output_txt = Label()
    
    
    
    window1.mainloop()

show_top_picks(G, name, book_data)




























































