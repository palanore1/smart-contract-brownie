from brownie import CoolPunks
from scripts.helpful_scripts import get_account


def unstake(token_id):
    contract = CoolPunks[-1]
    account = get_account()
    tx = contract.unstake(0, token_id, {"from": account, "value": 1000000000000000})
    tx.wait(1)


def main():
    unstake(0)
