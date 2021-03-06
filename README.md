# Problem

This project identifies occupations and states with the most number of approved H1B visas by analysing immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years.

Data Source: [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis)

Given input data, this project can easily calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

## Input data format
The input data file is .csv file with a semicolon separated (";").

The first line is the names of all columns. Different input data may have different columns names. The remaining lines are the repective values.

### Example
`./input/h1b_input.csv`:
```
;CASE_NUMBER;CASE_STATUS;CASE_SUBMITTED;DECISION_DATE;VISA_CLASS;EMPLOYMENT_START_DATE;EMPLOYMENT_END_DATE;EMPLOYER_NAME;EMPLOYER_BUSINESS_DBA;EMPLOYER_ADDRESS;EMPLOYER_CITY;EMPLOYER_STATE;EMPLOYER_POSTAL_CODE;EMPLOYER_COUNTRY;EMPLOYER_PROVINCE;EMPLOYER_PHONE;EMPLOYER_PHONE_EXT;AGENT_REPRESENTING_EMPLOYER;AGENT_ATTORNEY_NAME;AGENT_ATTORNEY_CITY;AGENT_ATTORNEY_STATE;JOB_TITLE;SOC_CODE;SOC_NAME;NAICS_CODE;TOTAL_WORKERS;NEW_EMPLOYMENT;CONTINUED_EMPLOYMENT;CHANGE_PREVIOUS_EMPLOYMENT;NEW_CONCURRENT_EMP;CHANGE_EMPLOYER;AMENDED_PETITION;FULL_TIME_POSITION;PREVAILING_WAGE;PW_UNIT_OF_PAY;PW_WAGE_LEVEL;PW_SOURCE;PW_SOURCE_YEAR;PW_SOURCE_OTHER;WAGE_RATE_OF_PAY_FROM;WAGE_RATE_OF_PAY_TO;WAGE_UNIT_OF_PAY;H1B_DEPENDENT;WILLFUL_VIOLATOR;SUPPORT_H1B;LABOR_CON_AGREE;PUBLIC_DISCLOSURE_LOCATION;WORKSITE_CITY;WORKSITE_COUNTY;WORKSITE_STATE;WORKSITE_POSTAL_CODE;ORIGINAL_CERT_DATE
0;I-200-18026-338377;CERTIFIED;2018-01-29;2018-02-02;H-1B;2018-07-28;2021-07-27;MICROSOFT CORPORATION;;1 MICROSOFT WAY;REDMOND;WA;98052;UNITED STATES OF AMERICA;;4258828080;;N;",";;;SOFTWARE ENGINEER;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";51121.0;1;0;1;0;0;0;0;Y;112549.0;Year;Level II;OES;2017.0;OFLC ONLINE DATA CENTER;143915.0;0.0;Year;N;N;;;;REDMOND;KING;WA;98052;
1;I-200-17296-353451;CERTIFIED;2017-10-23;2017-10-27;H-1B;2017-11-06;2020-11-06;ERNST & YOUNG U.S. LLP;;200 PLAZA DRIVE;SECAUCUS;NJ;07094;UNITED STATES OF AMERICA;;2018723003;;Y;"BRADSHAW, MELANIE";TORONTO;;TAX SENIOR;13-2011;ACCOUNTANTS AND AUDITORS;541211.0;1;0;0;0;0;1;0;Y;79976.0;Year;Level II;OES;2017.0;OFLC ONLINE DATA CENTER;100000.0;0.0;Year;N;N;;;;SANTA CLARA;SAN JOSE;CA;95110;
2;I-200-18242-524477;CERTIFIED;2018-08-30;2018-09-06;H-1B;2018-09-10;2021-09-09;LOGIXHUB LLC;;320 DECKER DRIVE;IRVING;TX;75062;UNITED STATES OF AMERICA;;2145419305;;N;",";;;DATABASE ADMINISTRATOR;15-1141;DATABASE ADMINISTRATORS;541511.0;1;0;0;0;0;1;0;Y;77792.0;Year;Level II;OES;2018.0;OFLC ONLINE DATA CENTER;78240.0;0.0;Year;N;N;;;;IRVING;DALLAS;TX;75062;
3;I-200-18070-575236;CERTIFIED;;2018-03-30;H-1B;2018-09-10;2021-09-09;"HEXAWARE TECHNOLOGIES, INC.";;101 WOOD AVENUE SOUTH;ISELIN;NJ;08830;UNITED STATES OF AMERICA;;6094096950;;Y;"DUTOT, CHRISTOPHER";TROY;MI;SOFTWARE ENGINEER;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";541511.0;5;5;0;0;0;0;0;Y;84406.0;Year;Level II;OES;2017.0;OFLC ONLINE DATA CENTER;84406.0;85000.0;Year;Y;N;Y;;;NEW CASTLE;NEW CASTLE;DE;19720;
4;I-200-18243-850522;CERTIFIED;2018-08-31;2018-09-07;H-1B;2018-09-07;2021-09-06;"ECLOUD LABS,INC.";;120 S WOOD AVENUE;ISELIN;NJ;08830;UNITED STATES OF AMERICA;;7327501323;;Y;"ALLEN, THOMAS";EDISON;NJ;MICROSOFT DYNAMICS CRM APPLICATION DEVELOPER;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";541511.0;1;0;0;0;0;0;1;Y;87714.0;Year;Level III;OES;2018.0;OFLC ONLINE DATA CENTER;95000.0;0.0;Year;Y;N;Y;Y;;BIRMINGHAM;SHELBY;AL;35244;
5;I-200-18142-939501;CERTIFIED;2018-05-22;2018-05-29;H-1B;2018-05-29;2021-05-28;OBERON IT;;1404 W WALNUT HILL LN;IRVING;TX;75038;UNITED STATES OF AMERICA;;8666609190;;Y;"GARRITSON, JAMES";RICHARDSON;TX;SENIOR SYSTEM ARCHITECT;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";541511.0;1;0;0;0;0;0;1;Y;71864.0;Year;Level II;Other;2017.0;OFLC ONLINE DATA CENTER;74000.0;0.0;Year;Y;N;Y;;;SUNRISE;BROWARD;FL;33323;
6;I-200-18121-552858;CERTIFIED;2018-05-01;2018-05-07;H-1B;2018-05-02;2018-10-26;ICONSOFT INC.;;101 CAMBRIDGE STREET SUITE 360;BURLINGTON;MA;01803;UNITED STATES OF AMERICA;;8882054614;1;N;",";;;SENIOR ORACLE ADF DEVELOPER;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";541511.0;1;0;1;0;0;0;0;Y;92331.0;Year;Level III;Other;2017.0;OFLC ONLINE DATA CENTER;114000.0;0.0;Year;Y;N;Y;;;JACKSONVILLE;DUVAL COUNTY;FL;32202;
7;I-200-18215-849606;CERTIFIED;2018-08-03;2018-08-09;H-1B;2018-08-11;2021-08-11;COGNIZANT TECHNOLOGY SOLUTIONS US CORP;;211 QUALITY CIRCLE;COLLEGE STATION;TX;77845;UNITED STATES OF AMERICA;;2019661249;;N;",";;;SENIOR SYSTEMS ANALYST JC60;15-1121;COMPUTER SYSTEMS ANALYST;541512.0;1;0;1;0;0;0;0;Y;80579.0;Year;Level II;OES;2018.0;OFLC ONLINE DATA CENTER;80579.0;0.0;Year;Y;N;Y;;;OWINGS MILLS;BALTIMORE;MD;21117;
8;I-201-17339-472823;CERTIFIED;2017-12-08;2017-12-14;H-1B1 Chile;2017-12-08;2019-06-07;ISHI SYSTEMS INC;;185 HUDSON STREET;JERSEY CITY;NJ;07311;UNITED STATES OF AMERICA;;2013326900;;N;",";;;ASSOCIATE PRODUCT MANAGER(15-1199.09);15-1199;"COMPUTER OCCUPATIONS, ALL OTHER";541511.0;1;0;1;0;0;0;0;Y;88317.0;Year;Level III;OES;2017.0;OFLC ONLINE DATA CENTER;90000.0;0.0;Year;;;;;;JERSEY CITY;HUDSON;NJ;07311;
9;I-200-18233-239931;CERTIFIED;2018-08-21;2018-08-27;H-1B;2018-09-05;2021-09-04;"WB SOLUTIONS, LLC";;7320 E FLETCHER AVE;TAMPA;FL;33637;UNITED STATES OF AMERICA;;8133300099;;Y;"KIDAMBI, VAMAN";TRUMBULL;CT;SENIOR JAVA DEVELOPER;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";541511.0;1;0;0;0;0;1;0;Y;104790.0;Year;Level III;OES;2018.0;OFLC ONLINE DATA CENTER;105000.0;0.0;Year;Y;N;Y;Y;;ALPHARETTA;FULTON;GA;30005;
```

