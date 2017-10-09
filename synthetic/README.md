# qpid-dispatch evaluation script for G5k

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

# Deploys everything

# g5k
python main.py g5k inventory prepare qpidda

# vagrant
python main.py vagrant inventory prepare qpidd
```