import sys
from argparse import ArgumentParser
import os

import api
from shortest_cable import compute_length
import util


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--input_file')
    parser.add_argument('--stub_file')
    parser.add_argument('--output_file', default=None)
    return parser.parse_args()


def main():
    args = parse_args()
    stub_file = args.stub_file
    os.environ['STUB_FILE'] = stub_file
    input_file = args.input_file
    addresses = util.read_addresses(input_file)
    locations = api.address_locations(addresses)
    heights = api.address_heights(addresses)
    buildings = []
    for address in addresses:
        location = locations[address]
        height = heights[address]
        buildings.append(
            util.Building(location['x'], location['y'], height, address)
        )
    length, cables = compute_length(buildings)
    output_file = args.output_file
    if output_file is None:
        output_file = sys.stdout
    else:
        output_file = open(output_file, 'w+')
    print(f'Суммарная длина кабеля: {length} метров', file=output_file)
    print('Кабелями следует соединить здания:', file=output_file)
    for address1, address2 in cables:
        print(f'{address1} -- {address2}', file=output_file)


if __name__ == '__main__':
    main()

