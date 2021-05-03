from web3 import Web3

def getBalance(nodeIp,address):

 w3=Web3(Web3.HTTPProvider(nodeIp))

 #print(w3.isConnected())
balance=w3.fromWei(w3.eth.get_balance(address),'ether')

 print(f"{address} : {balance} ether")

if __name__=="__main__":
    nodeIp="http://127.0.0.1:7545"  #infura
    address="bnb136ns6lfw4zs5hg4n85vdthaad7hq5m4gtkgf23"

    getBalance(nodeIp,address)