## Output data format
This project will create 2 output files:
* `top_10_occupations.txt`: Top 10 occupations for certified visa applications
* `top_10_states.txt`: Top 10 states for certified visa applications

Each line holds one record and each field on each line is separated by a semicolon (;).

### Example
`./output/top_10_occupations.txt`:
```
TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
SOFTWARE DEVELOPERS, APPLICATIONS;6;60.0%
ACCOUNTANTS AND AUDITORS;1;10.0%
COMPUTER OCCUPATIONS, ALL OTHER;1;10.0% 
COMPUTER SYSTEMS ANALYST;1;10.0%
DATABASE ADMINISTRATORS;1;10.0%
```
`./output/top_10_states.txt`:
```
TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
FL;2;20.0%
AL;1;10.0%
CA;1;10.0%
DE;1;10.0%
GA;1;10.0%
MD;1;10.0%
NJ;1;10.0%
TX;1;10.0%
WA;1;10.0%
``` 

# Approach

For this project, I choose Python because of its convenience of reading and writing files.

## Data Process

### Semicolon

The input data file has the a semicolon separated (";"), but I found that there exists semicolons which is not a separated sign in the data file.

#### Example
```
;4342279239;;ROEPER, JENNIFER;TAMPA;FL;"PRESIDENT &AMP; CHIEF EXECUTIVE OFFICER";11-1011;
```

