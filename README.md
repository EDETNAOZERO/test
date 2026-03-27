# test
Effective Mobile test excercise for DevOps

## How to run it
You need docker engine installed. Cd into the project's directory and run
```
docker compose up -d
```
That's it!

## Check the result
You can use curl from command line to test it's working:
```
curl http://localhost
```
You should see "Hello from Effective Mobile!"

## How it's working
There are two containers: nginx proxy and backend. 
The backend is a simple python script using http.server. It's running on an unprivileged port 8080 to allow not using root. The port is listening only inside the docker bridge networking and not exposed to a host system.
The nginx proxy is a minimal nginx container which serves the 80 port and proxies it to the backend using internal docker bridge networking. 
When you're trying to access localhost with curl, you reach nginx which proxies your request to the backend.
