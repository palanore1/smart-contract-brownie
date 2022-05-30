from turtle import clear
from scripts.helpful_scripts import (
    get_account,
    OPENSEA_URL,
)
from scripts.setCollection import set_collection
from scripts.mint_and_uri import mint
from brownie import config, network, CoolPunks


def deploy():
    account = get_account()
    contract = CoolPunks.deploy(
        True,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print(f"Contract deployed at {contract.address}")
    return contract


def main():
    deploy()
    mint()