Therefore, we have to remove such a semicolon. They often follows "&AMP", so we can replace all such semicolons with another sign.

### Column names

Since data in different year has different format and they have different column names.

To calculate two metrics described above, we need three columns: `Status`, `State`, and `Occupation`.

I collect all possible column names for these three columns in the data from 2008 to 2018.

* `Status`:  "CASE_STATUS", "STATUS", "APPROVAL_STATUS"
* `State`: "WORKSITE_STATE", "LCA_CASE_WORKLOC1_STATE", "STATE_1"
* `Occupation`: "SOC_NAME", "LCA_CASE_SOC_NAME", "OCCUPATION_TITLE"

If there is a new data format and new column names for these three columns, we should add them in the code.

## Data Structure

1. I use a dictionary to record the name and count when I read input data file line by line.
2. I defind a class called Object to store respective name and count of occupations and states.
3. I use a heap and keep its size not exceed 10. In this case, I can find the top 10 objects in this heap with time complexity of O(nlogk).

## Algorithm

Find the top k elements of n objects:

keep a heap with size of k, put objects into the heap one by one. When the size of heap is more than k, we just pop one element.

Time Complexity: O(nlogk)

In this case, we want to find 10 largest elements which means k = 10. Therefore, we should build a min heap so that we can ganrantee elements in the heap are larger than others, because everytime we pop out the smallest element in the heap.

## Arguments Parse

I use argparse package to parse arguments which is inputed in the command line.

# Run

## Instructions

1. You should put the input data file `h1b_input.csv` into the `input` file.
2. Open the terminal and go to the directory which contains `run.sh`.
3. Run the bash script in the terminal.
```
./run/sh
```
You can see the output file `top_10_occupations.txt` and `top_10_states.txt` in the `output` file.

## Testing
I put three tests in the `/insight_testsuite/tests` file.
If we want to add more tests, we can just add it to this file.

1. Open the terminal and go to the directory which contains `run_tests.sh`.
2. Run the bash script in the terminal.
```
./run_tests/sh
```
You can see the information about tests in the terminal.
