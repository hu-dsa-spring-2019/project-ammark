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
##print(book_data) 

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
            if x!=():
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
##print(user_data)

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

#name=input('Your name?')

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
    print(Final[-1]+'.')
    return Final
#b=GetMeADuo(G,name)

genre_output = ''
def recommend_genre(bookdata,name,c):
    global genre_output
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
    genre_output = rec
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

top_picks_display = ''

def show_top_picks(G, name, book_data):    
    global top_picks_display
    top_picks_display = ''
    picks = top_picks(G, name)
    output = []
    for entry in picks:
        output.append((entry, book_data[entry]))
    
    top_picks_display = output



def display_main():
    global G
    global book_data
    window1 = Tk()
    window1.title('Book Butler')

    inputframe = LabelFrame(window1, width = 500, height = 300)
    inputframe.pack()

    outputframe = LabelFrame(window1, width = 500, height = 200)
    outputframe.pack()

    text_prompt = Label(inputframe, text = 'Enter your name:')
    text_prompt.place(relx = 0.2, rely= 0.2, anchor = 'center')
    
    Entry1 = Entry(inputframe, bd = 3, width = 25)
    Entry1.place(relx = 0.5, rely = 0.2, anchor = 'center')
    

    Addbutton = Button(inputframe, text = 'Add a new user', anchor = 'center')
    Addbutton.place(relx = 0.2, rely = 0.5)

    Bytaste_button = Button(inputframe, text = 'Top Picks for You', anchor = 'center', command=lambda: show_top_picks(G, Entry1.get(), book_data))
    Bytaste_button.place(relx = 0.4, rely = 0.5)

    Bygenre_button = Button(inputframe, text = 'Books of similar genre',anchor = 'center', command = lambda: recommend_genre(book_data, Entry1.get(), user_data))
    Bygenre_button.place(relx = 0.63, rely = 0.5)
    
    textout1 = StringVar()
    textout2 = StringVar()

    toppicklabel = Label(outputframe, text= '123')
    toppicklabel.place(relx = 0.2, rely = 0.4, anchor = 'center')
    topgenrelabel = Label(outputframe, text= '555')
    topgenrelabel.place(relx = 0.6, rely = 0.4, anchor = 'center')

    toppicklabel.configure(text=top_picks_display)
    topgenrelabel.configure(text=genre_output)

    window1.mainloop()
##display_main()
new_user_data=[]
def save_new_entries():
    global new_user_data
    new_user_name=input('Enter name of the new member.')
    new_user_books=eval(input('Enter the books you have read from the library, in the form of list, and with book name, type True if you liked it, else False.'))
    new_user_data=[new_user_name]
    for x in new_user_books:
        new_user_data.append(x)


#we will use the function, save_new_entries via GUI and the use the function, Add_to_records to save every new record from save_new_entry into the Userdata.csv file.       
def New_User(datafile,new_user_data):  #datafile is the Userdata.csv file
    import csv
    with open(datafile, 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(new_user_data)
##New_User(datafile,new_user_data)



def Add_to_records(datafile):
    global new_user_data
    save_new_entries()
    choice=input('Do you want to save all new enteries into the records? Yes/No')
    if choice=='Yes':
        New_User(datafile,new_user_data)
Add_to_records(datafile)






















































