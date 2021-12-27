#!/bin/sh

echo "running on port 8080 sever.py and the client.py" 

python3 server.py &
python3 client.py 


echo "press Enter key to continue" 

read varname