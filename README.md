# pythonapprds
In this Repo I have added my python application which will read the data from user and will add it to Redis Cluster and RDS Postgress SQL
Code will take a Password to connect with RDS and Redis from AWS Secret Manager.
app.py has a Python code
requirement.txt will contain all the required application, Dockerfile will pull the information from this and will install these requirment
utils.py has a seprate get secret value code and will be called from app.py
buildspec.yml is a file for code build ued to build the image.
