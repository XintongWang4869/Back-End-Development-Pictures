# Picture Service with Flask

This project is a microservice that contains the RESTful APIs for listing, creating, updating, and deleting picture resources.

 ## Major Steps in Skills Network Labs

 1. Setup the development environment
```
bash ./bin/setup.sh
exit
```

2. Run the flask server in development mode: `flask run --debugger --reload`
3. Complete the code for each endpoint
4. Run `pytest` and pass all tests.

<br>

## Deploy to IBM Code Engine

1. In Skills Network Labs, start Code Engine and create a project.
2. Build and tag the docker image: `docker build -t us.icr.io/$SN_ICR_NAMESPACE/pictures:1 .`
3. Push image to IBM Cloud Container Registry `docker push us.icr.io/$SN_ICR_NAMESPACE/pictures:1`
4. Deploy the application: `ibmcloud ce app create --name pictures  --image us.icr.io/${SN_ICR_NAMESPACE}/pictures:1 --registry-secret icr-secret --port 3000`
5. Check the app URL: `ibmcloud ce application list`
