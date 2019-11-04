import pandas as pd

df = pd.read_csv("/home/breno/PycharmProjects/untitled2/miRTarBase_MTI.csv", sep='\t')


def rename_columns(columns_names):
    only_hsa.columns = columns_names


def filter_by_organism(column=5, org='Homo sapiens'):
    return df[df.iloc[:, column] == org]


def remove_duplicates(column="D"):
    return only_hsa.drop_duplicates(subset=column)


only_hsa = filter_by_organism()
rename_columns(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
not_repeated = remove_duplicates("D")

genes = not_repeated["D", "E", "F"]