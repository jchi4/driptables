# driptables

![driptables_logo](images/driptables_logo.png)


```
GUI version of iptables
GUI framework: PyQt5
Backend language: Python
```

## Prerequisites

```
sudo apt-get update
```
```
sudo apt-get install python3.9
```

To run both of the above:

```
sudo bash -c "$(wget -nv -O - https://github.com/jchi4/driptables/raw/main/quick.sh)"
```

## Additional Packages

iptables-persistent and netfilters-persistent will autosave your firewall configuration.

```
sudo-apt-get install iptables-persistent netfilter-persistent
```

Prerequisites + additional packages + driptables:

```
sudo bash -c "$(wget -nv -O - https://github.com/jchi4/driptables/raw/main/full.sh)"
```