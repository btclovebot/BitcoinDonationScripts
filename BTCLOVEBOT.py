#!/usr/bin/env python
## The @BTCLOVEBOT TWITTER SCRIPT

## Create a proxy object and connect to the bitcoin.rpc
import bitcoin.rpc
from twython import Twython

myproxy = bitcoin.rpc.Proxy()

## Grab the block we going to need it
block_info = myproxy.getblock(myproxy.getblockhash(myproxy.getblockcount()))
vtx = block_info.vtx

## Setting these as variables will make them easier for future edits
app_key =  ''
app_secret = ''
oauth_token = ''
oauth_token_secret = ''

## Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#The above should just be a single line, without the break

## KEYS we search for an tweet about
alakanani = "1JQYtfn54M2hYsHqeFmSZfUNfyrJFTT5oJ"
alakananikey = "beee539a790605764f5bae7523d4805f4927480d" 

protip = "1ProTip9x3uoqKDJeMQJdQUCQawDLauNiF"
protipkey = "fabdeeccef02450b17c8a9d3d497a405504ce3da" 

andreas = "1andreas3batLhQa2FawWjeyjCqyBzypd"
andreaskey = "0663d2403f560f8d053a25fbea618eb470716176" 

courage = "1courAa6zrLRM43t8p98baSx6inPxhigc"
couragekey = "06c5b7d78985ab1046fa13a7f2835a453b7ae454" 

freeRoss = "1Ross5Np5doy4ajF9iGXzgKaC2Q3Pwwxv"
freeRossKey = "04b11d2eb716291f33be29210ee5b2a161c071af" 

gpg = "1M3GipkG2YyHPDMPewqTpup83jitXvBg9N"
gpgkey = "dbd0788d294dd15704d232053790c555d1cb3378" 

lukewearechange = "17zfAyA1kxieD7QzjRUDLrRPRxxfPDZxtD"
lukewearechangekey = "4cb8542bcb9d8791cf08b8e81d99129f7cb69386" 

MadBitcoins = "1LAYuQq6f11HccBgbe6bx8DiwKwzuYkPR3"
MadBitcoinsKey = "d238c3eebafd29537437cd2a40081d9bc6e2067e"

hirosaki = "1HMyNgDXM9QF2zgMbJTW5dZTo1px3DnBRk"
hirosakiKey = "b37963e3b48ee4b315cea3c5c1844d70e8c05813" 

rnli = "1PZ5ebvdt43dvRRgRNgBhsq2PwAKN4X6W"
rnlikey = "0443ee29160b2ab12ab660302891abab61029748" 

ubuntumate = "1Mpan6eExzNKdS8JnFAod5Pwt49aR6JsDB"
ubuntumatekey = "e462430f1f06837b4bb9a7c3e5d489b5fa4c9c31" 

wikiLeaks = "1HB5XMLmzFVj8ALj6mfBsbifRoD4miY36v"
wikiLeaksKey = "b169f2b0b866db05900b93a5d76345f18d3afb24" 

## FUNCTION BLOCK ##

## Function to search for an  output to a given pubkey
def searchblock (key) :
	donation = 0 
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
							if z == key:
								donation = vo.nValue

	return donation ;
	
