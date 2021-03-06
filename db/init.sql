CREATE DATABASE airbnbData;
use airbnbData;

CREATE TABLE IF NOT EXISTS airbnbtbl (
    `id` int AUTO_INCREMENT,
    `City` VARCHAR(20) CHARACTER SET utf8,
    `fldState` VARCHAR(20) CHARACTER SET utf8,
    `ActiveRentals` INT,
    `AverageDailyRate` INT,
    `OccupancyRate` INT,
    `Revenue` INT,
    PRIMARY KEY (`id`)
);
INSERT INTO airbnbtbl (City,fldState,ActiveRentals,AverageDailyRate,OccupancyRate,Revenue) VALUES
    ('Anchorage','Alaska',743,121,70,1470),
    ('Atlanta','Georgia',9078,147,55,1758),
    ('Augusta','Alaska',743,121,70,1470),
    ('Austin','Georgia',9078,147,55,1758),
    ('Bar Harbor','Maine',204,261,81,3728),
    ('Boston','Massachusetts',1524,182,50,1800),
    ('Cape May','New Jersey',585,343,64,4200),
    ('Charlotte','North Carolina',2723,137,59,1694),
    ('Chicago','Illinois',5622,140,50,1359),
    ('Cincinnati','Ohio',1093,117,57,1352),
    ('Colorado Springs','Colorado',1781,149,80,2393),
    ('Dallas','Texas',4172,124,65,1643),
    ('Denver','Colorado',4333,140,76,2030),
    ('Honolulu','Hawaii',5192,176,68,2208),
    ('Houston','Texas',7403,119,56,1329),
    ('Kansas City','Kansas',115,114,70,1666),
    ('Kennebunkport','Maine',130,373,63,3640),
    ('Key West','Florida',1649,350,63,4849),
    ('Lake George','New York',148,295,56,3480),
    ('Las Vegas','Nevada',8232,189,55,2119),
    ('Los Angeles','California',10513,169,60,1948),
    ('Miami','Florida',8754,177,61,2056),
    ('Milwaukee','Wisconsin',1156,121,52,1298),
    ('Minneapolis','Minnesota',1794,125,60,1389),
    ('Myrtle Beach','South Carolina',7633,174,52,1953),
    ('Nashville','Tennessee',5868,217,48,2401),
    ('New Orleans','Louisiana',6532,185,43,1884),
    ('New York City','New York',21098,170,46,1441),
    ('Newport','Rhode Island',636,341,52,3124),
    ('Niagara Falls','New York',222,134,45,1350),
    ('North Conway','New Hampshire',382,304,58,3896),
    ('Orlando','Florida',7262,173,55,1815),
    ('Philadelphia','Pennsylvania',4346,132,50,1340),
    ('Phoenix','Arizona',4058,149,71,1942),
    ('Pittsburgh','Pennsylvania',1243,116,57,1275),
    ('Portland','Oregon',3307,114,71,1460),
    ('Portland','Maine',454,190,73,2495),
    ('Saint Louis','Missouri',1587,109,61,1320),
    ('Salt Lake City','Utah',2161,125,78,1745),
    ('San Antonio','Texas',3701,129,57,1513),
    ('San Diego','California',7970,200,69,2692),
    ('San Jose','California',1766,164,63,1712),
    ('Savannah','Georgia',2319,226,50,2779),
    ('Seattle','Washington',4777,135,65,1530),
    ('Sioux Falls','South Dakota',217,104,67,1360),
    ('Tampa','Florida',3252,132,68,1704),
    ('Virginia Beach','Virginia',1541,306,61,3662),
    ('Washington','District of Columbia',5577,145,50,1442),
    ('Wichita','Kansas',330,99,57,12700);