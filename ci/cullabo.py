from web3 import Web3, IPCProvider

# Connect to the Ethereum node
w3 = Web3(IPCProvider())

# Create an account from a private key
account = w3.eth.account.privateKeyToAccount("0x...")

# Print the address of the account
print(account.address)
