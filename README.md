# NBAStat
A Repository for the Django/Python Implemented Web Page containing NBA Team and player stats.

## Team Members
[Justin Kelly](https://github.com/JustinJKelly)  
[Samuel Gibson](https://github.com/sammgibson)  
[Justin Armbrust](https://github.com/Justin-Armbrust)  
[Kostyantyn Shumishyn](https://github.com/Kshumishyn)  

## Links
[Grepthink](https://www.grepthink.com/project/nbastats/)  
[Trello](https://trello.com/b/1YdRzshT/nba-stat)  

## Documents (Live  Updates)
[Release Plan](https://docs.google.com/document/d/1nJGOxF5GoE3BxtW1B5ujn3DLQTCFF8OjEpv2Y7UUhI4/edit?usp=sharing)  
[Working Prototype Known Problems Report](https://docs.google.com/document/d/1is3xJD_DspNIHmydAzxzgiwd9nEv8kD_E6VHc7KTIwk/edit?usp=sharing)  
[System and Unit Test Report](https://docs.google.com/document/d/1c4oCdJh30i7caVZcQ-TXPTrgJtvE5OPgEl6yDXjRYmw/edit?usp=sharing)  

### Sprint 1:
[Sprint 1 Plan](https://docs.google.com/document/d/1tbNu38Wda2Chr2G6RD29FZIok0ideNPkI4XeGHe6ceg/edit?usp=sharing)  
[Sprint 1 Report](https://docs.google.com/document/d/1VpJ8YTTr0-iarhR6Wa5_Arjf1HhlIie8K5JfZdxIv9c/edit?usp=sharing)  


### Sprint 2:
[Sprint 2 Plan](https://docs.google.com/document/d/1Cy32H088HgJUuOSLkKJtrASwZ8ID_g09SayusXHgvas/edit?usp=sharing)  
[Sprint 2 Report](https://docs.google.com/document/d/1UtFOsaPV_hweyOPeC5Phii_Mb9HpCiFwD0E-VRr7Ihs/edit?usp=sharing)  


### Sprint 3:
[Sprint 3 Plan](https://docs.google.com/document/d/1kdrpzKujRP6eHbeuwFmMqcZQ63IMKpuTDUGNrhRC99w/edit?usp=sharing)  
[Sprint 3 Report](https://docs.google.com/document/d/1RCVtMuMpe9iiU4wDPxOQFqN7wDGbUvd1hxNS1fuReTU/edit?usp=sharing)  


### Sprint 4:
[Sprint 4 Plan](https://docs.google.com/document/d/1COXk3VyuFRoEVnb-JLJxKLkeWnljcLDOGC4WISU71rM/edit?usp=sharing)  
[Sprint 4 Report](https://docs.google.com/document/d/1m1HBcWxZtMXsp5uO9zwWNUdgqFn-AKMY55VpEvKhP8I/edit?usp=sharing)

## Files/Directories  
```  
├── All_Players.json  
├── getAllTeams.py  
├── loadJSON.py  
├── nbaStat  
│   ├── db.sqlite3  
│   ├── fusioncharts.py  
│   ├── manage.py  
│   ├── nbaStat  
│   ├── _nbatest.py  
│   ├── player  
│   ├── __pycache__  
│   └── static  
├── ProjectDocuments  
│   ├── Release Plan.pdf  
│   ├── Sprint #1 Plan.pdf  
│   ├── Sprint #1 Report.pdf  
│   ├── Sprint #2 Plan.pdf  
│   ├── Sprint #2 Report.pdf  
│   ├── Sprint #3 Plan.pdf  
│   ├── Sprint #3 Report.pdf  
│   ├── Sprint #4 Plan.pdf  
│   ├── Sprint #4 Report.pdf  
│   ├── System and Unit Test Report.pdf  
│   └── Working Prototype Known Problems Report.pdf  
├── README.md  
├── team.json  
└── Testing    
```

# Setup and Execution
In order to run our server, it is assumed that at the very least you are using a system capable of installing Python3 and PIP3.

##### 1. Verify system is up to date
If using unix-based system, make sure update repository is up to date.

##### 2. Install python3
Using either command-line, terminal or external interface, download python3 and verify it is installed.

##### 3. Install pip3
In addition to python3, install the pip3 interface, this will be a crucial package manager.

##### 4. Install dependencies
Using some form of command-line or terminal, use the pip3 package manager to download and install the "Django" and "nba_api" packages and verify they have installed correctly.  
`pip3 install Django`  
`pip3 install nba_api`  

##### 5. Update server database and static elements
In the nested nbaStat directory containing manage.py, run the following commands:  
`python3 manage.py collectstatic`  
`python3 manage.py makemigrations`  
`python3 manage.py migrate`  

##### 6. Run server
Begin the server by running the following command:  
`python3 manage.py runserver`  

##### 7. Explore Website
By default the website will be hosted locally on localhost:8000. Navigate to that in a browser and explore the available content.
