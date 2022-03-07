# AIRBNB CLONE
![image](https://user-images.githubusercontent.com/73969861/156969348-4eb599dd-b1b1-4a64-a04a-e5a9f4e183da.png)
This web application is composed by:
* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)
# 1. Console
With this command interpreter you can:
* create your data model
* manage (create, update, destroy, etc) objects
* store and persist objects to a file (JSON file)
## How to clone
```
git clone https://github.com/humtej1204/AirBnB_clone
```
## Usage
```
./console.py
```
In the console you can use the following commands:
Command |First usage <img width=300/>|Second Usage <img width=300/>|Description
---|---|---|---
help|`help <command>`||Prints a description about the command
quit|`quit`||Exits the console
create|`create <class name>`|`<class name>.create()`|Creates a class instance, saves it to the JSON file and prints the id
show|`show <class name> <id>`|`<class name>.show(<id>)`|Prints the string representation of an instance based on the class name and id
destroy|`destroy <class name> <id>`|`<class name>.destroy(<id>)`|Deletes an instance based on the class name and id (save the change into the JSON file)
all|`all <class name>`|`<class name>.all()`|Prints all string representation of all instances based or not on the class name
update|`update <class name> <id> <attribute> <value>`|`<class name>.update(<id>, <attribute>, <value>)`|Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)
count|`count <class name>`|`<class name>.count()`|Prints the amount of a class instances

You can manage the following classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

For example:
```
$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)
```
## Authors
* Michael Chambilla - [GitHub](https://github.com/Mcfreestyle)
* Humberto Tejada - [GitHub](https://github.com/humtej1204)
