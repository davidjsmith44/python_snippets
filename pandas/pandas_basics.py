""" Pandas Basics """


# Loading data functions
df = pd.read_excel("relative_path_and_filename", sheet_name="name_of_worksheet_in_file")


# Renaming columns (below explicitly passes a dictionary. Can reference a dictionary within rename.)
df.rename(
    index=str,
    columns={
        "Document Currency": "curr",
        "Enterprise BU Desc": "BU",
        "Invoice Fiscal Year Period Desc": "period",
        "Product Config Type": "config",
        "Rev Rec Category": "rev_req_type",
        "Rule For Bill Date": "rebill_rule",
        "Completed Sales ( DC )": "DC_amount",
        "Completed Sales": "US_amount",
    },
    inplace=True,
)


# Value Counts - creates listing of how often each unique entry in the column occurs in the column
df["column"].value_counts()


#### Cleaning up dataframes

# Remove all rows that have a zero in column 'A'
df = df[df["A"] != 0]


# creating a slice of a dataframe
df_slice_copied = df[df["A"] == "something"].copy()


# Groupby multuple columns and sum everythong else
df_grouped = df.grouby(["col 1", "col2", "col3"]).sum()

# Grouping based on whether data is in a list (verses grouping all)
a_list = ["Y1", "Y2", "Y3"]
df_grouped = df[df["column A"].isin([a_list])].copy()


### Merging dataframes

## Joining Dataframes

#### Concatenating dataframes
