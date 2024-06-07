import sys
import os 
from Bio import Entrez, SeqIO 
Entrez.email="liron151@gmail.com"
import requests 
import datetime 
import csv 


def get_data(term,max):
    handle=Entrez.esearch(db="Gene",term=term,idtype="acc",retmax=max)
    record=Entrez.read(handle)
    handle.close()
    return record['IdList'], int(record['Count'])

def download_data(ids,term):
    for i, ncbi_id in enumerate(ids):
        try:
            handle = Entrez.efetch(db="gene", id=ncbi_id, rettype="fasta", retmode="text")
            data = handle.read()
            handle.close()
            filename = f"item_{i+1}_{term}.fasta"
            with open(filename, "w") as file:
                file.write(data)
            print(f"Downloaded {filename}")
        except Exception as e:
            print(f"Error downloading {ncbi_id}: {e}")
        

    
def add_to_csv(date,term,max,total):
    entry=[date,term,max,total]
    filename="search_data.csv"
    file_exists = os.path.isfile(filename)
    with open(filename,"a",newline='') as file:
        writer=csv.writer(file)
        if not file_exists: 
            writer.writerow(["date","term","max","total"])
        writer.writerow([date,term,max,total])



if __name__ == "__main__":
    if len(sys.argv) != 3:
        exit(f"Usage: {sys.argv[0]} <TERM> <NUMBER>")
    term=sys.argv[1]
    max=sys.argv[2]
    IDs,total=get_data(term,max)
    download_data(IDs,term)
    date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    add_to_csv(date,term,max,total)


