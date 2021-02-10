from flask import Flask,render_template,request,url_for,redirect
from colorama import Fore, Back, Style 
from data import data,search,findpage
app = Flask(__name__ )

global l 
l = data()

page =1

@app.route('/search/')

def search1():     
    
    print(Style.DIM + "inside GET")
    print(Style.RESET_ALL)
    pn = request.args.get('pn')
    print(Fore.RED +"Provider : "+pn)
    print(Style.RESET_ALL) 
    rn = request.args.get('rn')
    print(Fore.RED +"Reciver : "+rn)
    page1 = int(request.args.get('page') )
    print(Style.RESET_ALL)
    global l1
    l1 = search(pn,rn)
    l2,p,s,e,next,pre,page = give(page1,l1)
    ######################################################
    if page1 > p or page1 <= 0:
        return render_template('404.html',v='Something Wrong')
    ##########################################################
    else:
        
        return render_template('table.html',l=l2,p=p,start1=s,end1=e,next = next,pre=pre ,active1 = page,url = 'search1')
    

@app.route('/search1/')
def sample():
    page1 = int(request.args.get('page'))
    
    l2,p,s,e,next,pre,page = give(page1,l1)
    print("Total pages:",p)
    ######################################################
    if page1 > p or page1 <= 0:
        return render_template('404.html',v='Something Wrong')
    ##########################################################
    else:
        return render_template('table.html',l=l2,p=p,start1=s,end1=e,next = next,pre=pre ,active1 = page,url = 'search1')
    
@app.errorhandler(500)
def internal(e):
    return render_template('404.html',v='Problem occured')
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html',v='Not found')
  

def give(page,l2):
    
    l2 , s ,e , p = findpage(page,l2,limit=10)
    
    if page == 1 and page == p:
        pre = 1
        
        next = 1

    elif  page == 1:
        pre = p
        next = page + 1

    elif page == p:
        
        next = 1
        pre = p-1
        
    else:
        next = page + 1
        pre = page -1

    print(request.path)
    print("Start Page data :",s,"endpage data1:",e)
    return l2,p,s,e,next,pre,page
    


@app.route('/pyhackons/')
def pyhackons():
    return render_template('pyhackons.html')

@app.route('/')
def home():
    
    l2,p,s,e,next,pre,page = give(1,l)
    return render_template('table.html',l=l2,p=p,start1=s,end1=e,next = next,pre=pre ,active1 = page ,url='table')

@app.route('/table/')
def table():
    
    page1 = int(request.args.get('page'))
    l2,p,s,e,next,pre,page = give(page1,l)
    print("Total pages:",p)
    ######################################################
    if page1 > p or page1 <= 0 :
        return render_template('404.html',v='Something Wrong')
    ##########################################################
    else:
        return render_template('table.html',l=l2,p=p,start1=s,end1=e,next = next,pre=pre ,active1 = page,url='table')

if __name__ == '__main__':
    print(Fore.RED + 'Start')
    print(Style.RESET_ALL)
    app.run(host = '0.0.0.0')
