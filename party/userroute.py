import re,random,os,requests,json
from flask import render_template,request,redirect,flash,make_response,session,url_for
from sqlalchemy.sql import text
from party import app, csrf
from party.models import db,Donation,User

# from party.forms import 

@app.route("/index")
def user():
    return render_template("index.html")


@app.route("/booking")
def booking():
    return render_template("book.html")




@app.route("/donate", methods=['POST','GET']) 
def donation():
    useronline =session.get('userid')
    userdeets =db.session.query(User).get(useronline)
    if request.method == 'GET':
        return render_template("donation.html", userdeets=userdeets)
    else:
        #retrieve form data
        fullname = request.form.get("fullname")
        email = request.form.get('email')
        amount = request.form.get('amount')
        
        if fullname=="" or email=="" or amount=="":
            flash("fields cannot be empty")
            return render_template("donation.html")
        # if request.form.get('userid') =="":
        #     userid = None
        else:
           userid = request.form.get('userid')
        refno = int(random.random()*100000000)
        #create a new donation instance
        don = Donation(don_amt=amount,don_userid=userid,don_fullname=fullname,don_email=email,don_refno=refno,don_status='pending')
        db.session.add(don)
        db.session.commit()
        #save the refno in a session so that we can retrieve the details on the next page
        session['ref'] = refno
        return redirect("/payment")
    

@app.route("/payment")
def make_payment():
    userdeets = db.session.query(User).get(session.get('userid'))
    if session.get('ref') !=None:
        ref = session['ref']
         #TO DO: we want to get the details of the transaction and display to the user
        trxdeets = db.session.query(Donation).filter(Donation.don_refno==ref).first()
        return render_template("payment.html", trxdeets=trxdeets,userdeets=userdeets)
    else:
        return redirect("/donate")
    

@app.route("/paystack", methods=["POST"])
def paystack():
    if session.get('ref') !=None:
        ref = session['ref']
        trx =db.session.query(Donation).filter(Donation.don_refno==ref).first()
        email = trx.don_email
        amount = trx.don_amt
        #we want to connect to paystack api
        url = "https://api.paystack.co/transaction/initialize"
        headers ={"Content-Type":"application/json","Authorization":"Bearer sk_test_ea189b33e8fcd1473fdf44fc88fd2fe646e25dad"}
        data = {"email":email, "amount":amount*100,"reference":ref}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        rspjson = response.json()
        if rspjson['status'] ==True:
            paygateway = rspjson['data']['authorization_url']
            return redirect(paygateway)
        else:
            return rspjson
    else:
        return redirect("/donate")




@app.route("/landing")
def  paystack_landing():
    ref = session.get('ref')
    if ref ==None:
        return redirect("/donate")
    else:
        headers={"Content-Type":"application/json","Authorization":"Bearer sk_test_ea189b33e8fcd1473fdf44fc88fd2fe646e25dad"}
        verifyurl= "https://api.paystack.co/transaction/verify/"+str(ref)
        response= requests.get(verifyurl,headers=headers)
        rspjson=json.loads(response.text)
        if rspjson['status']== True: #payment was successful
            return rspjson
        else:  #payment was not successful
            return "payment was not successful"
    