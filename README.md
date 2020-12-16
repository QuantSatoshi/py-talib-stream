# py-talib-stream

## dev install
```
make dev-install
```

## run unit test
```
make install
make test
```

## auto formatting

```
make format
```


## install talib in ubuntu

These command may work
```
apt update && apt install build-essential wget -y
wget https://artiya4u.keybase.pub/TA-lib/ta-lib-0.4.0-src.tar.gz
tar -xvf ta-lib-0.4.0-src.tar.gz

cd ta-lib/ &&./configure --prefix=/usr && make && make install
rm -rf ta-lib-0.4.0-src.tar.gz
pip install TA-Lib
```

