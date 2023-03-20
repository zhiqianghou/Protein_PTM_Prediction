# Protein_PTM_Prediction
This code predicts potential post-translational modifications (PTMs) on lysine residues in the input protein, including phosphorylation, acetylation, methylation, ubiquitination, and SUMOylation. The code uses the NetPhos algorithm to predict phosphorylation sites and retrieves known PTM sites from UniProt. The output is a list of potential lysine PTM sites and a plot of the tau protein sequence highlighting these sites.

## Requirements

* Python 3
* requests module
* matplotlib module
* UniProt (https://www.uniprot.org/)

## Usage
1. Download the code and Download the code and navigate to the directory containing the code.
2. Update the UniProt accession number of the POI (Protein of Interest)
3. Run the code: python PTM_on_K_pred.py
4. The code will output a list of potential lysine PTM sites and plot the tau protein sequence highlighting these sites.

## Output

The code will output the following:

* A list of potential lysine PTM sites in the tau protein.
* A plot of the tau protein sequence with lysine residues highlighted in black and potential PTM sites highlighted in red.

