from brownie import CoolPunks
from scripts.helpful_scripts import get_account


def stake(token_id):
    contract = CoolPunks[-1]
    account = get_account()
    tx = contract.stake(0, token_id, {"from": account})
    tx.wait(1)


def main():
    stake(0)
