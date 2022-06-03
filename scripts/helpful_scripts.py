from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3
DECIMALS = 8
STARTING_PRICE= 181100000000
LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development","ganache-local"]

def get_account(index: int):
    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS):
        return accounts[index] #Ganache CLI
    else:
        return accounts.add(config["wallets"]["from_key"]) #rinkeby

def get_httpprovider():
    return config["httpprovider"][network.show_active()]["website"]

def get_verify():
    return config["networks"][network.show_active()].get("verify")

def deploy_mocks():
        if len(MockV3Aggregator) <=0:
            MockV3Aggregator.deploy(
                #DECIMALS, Web3.toWei(STARTING_PRICE,"ether"), {"from": get_account()}
                DECIMALS, STARTING_PRICE, {"from": get_account(0)}
            )

def get_priceAddr():
    if(network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS):
        ####rinkeby '0x8A753747A1Fa494EC906cE90E9f37563A8AF630e'
        price_feed_address=config["networks"][network.show_active()][
            "eth_usd_price_feed"
            ] 
    else:
        print(f"The active netwrok is {network.show_active()}")
        print("Deploying Mocks Aggregator")
        deploy_mocks()
        price_feed_address=MockV3Aggregator[-1].address
        print("Mocks Aggregator Deployed ")

    return price_feed_address
