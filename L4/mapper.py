#!/usr/bin/env python

import sys

# Initialize damping factor (usually denoted as d)
d = 0.85

# Mapper function
for line in sys.stdin:
    # Parse input
    page, links_str = line.strip().split("\t")
    links = eval(links_str)  # Convert string representation of list to list

    # Emit contribution to each linked page
    num_links = len(links)
    if num_links > 0:
        contribution = d / num_links
        for link in links:
            print(f"{link}\t{contribution}")

    # Emit original page with its links for graph structure preservation
    print(f"{page}\t{links_str}")
    