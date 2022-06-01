from brownie import FundMe
from scripts.helpful_scripts import get_account
import os
from dotenv import load_dotenv
load_dotenv()

def deploy_fund_me():
    account = get_account()
    fund_me = FundMe.deploy({"from":account}, publish_source=True)
    #print(f"conctract is deplyed to {fund_me.address}")

def main():
    deploy_fund_me()