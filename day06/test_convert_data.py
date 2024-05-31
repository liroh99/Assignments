from convert_data import convert_file

#The test will check the Gene expression column to see if the calculation was done correctly 


def test_calculate_gene_expression():
    df_res = convert_file("test.csv")
    df1 = df_res.iloc[0]
    col1 = df1['Gene Expression']
    assert col1==2**-20.953


    df2 = df_res.iloc[2]
    col2 = df2['Gene Expression']
    assert col2== 2**-21.799






