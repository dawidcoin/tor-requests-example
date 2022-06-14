### Tor requests example

Example of browsing darknet using Tor client and python `request` library.

#### Install

Install Tor using instructions from here https://support.torproject.org/apt/. Enable control port and password-protect it:

```commandline
torpass=$(tor --hash-password "my-tor-password")
printf "HashedControlPassword $torpass\nControlPort 9051\n" | sudo tee -a /etc/tor/torrc
```

Confirm that password was properly included and restart tor service:

```commandline
tail -2 /etc/tor/torrc
sudo systemctl restart tor
```

Clone the repo and run the following:

```commandline
cd tor-requests-example
source source_me.sh
create_venv
```

#### Usage

`main.py` shows difference between your public IP and the one used in Tor circuit. You can also change Tor circuit which will result in new IP.

`python main.py <get_ip|get_tor_ip|change_tor_ip>`

Make sure that Tor service is running.
