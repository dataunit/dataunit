#!/bin/bash

/opt/mssql/bin/sqlservr --accept-eula &

# Unable to figure out how to dynamically tell when SQL Server finishes starting, but this represents that attempt
#BACK_PID=$!
#wait $BACK_PID
#while kill -0 $BACK_PID ; do
#    echo "Process is still active..."
#    sleep 5
#    # You can add a timeout here if you want
#done

echo 'Sleep for 33 seconds to allow enough time for SQL Server to start...'
sleep 33

#run the setup script to create the DB and the schema in the DB
echo 'Starting setup script'
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -d master -i /home/sqldb/MyFitBot_Setup.sql
echo 'Finished setup script'

# Make container sleep infinitely to keep the container and database accessible; otherwise, it shuts down once finished with the above
sleep infinity
