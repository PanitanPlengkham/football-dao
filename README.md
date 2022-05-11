# football-dao
Football Dataset of 50 Players.

## Footballer_data table
| id | footballer_name  | goals_score  | countries| weak_foot |
|--------------|---------|---------------|---------|---------|

1. id - The increment number of the players
2. footballer_name - The name of each players
3. goals_score  - The number of goal that player have score
4. countries - The countries name
5. weak_foot - The foot that footballer is good at.

Countries Dataset of 50 Weapons.

## Countries_data table
| id | countries  | population  | 
|---------|-------------|------------|

1. id - The increment number of the countries
2. countries - The countries name
3. population - The number of population in each countries 


#### Setup
        
        create database from command line
        >>> sqllite3 footballer-data.db < footballer-db.schema

        import the csv file
        >>> sqllite3 footballer-data.db
        .mode csv
        .import data/Footballer_dao_-_Sheet1.csv footballer
        .import data/Countries_data_-_Sheet1.csv countries

#### UML Class Diagram
[UML](../../wiki/uml-class-diagram)

#### Package Diagram
[Package Diagram](../../wiki/package-diagram)

#### Web Service API
[Web Service API](../../wiki/web-service-API)