def searchblockPT (key) :	

	isprotip = False
	donated = 0
	benefactors = 0
	protips = 0

	## Now we can search the block ...
	
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
							if z == protipkey:
								isprotip =  True ## OK we have found an output with the ProTip Vanity key
				if isprotip :
					if len(vout) >2 : ## If we have more than two outputs the last is usually back to user
						vo = vout[yy]
						for yy in range (0,len(vout)-1) :
							if vo.is_valid() :
								if vo.nValue > 0 :
									benefactors = benefactors + 1
									donated = donated + vo.nValue
					else :
						if len(vout) == 2 :
							for yy in range (0,len(vout)-1) :
								vo = vout[yy] ## we have a two outputs - just a donation to protip with protip ? or to protip with change to user
								if vo.is_valid() :
									if vo.nValue > 0 :
										benefactors = benefactors + 1
										donated = donated + vo.nValue
						else : ## we have single output to protip so is just a donation or sure
							vo = vout[0]
							if vo.is_valid() :
								if vo.nValue > 0 :
									benefactors = benefactors + 1
									donated = donated + vo.nValue
									
					isprotip = False ##reset the trigger for the next transaction in the block
					protips = protips +1 ##increment the count of tx's that are protip

					
	if protips >=1 : 
		if benefactors == 1 :
			txt1 = "#bitcoin #donation to @ProTipHQ " + str(btcformat(donated)) + " BTC #thankyou"
			photo = open('/home/pi/twitter/protip.jpg', 'rb')
			response = twitter.upload_media(media=photo)
			twitter.update_status(status=txt1, media_ids=[response['media_id']])
		else :
			txt1 = "#bitcoin #donation via @ProTipHQ " + str(btcformat(donated)) + " BTC to " + str(benefactors) +" recipients #thankyou"
			photo = open('/home/pi/twitter/protip.jpg', 'rb')
			response = twitter.upload_media(media=photo)
			twitter.update_status(status=txt1, media_ids=[response['media_id']])
	return ; 	

	
## Function to Format Satoshis into BTC eg 12,345,678.12345678
def btcformat (satoshis) :
	if satoshis == 0 :
		btcformatted = "0.00000000"
	else :
		satoshis = str(satoshis)
		satoshislen = len(satoshis)
		if satoshislen == 1 :
			btcformatted = "0.0000000" + satoshis
		if satoshislen == 2 :
			btcformatted = "0.000000" + satoshis
		if satoshislen == 3 :
			btcformatted = "0.00000" + satoshis
		if satoshislen == 4 :
			btcformatted = "0.0000" + satoshis
		if satoshislen == 5 :
			btcformatted = "0.000" + satoshis
		if satoshislen == 6 :
			btcformatted = "0.00" + satoshis
		if satoshislen == 7 :
			btcformatted = "0.0" + satoshis
		if satoshislen == 8 :
			btcformatted = "0." + satoshis
		if satoshislen == 9 :
			satoshisleft = satoshis[:1]
			satoshisright = satoshis[1:]
			btcformatted = satoshisleft + "." + satoshisright
		if satoshislen == 10 :
			satoshisleft = satoshis[:2]
			satoshisright = satoshis[2:]
			btcformatted = satoshisleft + "." + satoshisright
		if satoshislen == 11 :
			satoshisleft = satoshis[:3]
			satoshisright = satoshis[3:]
			btcformatted = satoshisleft + "." + satoshisright
		if satoshislen == 12 :
			satoshisleft = satoshis[:4]
			satoshisright = satoshis[4:]
			btcformatted = satoshisleft[:1] + "," + satoshisleft[1:] + "." + satoshisright
		if satoshislen == 13 :
			satoshisleft = satoshis[:5]
			satoshisright = satoshis[5:]
			btcformatted = satoshisleft[:2] + "," + satoshisleft[2:] + "." + satoshisright		
		if satoshislen == 14 :
			satoshisleft = satoshis[:6]
			satoshisright = satoshis[6:]
			btcformatted = satoshisleft[:3] + "," + satoshisleft[3:] + "." + satoshisright
		if satoshislen == 15 :
			satoshisleft = satoshis[:7]
			satoshisright = satoshis[7:]
			btcformatted = "," + satoshisleft[4:] + "." + satoshisright
			satoshismid = satoshisleft
			satoshisleft = satoshisleft[:1]
			satoshismid = satoshismid[:4]
			satoshismid = satoshismid[1:]
			btcformatted =  satoshisleft + "," + satoshismid + btcformatted
		if satoshislen == 16 :
			satoshisleft = satoshis[:8]
			satoshisright = satoshis[8:]
			btcformatted = "," + satoshisleft[5:] + "." + satoshisright
			satoshismid = satoshisleft
			satoshisleft = satoshisleft[:2]
			satoshismid = satoshismid[:5]
			satoshismid = satoshismid[2:]
			btcformatted =  satoshisleft + "," + satoshismid + btcformatted
	return btcformatted
	
	
