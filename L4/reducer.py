#!/usr/bin/env python

import sys

# Initialize damping factor (usually denoted as d)
d = 0.85
N = 1000  # Total number of pages (can be determined dynamically)

# Variables to store current page and its PageRank contributions
current_page = None
total_contribution = 0.0
page_links = []

# Reducer function
for line in sys.stdin:
    # Parse input
    page, value = line.strip().split("\t")
    
    try:
        value = float(value)
    except ValueError:
        # If value is not convertible to float, it represents a list of outgoing links
        page_links = eval(value)
        continue
    
    # If we're still processing the same page
    if current_page == page:
        total_contribution += value
    else:
        # If this is a new page, output the accumulated PageRank for the previous page
        if current_page:
            new_rank = (1 - d) / N + d * total_contribution
            print(f"{current_page}\t{new_rank}\t{page_links}")
        
        # Start processing a new page
        current_page = page
        total_contribution = value
        page_links = []

# Output the last page
if current_page:
    new_rank = (1 - d) / N + d * total_contribution
    print(f"{current_page}\t{new_rank}\t{page_links}")
    