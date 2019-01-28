from web3 import Web3, HTTPProvider
import rlp
from ethereum.transactions import Transaction
from util import getRawAccounts, getContractAddress

w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/fb99d3fd137c4e598ad561abaaadebcc'))

def getnonce(address):
    return w3.eth.getTransactionCount(address)



def playGame(s, nonce=None):
    '''
    :param sk: 私钥
    :param contract:合约账号
    :param nonce: nonce，如果连续完的话，每次+1
    :param value: 转账的金额
    :param gasprice:
    :param startgas: gaslimit
    :param funname: 要调用的方法
    :param params: 要调用的参数
    :return: tx
    '''
    # to EIP address
    address = '0x480E435352af25e2897E9fbE0FEE396451893A5F'
    sk = 'D1D2D5E93153360C38A1811023BF13BA43501332DFE31D093CFBA0462D78F8E7'
    address = w3.toChecksumAddress(address)

    # erc20 contract address
    #contractAddr = getContractAddress()
    # d = json.dumps(contractAddr)
    _contractAddr = '0xa1FFb2832cE68C619f580505B6d89Afeb9e2aDaC'


    # _data = w3.toBytes(hexstr=w3.toHex(text=s))
    _data =0xa9059cbb000000000000000000000000baaf27aedfb5c70bfa48c2c05eca8621ff410e160000000000000000000000000000000000000000000000000de0b6b3a7640000

    if not nonce:
        nonce = getnonce(address)
    startgas = 40

    # 空投地址
    RawAccounts = getRawAccounts()
    for i in RawAccounts:
        d = json.dumps(i)
        _address = json.loads(d)["address"]
        _amount = json.loads(d)["amount"]
        _transferAmount = _amount * 10 ** 18

        tx = Transaction(
            nonce=nonce,
            gasprice=100000000000,
            startgas=startgas,
            to=_contractAddr,
            value=0,
            data=_data)
        tx.sign(sk)
        raw_tx = rlp.encode(tx)
        raw_tx_hex = w3.toHex(raw_tx)
        tx = w3.eth.sendRawTransaction(raw_tx_hex)
        print(tx)
    return tx


if __name__ == '__main__':

    text = 'xixixixi'
    playGame(text)
