import json
import os


def stub_file_locations(addresses):
    stub_file = os.environ['STUB_FILE']
    with open(stub_file) as file:
        data = json.load(file)
    result = {}
    for address in addresses:
        result[address] = data[address]['location']
    return result


def stub_file_heights(addresses):
    stub_file = os.environ['STUB_FILE']
    with open(stub_file) as file:
        data = json.load(file)
    result = {}
    for address in addresses:
        result[address] = data[address]['height']
    return result


def address_locations(addresses):
    return stub_file_locations(addresses)


def address_heights(addresses):
    return stub_file_heights(addresses)
