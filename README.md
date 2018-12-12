# IPFS-Node

Create an IPFS node on your system and upload a file and fetch peers data.

## Steps

1. Open cmd terminal and install IPFS onto your system if you don't already have it from [here](https://docs.ipfs.io/introduction/install/)
```
# mac users can do so by running
brew install ipfs
```

2. Next, you need to instantiate ipfs on your system by running.
```
ipfs init
```

3. Next thing to make your system as ipfs node by running.
```
ipfs daemon
```
* This will make your system an ipfs node

4. Open a new cmd terminal and clone the repo.
```
git clone https://github.com/Zlash65/IPFS-Node.git

# go in the cloned directory
cd IPFS-Node
```

5. Install all the dependencies by running
```
# for python2 users
pip install -r requirements.txt

# for python3 users
pip3 install -r requirements.txt
```

6. Next thing is to connect to the peers that will help you host your file.
```
ipfs swarm peers
```

7. Everything is set now, simply run the `py-ipfs.py`
```
# for python2 users
python py-ipfs.py

# for python3 users
python3 py-ipfs.py
```

8. Enter the message that you want to be written in the file that will be uploaded to the ipfs network. You will be provided with a link on the terminal to access the file that was uploaded. You will also be shown the peers connected and the amount of data sent and received by each one of them.