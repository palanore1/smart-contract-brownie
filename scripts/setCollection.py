from brownie import CoolPunks
from scripts.helpful_scripts import get_account


def set_collection():
    contract = CoolPunks[-1]
    account = get_account()
    tx = contract.setCollection(
        True,  # is stakable
        contract.address,
        10000000000000000,  # mint fee
        1000000000000000,  # harvest fee
        2,  # multiplier
        5,  # staking limit
        10,  # harvestCooldown
        {"from": account},
    )
    tx.wait(1)
    print("Collection updated!")
