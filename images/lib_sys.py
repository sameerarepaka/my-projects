from collections import Counter,namedtuple,OrderedDict,defaultdict,deque
Books=namedtuple('Book', ['book_id','title','author'])
book_copies=Counter()
borrow_history=defaultdict(deque)
new_arrivals=OrderedDict()
vip_requests=deque()

def add_Book(book_id,title,author,copies=1):
    if book_copies[book_id]==0:
        book_copies[book_id]+=copies
        new_arrivals[book_id]=Books(book_id,title,author)
    else:
        book_copies[book_id]+=copies
    print(f"{book_id} is added to the library.")

def issue_Book(book_id,user_id):
    if book_copies[book_id]>0:
        book_copies[book_id]-=1
        borrow_history[user_id].appendleft(book_id)
        if len(borrow_history[user_id])>3:
            borrow_history[user_id].pop()
        print(f"{book_id} is issued to {user_id}.")
    else:
        print("Sorry! Book is unavailable.")

def return_Book(book_id,user_id):
    book_copies[book_id]+=1
    print(f"{book_id} is returned to the library.")

def prior_requests(user_id,book_id):
    vip_requests.append((user_id,book_id))
    while vip_requests:
        book_id,user_id=vip_requests.popleft()
        if book_copies[book_id]>0:
            book_copies[book_id]-=1
            borrow_history[user_id].appendleft(book_id)
            if len(borrow_history[user_id])>3:
                borrow_history[user_id].pop()
            print(f"{book_id} is issued to VIP user {user_id}.")
        else:
            print("Sorry! Book is unavailable.")
            
def display():
    common={}
    for user_id in borrow_history:
        borrowed_Books=Counter(borrow_history[user_id])
        for book_id in borrowed_Books:
            if book_id in common:
                common[book_id]+=1
            else:
                common[book_id]=1
    sorted_common=OrderedDict(sorted(common.items(), key=lambda x:x[1],reverse=True))
    print("Topmost borrowed books are:")
    print(list(sorted_common)[:2])
    user=input("Enter user id for browser history:")
    print(f"Borrow history of {user}:")
    print(borrow_history[user])
    print("New Arrivals in library:")
    for book_id, book in new_arrivals.items():
            print(f"{book_id}: {book.title} by {book.author}")