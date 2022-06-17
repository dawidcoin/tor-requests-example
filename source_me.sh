# After cloning repo
function create_venv() {
  echo "Creating virtual environment"
  virtualenv venv
  source ./venv/bin/activate
  echo "Installing modules from 'requirements.txt'"
  pip install -r requirements.txt
  echo "Done."
}

function activate() {
  source ./venv/bin/activate
}

function test_ip() {
  echo "IP"
  python3 main.py get_ip
  echo "Tor IP"
  python3 main.py get_tor_ip
  echo "Requesting new circuit"
  python3 main.py request_new_tor_circuit
  echo "Tor (new) IP"
  python3 main.py get_tor_ip
}

