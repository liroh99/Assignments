from convert_data import convert_file
import pytest

#The test will check the Gene expression column to see if the calculation was done correctly 

def test_calculate_gene_expression():
    df_res = convert_file("test.csv")
    df1 = df_res.iloc[1]
    col = df1['Gene Expression']
    assert(col, 0.00000049273705977)

    df2 = df_res.iloc[2]
    col = df2['Gene Expression']
    assert(col,0.000000274015319320)



test_calculate_gene_expression()
