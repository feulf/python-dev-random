# Python /dev/random
Python implementation of /dev/random. Pseudo random generator that uses MAC address, time and PID as seed, and a standard input as a source of entropy.


# Install
```bash
virtualenv -p python3 venv
. venv/bin/activate
```

# Run
Chose your source of entropy and pipe it into the random script
```bash
echo "111111111" | ./random.py
curl https://bitcoin.org/bitcoin.pdf | ./random.py
```