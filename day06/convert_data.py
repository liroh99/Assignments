import pandas as pd
import sys


def convert_file(input_filename):
    try:
        data = pd.read_csv(input_filename)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    filtered_data = data[data["CT"] != "Undetermined"]
    ct_mean = filtered_data["Ct Mean"]
    sample_name = filtered_data["Sample Name"]
    target_name = filtered_data["Target Name"]

    filtered_data["Ct Mean"] = pd.to_numeric(filtered_data["Ct Mean"], errors="coerce")


    gene_expression = 2 ** (-filtered_data["Ct Mean"])
    filtered_data["Gene Expression"] = gene_expression

    result_data = filtered_data[
        ["Sample Name", "Target Name", "Ct Mean", "Gene Expression"]
    ]
    
    return result_data


def convert_file_write_result(input_filename, output_filename):
    result_data = convert_file(input_filename)
    result_data.to_csv(output_filename, index=False)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        exit(f"Usage: {sys.argv[0]} <input filename> <output filename>")
    convert_file_write_result(sys.argv[1], sys.argv[2])
