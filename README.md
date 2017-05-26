# BitcoinDonationScripts
These scripts are setup to be run with bitcoind + blocknotify.  They scan blocks appearing on the network and announce donations on Twitter to known public addresses.


### Installing the Bitcoin Module 
```
git clone https://github.com/petertodd/python-bitcoinlib
```

### Then run the following commands to install

```
cd python-bitcoinlib
sudo python setup.py build
sudo python setup.py install
```

### Setting up one of the twitter modules

```
pip install twython
```

## You have to also execute the .py file like you would with a bash script

### sudo chmod +x ./yourfile.py

### Before running BTCLOVEBOT.py you will need to go into BTCLOVEBOT.py, and change the following code

## command to put in bitcoin.conf
### blocknotify='location of your file' %s

## Created By Steve Douglas
<https://twitter.com/_myveryown>
# And Oliver Morris
<https://twitter.com/official_coder>
