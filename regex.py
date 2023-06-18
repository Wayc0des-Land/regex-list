import re

input_file = "allsubdomain.txt"
output_file = "modified_domains.txt"

# Read domains from input file
with open(input_file, "r") as file:
    domains = file.read().splitlines()

# Process domains
modified_domains = []

for domain in domains:
    modified_domain = re.sub(r"\.(?=[^.]*$)", "", domain)
    modified_domains.append(modified_domain)

# Write modified domains to output file
with open(output_file, "w") as file:
    file.write("\n".join(modified_domains))

print("Modified domains have been written to", output_file)