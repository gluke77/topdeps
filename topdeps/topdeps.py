import sys


def main():
    deps = {}

    nontops = set()

    for line in sys.stdin:
        line = line.strip()
        pkg, pkgs = line.split(":")
        deps[pkg.strip()] = [p.strip() for p in pkgs.split()]

    for d in deps.values():
        nontops.update(d)

    tops = set(deps.keys())
    tops -= nontops

    print("v.0.2.0")
    print("tops", tops)
    print("nontops", nontops)
