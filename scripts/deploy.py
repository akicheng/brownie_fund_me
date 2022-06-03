from brownie import FundMe
from scripts.helpful_scripts import (
    get_account, 
    get_priceAddr, 
    get_verify,
    LOCAL_BLOCKCHAIN_ENVIROMENTS,
)
#import os
#from dotenv import load_dotenv
#load_dotenv()



def deploy_fund_me():
    account = get_account(0)
    priceAddr= get_priceAddr()
    verify= get_verify()
    ## publish_source=True for contract verify when deploy to Etherscan
    #fund_me = FundMe.deploy({"from":account}, publish_source=True)
    #fund_me = FundMe.deploy(priceAddr,{"from":account}, publish_source=True)
    fund_me = FundMe.deploy(priceAddr,{"from":account} , publish_source=get_verify())
    print(f"conctract is deplyed to {fund_me.address}")
    print(f"FundMe conctract is deplyed {len(FundMe)} times!")
    return fund_me

def main():
    deploy_fund_me()