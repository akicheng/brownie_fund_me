from brownie import network,accounts,exceptions
from scripts.helpful_scripts import (
    get_account, 
    get_httpprovider,
    LOCAL_BLOCKCHAIN_ENVIROMENTS,
)
from scripts.deploy import deploy_fund_me
from web3 import Web3, HTTPProvider
import pytest

def test_can_fund_and_withdraw():
    w3 =Web3(Web3.HTTPProvider(get_httpprovider()))
    account =get_account(0)
    fund_me = deploy_fund_me()
    fund_fee = (fund_me.getEntranceFee()) * 1.01
    tx= fund_me.fund({"from": account,"value":fund_fee })
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == fund_fee
    tx2=fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert w3.eth.get_balance(str(fund_me)) == 0
    #assert fund_me.addressToAmountFunded(account.address) == 0

def test_other_withdraw():
    w3 =Web3(Web3.HTTPProvider(get_httpprovider()))
    account =get_account(0)
    fund_me = deploy_fund_me()
    fund_fee = (fund_me.getEntranceFee()) * 1.01
    tx= fund_me.fund({"from": account,"value":fund_fee })
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == fund_fee

    if network.show_active() != "development":
        pytest.skip("not in local network! Only for local testing")

    account2 =accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": account2})

    assert w3.eth.get_balance(str(fund_me)) != 0

def test_only_owner_can_withdraw():
    #if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
    if network.show_active() != "development":
        pytest.skip("not in local network! Only for local testing")
    fund_me = deploy_fund_me()
    account2 = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": account2})