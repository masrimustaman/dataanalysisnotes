## read_csv
1. Given the name of the column, the parse_dates parameter converts the data type to datetime64[ns] which is the appropriate data type for dates.`df = pd.read_csv("Data/sample-sales-data.csv", parse_dates=["sales_date"])`
2. The usecols parameter allows for reading a subset of columns which is especially useful when there are several columns and we only need some of them. `df = pd.read_csv("Data/sample-sales-data.csv", usecols=["store","product","sales_qty"])`

## value_counts
It returns the unique values in a column along with the number of their occurrences.
```
df["store"].value_counts()
# output
3    29
4    22
2    19
5    16
6     8
1     6
Name: store, dtype: int64
```
We can use the normalize parameter to check the distribution with percent shares.
```
df["store"].value_counts(normalize=True)
# output
3    0.29
4    0.22
2    0.19
5    0.16
6    0.08
1    0.06
Name: store, dtype: float64
```

## astype
The astype function converts the data type of columns.
```
df["sales_date"] = df["sales_date"].astype("datetime64[ns]")
df.dtypes
# output
store                  int64
product                int64
sales_date    datetime64[ns]
sales_qty              int64
sales_rev            float64
dtype: object
```
We can also use a dictionary to change the data type of multiple columns in a single operation.
```
df = df.astype({"store":"category","sales_qty":"float"})
df.dtypes
# output
store               category
product                int64
sales_date    datetime64[ns]
sales_qty            float64
sales_rev            float64
dtype: object
```

## isna
```
customer.isna().sum()
# output
id            0
name          0
salary        2
city          1
start_date    1
dtype: int64

customer.isna().sum(axis=1) # for rows
# output
0    0
1    0
2    1
3    0
4    3
dtype: int64
```

## dropna
The following 3 parameters define how this function operates:
- axis: 0 for rows and 1 for columns
- how: any for dropping a row or column with any missing value and all for dropping a row or column with all missing values
- thresh: set a threshold on the number of non-missing values for a row or column so that it is not dropped.
Example : Let’s drop any row that does not have at least 3 non-missing values.`customer.dropna(axis=0, thresh=3, inplace=True)`

## fillna
Example : `customer["salary"].fillna(customer["salary"].mean(), inplace=True)`

## groupby
```
df.groupby("store")["sales_qty"].sum()
# output
store
1     140436
2      89710
3      71309
4      45068
5      69614
6      23598
Name: sales_qty, dtype: int64

```

We can also use named aggregations as follows:
```
df.groupby("store").agg(
    total_sales = ("sales_qty","sum")
)
```
