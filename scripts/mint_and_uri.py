from brownie import CoolPunks
from scripts.helpful_scripts import get_account


BASE_TOKEN_URI = (
    "https://gateway.pinata.cloud/ipfs/Qmciutf991sTocVdBykwTfajKcq3Ww5VbLTJLj7raZajNf/"
)


def mint():
    contract = CoolPunks[-1]
    account = get_account(index=0)
    token_uri = BASE_TOKEN_URI + str(contract.tokenCounter()) + ".json"
    tx = contract.createCollectible(
        0, token_uri, {"from": account, "value": 10000000000000000}
    )
    tx.wait(1)
    print(f"So far, there were {contract.tokenCounter()} tokens minted!")


def main():
    mint()
