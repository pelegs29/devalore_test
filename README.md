# Devalore Test
this guide will go through how to run and test this small python program which fetching rates from exchangerates_data api

### 1. install docker
the first step will be to install docker on your machine, in the docker main website there is a detailed guide on how to install docker on your machine, you can find it [here](https://docs.docker.com/get-docker/)

### 2. run Jenkins on your docker
after installing docker, you can run Jenkins on your docker by running the following command:
```bash
docker run -d -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```

The first time you boot Jenkins, the Docker logs will contain a message like this:
```bash
Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

1883c809f01b4ed585fb5c3e0156543a

This may also be found at: /var/jenkins_home/secrets/initialAdminPassword
```

That random string of numbers and letters is the initial administrator password, which is required to complete the Jenkins configuration.

Open http://localhost:8080 in your browser and enter the password from the Docker logs. You will be prompted to install additional plugins. You can install the suggested plugins or select specific plugins to install. Once the installation is complete, you will be prompted to create an admin user.

### 3. install python and pip on your docker
after running Jenkins on your docker, you will need to install python and pip on your docker, you can do that by running the following command:

first of all you will need your container id, you can get it by running the following command:
```bash
docker ps
```

then you can install python and pip by running the following command:

```bash
docker exec -it <container_id> bash
```
```bash
apt-get update
```
```bash
apt-get install python3
```
```bash
apt-get install python3-pip
```


### 4. install python packages
you will need to install the following python packages: requests, pytest using the following commands on your docker:
```bash
pip3 install requests
```
```bash
pip3 install pytest
```

### 5. back to Jenkins - install Jenkins plugins
you will need to install the following Jenkins plugins: ShiningPanda Plugin
go to Jenkins dashboard, then click on manage jenkins, then click on manage plugins, then click on available tab, then search for ShiningPanda Plugin and install it
this will allow you to run python scripts on Jenkins


### 6. create a new job
after installing python and pip on your docker, you can go back to Jenkins and create a new job, you can do that by clicking on the "New Item" button on the left side of the screen, then you can give your job a name and select "Freestyle project" and click on "OK" button.
under Source Code Management section, you can select Git and paste the following url:
```bash
https://github.com/pelegs29/devalore_test.git
```
and make sure Branch Specifier is set to */master

then under Build section, you can select "Add build step" and select "Python Builder" and paste the following command:
```bash
python3 -m pytest
```
and click on "Save" button

### 7. run the job
after creating the job, you can run it by clicking on the "Build Now" button on the left side of the screen,
you can see the build status on the left side of the screen, if the build is successful, you will see a green check mark,
by pressing the green check mark, you can see the build console output, you can see the test results there :
![image](https://user-images.githubusercontent.com/80215741/201642979-a8bdb2b6-46ef-4f11-aed0-7959f9c27631.png)

that's all, thank you for reading this guide !
