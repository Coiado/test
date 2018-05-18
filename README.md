# Data Engineering Project OUAP-4314 : Historic monuments of Paris

This project is a project done during the 4th year of engineering school at ESIEE Paris.</br>
We scrap and store data in a database from the website : http://www2.culture.gouv.fr/public/mistral/dapamer_fr?ACTION=RETROUVER_TITLE&LEVEL=1&GRP=0&REQ=((paris)%3aLOCA%2cPLOC). Then we will be able to query this database to get specific informations and values.

## First steps

### Git

* First of all clone this project to your work area, with the follow command:

```
$ git clone https://github.com/Coiado/OUAP4314_Projet_Sujet1.git
```

### Docker

* At first, be sure you have docker install in your computer and you are logged in docker, to run docker in mac or windows you need to use docker toolbox, to see more details give a look here [here](https://docs.docker.com/toolbox/overview/ )

> Then, type follow command to create a mongo container that will be our database
```
$ docker run -d --name mongodb mongo
```

* Be sure the name of your container is mongodb, otherwise the program will not work

> Now you have to create the flask container, but at first use the dockefile to create an image called flask, so go to the file Flask, and use the follow comand:
```
$ docker build -t flask .
```

> And then create the container:
```
$ docker run -p 5000 --name flask --link mongodb:mongo flask
```

> With this process you now could see your webaplication running in your "localhost:5000". But there will not have any monument in your web aplication.

> To scrapy the data for the web, we need to do the same process that we did with scrapy, so open other terminal, go to scrapy folder and create the image:
```
$ docker build -t scrapy .
```

>  And create your container :
```
$ docker run --name scrapy --link mongodb:mongo scrapy
```
In this way refresh your browser and you will see all the monuments took in the website


## Explaination

The web application is coded with the Python framework __Flask__ and we use three dockers containers to run this application
One for flask; other for mongodb and another to scrapy our data.
So we use Scrapy to get Informations about historic monuments of Paris from the website http://www2.culture.gouv.fr/public/mistral/dapamer_fr?ACTION=RETROUVER_TITLE&LEVEL=1&GRP=0&REQ=((paris)%3aLOCA%2cPLOC) 
and stored in our own database. More details about those framework could be see in next links.


## Built with

* [Docker](https://hub.docker.com/) - Containerization
* [Flask](flask.pocoo.org/) - Build web application
* [Scrappy](https://scrapy.org/) - Scrapping framework
* [MongoDB](https://www.mongodb.com/fr/) - Data store



## Group project members

* **Clément BERRURIER** 
* **Alexis CHARVET** 
* **Lucas COIADO MOTA**
* **Hung Hoang DANG**


