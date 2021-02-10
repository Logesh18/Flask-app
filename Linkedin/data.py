from pymongo import MongoClient

def data():
    
    client = MongoClient('Your Mongodb File') #link of atlas
    db = client['LinkedIn']
    doc = db['reco']
    l = list(doc.find({}))
    
    return l

def search(pn , rn):
    client = MongoClient('Your Mongodb File')#link of atlas
    db = client['LinkedIn']
    doc = db['reco']
    
    if pn == '':
        a = doc.create_index([('Receiver_Name','text')])
        myquery = {'$text':{'$search':rn}}
        l = list(doc.find(myquery))
        doc.drop_index(a)
    elif rn == '':
        a = doc.create_index([('Provider_Name','text')])
        myquery = {'$text':{'$search':pn}}
        l = list(doc.find(myquery))
        doc.drop_index(a)
    else:
        myquery = { "Provider_Name": pn ,"Receiver_Name": rn}
        l = list(doc.find(myquery))
    return l


   # j = doc.find( {'$text':{'$search':'csp'}}) 
def findpage(page,dataset,limit=10):
    '''
    page: which page no
    dataset: list(dict()) data
    limit : how much data want
    '''
    end = (page * limit)
    start =  end - limit
    
    print("Start PageData :",start,"End PageData :",end)
    length = len(dataset)
    pg,r=divmod(length ,limit)
    if(r>0):
        pg += 1
    '''
    startofpage = dataset[start]['_id']
    if end < length:
        endofpage = dataset[end -1]['_id']
    else:
        endofpage = dataset[length-1]['_id']'''
    
    if end <= length:
        return(dataset[start:end] , start , end , pg)
    else:
        return(dataset[start:] , start , end , pg)
