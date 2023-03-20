import urllib.request
import requests
import matplotlib.pyplot as plt

# Download the protein sequence for the tau protein from UniProt
url = "https://www.uniprot.org/uniprot/P10636-8.fasta"
response = urllib.request.urlopen(url)
sequence = response.read().decode().split('\n')[1:]



# Use UniProt to retrieve known acetylation, methylation, and SUMOylation sites on lysine residues
url = "https://www.uniprot.org/uniprot/P10636-8.xml"
response = urllib.request.urlopen(url)
xml = response.read().decode()

acetylation_sites = []
methylation_sites = []
ubiquitination_sites = []
sumoylation_sites = []

for i, aa in enumerate(sequence):
    if aa == 'K':
        pos = i+1
        if f'<feature type="modified residue" description="Acetylation" location="{pos}"' in xml:
            acetylation_sites.append(pos)
        if f'<feature type="modified residue" description="Methyllysine" location="{pos}"' in xml:
            methylation_sites.append(pos)
        if f'<feature type="modified residue" description="SUMOylation" location="{pos}"' in xml:
            sumoylation_sites.append(pos)

# Combine the predicted PTM sites and the known PTM sites into a list of potential lysine PTM sites
ptm_sites = set(acetylation_sites + methylation_sites + sumoylation_sites)
ptm_sites = sorted(list(ptm_sites))

print("Potential lysine PTM sites:")
print(ptm_sites)

# Plot the lysine residues in the protein sequence and highlight the predicted PTM sites
fig, ax = plt.subplots(figsize=(10, 2))
ax.set_xlim([0, len(sequence)])
ax.set_ylim([0, 1])
ax.axis('off')
for i, aa in enumerate(sequence):
    if aa == 'K':
        color = 'red' if i+1 in ptm_sites else 'black'
        ax.text(i+0.5, 0.5, aa, ha='center', va='center', color=color)
    else:
        ax.text(i+0.5, 0.5, aa, ha='center', va='center')
plt.show()

