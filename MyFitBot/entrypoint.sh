#!/bin/bash

/opt/mssql/bin/sqlservr --accept-eula &
#BACK_PID=$!
#wait $BACK_PID
#while kill -0 $BACK_PID ; do
#    echo "Process is still active..."
#    sleep 5
#    # You can add a timeout here if you want
#done
echo 'Sleep for 33 seconds to allow enough time for SQL Server to start...'
sleep 33
echo 'Starting setup script'
#./run_sql.sh
#run the setup script to create the DB and the schema in the DB
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -d master -i /home/sqldb/MyFitBot_Setup.sql
echo 'Finished setup script'
sleep infinity
#/opt/mssql/bin/sqlservr --accept-eula && ./run_sql.sh
#start the script to create the DB and data then start the sqlserver
#./run_sql.sh & /opt/mssql/bin/sqlservr

#echo 'Sleeping 20 seconds before running setup script'
#sleep 10

#echo 'Starting setup script'

#/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P dataunitSQL2020! -d master -i MyFitBot_Setup.sql

#echo 'Finished setup script'
#/opt/mssql/bin/sqlservr --accept-eula &