#Airflow for beginners


## Prerequisite
	- [Install Docker](https://docs.docker.com/engine/install/)
	- [Install docker-compose](https://docs.docker.com/compose/install/)


##How to run airflow in your local
	
	cd to airflow_beginner project and run below command 

	```
	docker-compose up -d
	```
	
	validate the airflow set up is working with following command

	```
	docker ps
	```
	there should be 3 docker containers running one for postgres, scheduler and webserver



##How to see your dag in Airflow GUI
	Add your dags in ~/airflow-beginner/dags folder
	this will automatically reflect in GUI.