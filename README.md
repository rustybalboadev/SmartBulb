<div align="center">
    <h1>SmartBulb</h1>
</div>

## Preparation ✔️
1. Get a [SmartThings API Key](https://account.smartthings.com/tokens)
2. Find your lights by following this [documentation](https://smartthings.developer.samsung.com/docs/api-ref/st-api.html#operation/getDevices)
3. Open **config.json** in the **app** folder and input your API Key & Device ID in the correct fields.

## Installation ✏️
First clone the repo
```bash
git clone https://github.com/RustyBalboadev/SmartBulb.git
```
Install necessary python modules
```bash
pip install -r requirements.txt
```
Run flask application
```bash
flask run
```