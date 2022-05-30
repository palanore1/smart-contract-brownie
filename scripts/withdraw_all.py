from brownie import CoolPunks
from scripts.helpful_scripts import get_account


def withdraw_all():
    account = get_account()
    contract = CoolPunks[-1]
    tx = contract.withdraw({"from": account})
    tx.wait(1)
    print("You have withdrawn all the funds from the contract!")


def main():
    withdraw_all()
