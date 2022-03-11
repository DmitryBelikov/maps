import math


def manhattan_distance(first, second):
    return math.fabs(first.x - second.x) + math.fabs(first.y - second.y)


def get_component(vertex, components_base):
    parent = components_base[vertex]
    if parent == vertex:
        return parent
    component_id = get_component(parent, components_base)
    components_base[vertex] = component_id
    return component_id


def unite(left, right, components_base):
    left_parent = get_component(left, components_base)
    right_parent = get_component(right, components_base)

    if left_parent == right_parent:
        return

    if components_base[right] != left:
        components_base[left] = right_parent


def compute_length(buildings):
    edges = []
    for first_idx in range(len(buildings)):
        first = buildings[first_idx]
        for second_idx in range(first_idx + 1, len(buildings)):
            second = buildings[second_idx]
            length = manhattan_distance(first, second)
            edges.append((length, first_idx, second_idx))

    edges = sorted(edges)
    components_base = [x for x in range(len(buildings))]
    used_addresses = []
    answer = sum(2 * building.height for building in buildings)
    for length, left, right in edges:
        if get_component(left, components_base) == \
           get_component(right, components_base):
            continue
        answer += length
        used_addresses.append((buildings[left].address,
                               buildings[right].address))
        unite(components_base[left], components_base[right], components_base)
    return answer, used_addresses
