FROM mcr.microsoft.com/mssql/server:2019-latest

# Declare environment variables for SQL DB
ENV ACCEPT_EULA=Y
ENV SA_PASSWORD=dataunitSQL2020!

# Create directory to place app specific files
USER root
RUN mkdir -p /home/sqldb
WORKDIR /home/sqldb

# Copy setup scripts
COPY entrypoint.sh ./
COPY run_sql.sh ./
COPY MyFitBot_Setup.sql ./

# Ensure main script is executable
RUN chmod +x ./entrypoint.sh

# Run main script, which will start and set up SQL DB
CMD /bin/bash ./entrypoint.sh