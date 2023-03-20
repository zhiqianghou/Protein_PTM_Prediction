import urllib.request
import requests


# Retrieve the tau protein sequence from UniProt
url = "https://www.uniprot.org/uniprot/P10636-8.fasta"
response = urllib.request.urlopen(url)
sequence = response.read().decode().split('\n')[1:]
sequence = ''.join(sequence)



# Use NetPhos to predict phosphorylation sites on lysine residues
url = "http://www.cbs.dtu.dk/cgi-bin/webface2.fcgi"
params = {
    'method': 'NetPhos',
    'seqsubmit': 'true',
    'seq': sequence,
    'output': 'text',
    'stype': 'protein',
    'format': 'internal'
}
response = requests.post(url, data=params)
phospho_predictions = response.text.split('\n')[1:-1]
lysine_phospho_sites = [int(x.split()[0]) for x in phospho_predictions if x.split()[2] == 'K']
