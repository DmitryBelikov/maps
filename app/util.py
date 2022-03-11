from dataclasses import dataclass


@dataclass
class Building:
    x: float
    y: float
    height: float

    address: str


def read_addresses(input_file):
    addresses = []
    with open(input_file) as file:
        for line in file:
            addresses.append(line.strip())
    return addresses
