# MySQL to JSON Webservice

This webservce exposes the results from a single mysql query as json.

## Environment variables

* `MYSQL_HOST` (required) - hostname or ip address of mysql server
* `MYSQL_PORT` (default 3306) - port of mysql server
* `MYSQL_USER` (required) - username for mysql connection
* `MYSQL_PASSWORD` (required) - password for mysql connection
* `MYSQL_DATABASE` (required) - mysql database to connect to
* `MYSQL_QUERY` (required) - query to execute
* `HTTP_PORT` (default 8000) - port of http server
* `ACCESS_TOKEN` (optional) - if set, the webservice is proteced by this token which must be passed as ?access_token=**** to the request

