import requests
import sys
from stem import Signal
from stem.control import Controller
from yaml import full_load


def get_control_port_password() -> str:
    try:
        with open(CONFIG_FILE) as file:
            paths = full_load(file)
        return paths['password']
    except FileNotFoundError:
        print(f'No {CONFIG_FILE} in data folder.')
        exit(1)


def get_ip() -> None:
    print(requests.get(
        IP_URL
    ).text)


def get_tor_ip() -> None:
    print(requests.get(
        IP_URL,
        proxies={
            "https": "socks5h://127.0.0.1:9050"
        }
    ).text)


def change_tor_ip() -> None:
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=get_control_port_password())
        controller.signal(Signal.NEWNYM)


CONFIG_FILE = "config.yaml"
IP_URL = "https://api.ipify.org"
HELP_MESSAGE = "Usage: main.py <print_id|print_tor_ip|change_tor_ip>"
FUNCTIONS = {
    "get_ip": get_ip,
    "get_tor_ip": get_tor_ip,
    "change_tor_ip": change_tor_ip
}


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in FUNCTIONS:
        print(HELP_MESSAGE)
    else:
        FUNCTIONS[sys.argv[1]]()
