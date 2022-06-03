from brownie  import FundMe, accounts
from scripts.helpful_scripts import get_account

def fund(index: int):
    fund_me = FundMe[-1]
    account=get_account(index)
    entrance_fee = fund_me.getEntranceFee()
    #fund_fee > entrance_fee
    fund_fee =entrance_fee + 1;
    print(f"get_price={fund_me.getPrice()}")
    print(f"entrance_fee={entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": fund_fee})
    print("fund balance=",fund_me.addressToAmountFunded(account.address))

def withdraw(index: int):
    fund_me = FundMe[-1]
    account = get_account(index)
    fund_me.withdraw({"from": account})
    ## cannot get the 0 balance ????
    #balance=fund_me.getBal({"from": account})
    #print("fund balance=",balance)
    balance=fund_me.addressToAmountFunded(account.address)
    print("fund balance=",balance)


def main():
    ##0: contractr creater (owner)
    fund(0)
    fund(1)
    fund(3)
    withdraw(0)