## END FUNCTINON BLOCK

## MAIN SCRIPT
## Display what we are doing
#print ("Searching for a Donations")

## First up is to run the ProTip Search ..this search adjusts the tweet depending upon result
searchblockPT(protipkey)

## Then we can run the standard search/tweets for all other addresses
thedonation = searchblock(alakananikey)
thedonation = btcformat(thedonation)
if thedonation != "0.00000000" :
	txt1 = "#bitcoin #donation @bitcoinlady " + thedonation + " BTC #thankyou #bitcoinlove #satoshicentre"
	twitter.update_status(status=txt1)

thedonation = searchblock(andreaskey)
thedonation = btcformat(thedonation)
if thedonation != "0.00000000" :
	txt1 = "#bitcoin #donation @aantonop " + thedonation + " BTC #thankyou"
	twitter.update_status(status=txt1)

thedonation = searchblock(couragekey)
thedonation = btcformat(thedonation)
if thedonation != "0.00000000" :
	txt1 = "#bitcoin #donation @couragefound " + thedonation + " BTC #thankyou #couragefoundation"
	twitter.update_status(status=txt1)

thedonation = searchblock(freeRossKey)
thedonation = btcformat(thedonation)
if thedonation != "0.00000000" :
	txt1 = "#bitcoin #donation @free_ross " + thedonation + " BTC #thankyou #FreeRoss"
	twitter.update_status(status=txt1)

thedonation = searchblock(gpgkey)
thedonation = btcformat(thedonation)
if thedonation != "0.00000000" :
	txt1 = "#bitcoin #donation @gpg4win " + thedonation + " BTC #thankyou #gpg"
	twitter.update_status(status=txt1)

thedonation = searchblock(lukewearechangekey)
thedonation = btcformat(thedonation)
if thedonation != "0.00000000" :
	txt1 = "#bitcoin #donation @Lukewearechange " + thedonation + " BTC #thankyou #WeAreChange"
	twitter.update_status(status=txt1)

thedonation = searchblock(MadBitcoinsKey)
thedonation = btcformat(thedonation)
if thedonation != "0.00000000" :
	txt1 = "#bitcoin #donation @madbitcoins " + thedonation + " BTC #thankyou #bitcoinlove"
	twitter.update_status(status=txt1)

thedonation = searchblock(hirosakiKey)
thedonation = btcformat(thedonation)
if thedonation != "0.00000000" :
	txt1 = "#bitcoin #donation Hirosaki's cherry blossoms @coincheckjp " + thedonation + " BTC #thankyou"
	twitter.update_status(status=txt1)

thedonation = searchblock(rnlikey)
thedonation = btcformat(thedonation)
if thedonation != "0.00000000" :
	txt1 = "#bitcoin #donation @RNLI " + thedonation + " BTC #thankyou #rnli"
	twitter.update_status(status=txt1)

thedonation = searchblock(ubuntumatekey)
thedonation = btcformat(thedonation)
if thedonation != "0.00000000" :
	txt1 = "#bitcoin #donation @ubuntu_mate " + thedonation + " BTC #thankyou #ubuntu"
	twitter.update_status(status=txt1)

thedonation = searchblock(wikiLeaksKey)
thedonation = btcformat(thedonation)
if thedonation != "0.00000000" :
	txt1 = "#bitcoin #donation @wikileaks " + thedonation + " BTC #thankyou #wikileaks"
	twitter.update_status(status=txt1)
	
## EOF ##