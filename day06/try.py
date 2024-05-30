import pandas as pd
import sys


def convert_file(input_filename, output_filename):
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} <filename>")

    filename = sys.argv[1]

    try:
        data = pd.read_csv(filename)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    filtered_data = data[data["CT"] != "Undetermined"]
    ct_mean = filtered_data["Ct Mean"]
    sample_name = filtered_data["Sample Name"]
    target_name = filtered_data["Target Name"]

    filtered_data["Ct Mean"] = pd.to_numeric(filtered_data["Ct Mean"], errors="coerce")
    filtered_data = filtered_data.dropna(subset=["Ct Mean"])

    gene_expression = 2 ** (-filtered_data["Ct Mean"])
    filtered_data["Gene Expression"] = gene_expression

    result_data = filtered_data[
        ["Sample Name", "Target Name", "Ct Mean", "Gene Expression"]
    ]
    
    print(result_data)
    output_file_path = 'gene_expression_results.csv'
    result_data.to_csv(output_file_path, index=False)



if __name__ == "__main__":
    if len(sys.argv) != 3:
        exit(f"Usage: {sys.argv[0]} <input filename> <output filename>")
    convert_file(sys.argv[1], sys.argv[2])
