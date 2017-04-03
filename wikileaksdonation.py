## ## Create a proxy object and connect to the bitcoin.rpc
import bitcoin.rpc
myproxy = bitcoin.rpc.Proxy()
## Create a proxy object and connect to the bitcoin.rpc
import bitcoin.rpc
import os
from twython import Twython

myproxy = bitcoin.rpc.Proxy()

## Grab the block
block_info = myproxy.getblock(myproxy.getblockhash(myproxy.getblockcount()))

#Setting these as variables will make them easier for future edits
app_key =  ''
app_secret = ''
oauth_token = ''
oauth_token_secret = ''

#Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#The above should just be a single line, without the break

## Declare some variables used by our search
isdonation = 0
wikiLeaks = "1HB5XMLmzFVj8ALj6mfBsbifRoD4miY36v"
wikiLeaksKey = "b169f2b0b866db05900b93a5d76345f18d3afb24" 
btcdonation = ""
btcdonationleft= ""
btcdonationright = ""

## Display what we are doing
print ("Searching for a Donation to " + wikiLeaks)

## Now we can search the block ...
vtx = block_info.vtx
tx_count = len(block_info.vtx)
if tx_count >= 2 : # then we have more than just a coinbase transaction in the current block
        for x in range (0, len(vtx)) :  #loop the transactions
                thetx = vtx[x] #grab the CTransaction object
                vout = thetx.vout #grab the CTxOut object
                if len(vout) >= 1 : #	
			for y in range (0,len(vout)) : ##l
                        	vo = vout[y]
 	                        if vo.is_valid() :
                                	if vo.nValue > 0 :
                                        	z = bitcoin.core.b2x(vo.scriptPubKey) 
						z = z[6:]
						zlen = len(z)		
						zlen = zlen-4
						z = z[:zlen]
						if z == wikiLeaksKey:
							#print z
							donation = vo.nValue
							#print(donation)                                        	
							isdonation = isdonation+donation


btcdonation = str(isdonation)
btcdonationlen = len(btcdonation)
if btcdonationlen == 1 :
	btcdonation = "0.0000000" + str(btcdonation)
if btcdonationlen == 2 :
	btcdonation = "0.000000" + str(btcdonation)
if btcdonationlen == 3 :
	btcdonation = "0.00000" + str(btcdonation)
if btcdonationlen == 4 :
	btcdonation = "0.0000" + str(btcdonation)
if btcdonationlen == 5 :
	btcdonation = "0.000" + str(btcdonation)
if btcdonationlen == 6 :
	btcdonation = "0.00" + str(btcdonation)
if btcdonationlen == 7 :
	btcdonation = "0.0" + str(btcdonation)
if btcdonationlen == 8 :
	btcdonation = "0." + str(btcdonation)
if btcdonationlen == 9 :
	btcdonationleft = btcdonation[:1]
	btcdonationright = btcdonation[1:]
	btcdonation = btcdonationleft + "." + btcdonationright
if btcdonationlen == 10 :
	btcdonationleft = btcdonation[:2]
	btcdonationright = btcdonation[2:]
	btcdonation = btcdonationleft + "." + btcdonationright
if btcdonationlen == 11 :
	btcdonationleft = btcdonation[:3]
        btcdonationright = btcdonation[3:]
	btcdonation = btcdonationleft + "." + btcdonationright
if btcdonationlen == 12 :
	btcdonationleft = btcdonation[:4]
	btcdonationright = btcdonation[4:]
	btcdonation = btcdonationleft + "." + btcdonationright
if btcdonationlen == 13 :
	btcdonationleft = btcdonation[:5]
	btcdonationright = btcdonation[5:]
	btcdonation = btcdonationleft + "." + btcdonationright
if btcdonationlen == 14 :
	btcdonationleft = btcdonation[:6]
	btcdonationright = btcdonation[6:]
	btcdonation = btcdonationleft + "." + btcdonationright
if btcdonationlen == 15 :
	btcdonationleft = btcdonation[:7]
	btcdonationright = btcdonation[7:]
	btcdonation = btcdonationleft + "." + btcdonationright
if btcdonationlen == 16 :
	btcdonationleft = btcdonation[:8]
	btcdonationright = btcdonation[8:]
	btcdonation = btcdonationleft + "." + btcdonationright
		
if btcdonation != "0.00000000" :
        txt1 = "#bitcoin #donation @wikileaks " + btcdonation + " BTC #thankyou #bitcoinlove"
        s = twitter.update_status(status=txt1)
        print (s)
os.system('python /home/pi/freeross.py')






