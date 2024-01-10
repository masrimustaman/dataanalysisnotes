## Connect to a database
DuckDB, by default, connects to a transient in-memory database. In other words, when the process is terminated, the data loaded is flushed. Providing the database parameter to the connect method persists all further changes. Two new files will be created.

Ref : https://github.com/octavianzarzu/flight-prices-streamlit-app-1/blob/main/app.py
```
!pip install duckdb
!pip install streamlit

import duckdb
con = duckdb.connect(database='itineraries.duckdb') 
```

## Loading the data
### Have a look at the data

```
preview_data_query = "FROM 'itineraries_snappy.parquet' LIMIT 5"
con.execute(preview_data_query).df()
--- Running a SELECT COUNT(*) returns more than 82 million rows.
```

### Load Data 

```
load_query = """
    CREATE OR REPLACE TABLE itineraries 
    AS SELECT
        flightDate,
        startingAirport,
        destinationAirport,
        -- travelDuration, /* inferred from Arrival & Departure */
        -- isBasicEconomy, /* not required for analysis */
        -- isRefundable, /* not required for analysis */
        -- isNonStop, /* applied as a filter on a single value */
        -- baseFare, /* not required for analysis */
        totalFare,
        seatsRemaining,
        segmentsAirlineName,
        segmentsArrivalTimeRaw,
        segmentsDepartureTimeRaw,
        segmentsCabinCode
    FROM 'itineraries_snappy.parquet'
    WHERE isNonStop
"""

con.execute(load_query)
```


## Passing Param
```
with col_a1: 
    startingAirports_df = con.execute("""
        SELECT 
            DISTINCT startingAirport 
        FROM itineraries 
        ORDER BY startingAirport
    """).df()
    startingAirport = st.selectbox('Starting Airport', startingAirports_df)

with col_a2:
    destinationAirports_df = con.execute("""
        SELECT 
            DISTINCT destinationAirport 
        FROM itineraries 
        WHERE startingAirport = ? 
        ORDER BY destinationAirport DESC
    """, [startingAirport]).df()
    destinationAirport = st.selectbox('Destination Airport', destinationAirports_df)
```
