import sys


def main():
    tops = set()
    nontops = set()

    for line in sys.stdin:
        pkg, pkgs = line.strip().split(":")
        tops.add(pkg.strip())
        nontops.update(p.strip() for p in pkgs.split())

    tops -= nontops

    print("v.0.2.1")
    print("tops", tops)
    print("nontops", nontops)
