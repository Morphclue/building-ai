port_names = ["PAN", "AMS", "CAS", "NYC", "HEL"]

def permutations(route, ports):
    if len(ports) == 0:
        print(' '.join([port_names[i] for i in route]))
    else:
        for i in range(len(ports)):
            permutations(route + [ports[i]], ports[:i] + ports[i + 1:])

permutations([0], list(range(1, len(port_names))))
