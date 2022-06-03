from brownie  import FundMe, accounts
from scripts.helpful_scripts import get_account,get_httpprovider
from web3 import Web3, HTTPProvider

w3 =Web3(Web3.HTTPProvider(get_httpprovider()))

def withdraw(index: int):
    fund_me = FundMe[-1]
    account = get_account(index)
    #balance=fund_me.addressToAmountFunded(account.address)
    balance=w3.eth.get_balance(str(fund_me))
    print("Current fund balance=",balance)
    if(balance==0):
        print("fund balance= 0, you can not withdraw!")
    ## cannot get the 0 balance ????
    #balance=fund_me.getBal({"from": account})
    #print("fund balance=",balance)
    else:
        fund_me.withdraw({"from": account})
        #balance=fund_me.addressToAmountFunded(account.address)
        balance=w3.eth.get_balance(str(fund_me))
        if(balance==0):
            print("fund balance=",balance,"withdraw success!")
        else:
            print("fund balance=",balance,"withdraw fail!")

def main():
    withdraw(0)