# Powershell + SQL
Sometime export is better done in powershell due to the text qualifier. 

Example code : 
```
# Define the SQL Server connection details
$serverInstance = "sv04935\sql04935"  # Replace with your server name
$databaseName = "svr_reporting"  # Replace with your database name

# Define the query
$query = @"
SELECT * 
FROM RAW_SMAX_ASSET
"@

# Execute the query
Invoke-Sqlcmd -ServerInstance $serverInstance -Database $databaseName -Query $query -TrustServerCertificate
```
