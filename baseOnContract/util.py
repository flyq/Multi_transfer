import json
import os

def getRawAccounts():
    "获取所有的账号,以及要给该账号地址发送多少币"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    accountFile = os.path.join(current_dir, "account.json")
    with open(accountFile) as f:
        account_names = json.loads(f.read())["rows"]
        return account_names