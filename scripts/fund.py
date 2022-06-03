from brownie  import FundMe, accounts
from scripts.helpful_scripts import get_account,get_httpprovider
from web3 import Web3, HTTPProvider

#w3 =Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/abadc6c834c5405db38243031cbaef6e"))
w3 =Web3(Web3.HTTPProvider(get_httpprovider()))

def fund(index: int):
    fund_me = FundMe[-1]
    account=get_account(index)
    entrance_fee = fund_me.getEntranceFee()
    #fund_fee > entrance_fee
    fund_fee =entrance_fee * 1.01;
    print(f"get_price={fund_me.getPrice()}")
    print(f"entrance_fee={entrance_fee}")
    print(f"Accout[{index}] Funding!")
    fund_me.fund({"from": account, "value": fund_fee})
    print(f"fund[{index}]balance=",fund_me.addressToAmountFunded(account.address))
    Total_balance=w3.eth.get_balance(str(fund_me))
    print("Contract totalta funding=",Total_balance)

def main():
    ##0: contractr creater (owner)
    fund(0)
    fund(1)
    fund(2)
