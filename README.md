## Password Strength Calculator

`6_password_strength` is a password estimator that gives score from 1 to 10.

### Requirements

* [zxcvbn-python](https://github.com/dwolfhub/zxcvbn-python)

### Installation

1. [Download](https://github.com/apirobot/6_password_strength/archive/master.zip) 6_password_strength from GitHub;
2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

```
usage: password_strength.py [-h] [-i INPUTS [INPUTS ...]]

Password Strength Calculator

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTS [INPUTS ...], --inputs INPUTS [INPUTS ...]
                        list of user inputs like name and email
```

### Usage examples

```bash
python password_strength.py
>>> Type password: correcthorsebatterystaple
>>> Password strength: 10 of 10

python password_strength.py
>>> Type password: DenisPa$$w0rd
>>> Password strength: 4 of 10

python password_strength.py --inputs Denis denis@gmail.com
>>> Type password: DenisPa$$w0rd
>>> Password strength: 3 of 10
```
