# deepersCreepers
Scrape the deep web for live urls

# Requirements
PyGoogle
  - pip install pygoogle

# Arguments
-v / -V    Verbose Mode Enabled

-b / -B    Brute force URLs

-s / -S    Scrape urls

# Configuration
This script is configured using the 'config.ini' file inside of the 'config' folder.  Below we will look at each section of the configuration file.

Tor
---
This section contains the configuration information for your tor
proxy server settings.  You must have tor running and accessable
to your machine.  You may test the connection to your proxy by
entering the tor ip and port you will use below in your browser
of choice and visiting https://check.torproject.org/

* host
    * IP address where tor is running
* port
    * Port tor is listening on

Database
---
This section contains all of the configuration information for your
database engine.  Currently only sqlite and mongodb are supported for
persistent result storage.

Example configs:
* Sqlite
    * engine: sqlite
    * dir: database
    * filename: onion
* MongoDb
    * engine: mongodb
    * host: 127.0.0.1
    * port: 1234
    * collection: onion
