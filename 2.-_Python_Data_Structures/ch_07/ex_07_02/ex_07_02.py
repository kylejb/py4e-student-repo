# use mbox-short.txt for sample file data
fname = input("Enter file name: ")
fh = open(fname)
counter = 0
tl_xconf = 0
for line in fh:
    rline = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        counter = counter + 1
        # storing value for denominator in tcount
        t_count = counter
        # stripping rline to isolate numerical value
        xconf = float(rline[len(rline) - 6 : len(rline)])
        # adding xconf through iterative loop
        tl_xconf += xconf
        # storing value for final sum in tl_xconf
        t_xconf = tl_xconf
        # storing AVG of X-DSPAM-Confidence
        avg_xconf = t_xconf / t_count
print("Average spam confidence:", avg_xconf)
