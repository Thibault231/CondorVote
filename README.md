# CondorVote

								            CondorVote
								 Voting application for school elections
										
     									Django_Python_Heroku 
										 Python 3.8.3                         

# SUM UP: 
CondorVote is an opensource web application for creating election according to Condorcet principles.
On the home page user can both create a vote-desk ou vote.
If it chooses to vote, it has to enter a ticket's code, then a ballot of the corresponding vote-desk is displayed.
If it chooses to create a vote-desk, it has to create an organizer account then click on "Create a new desk". 
When creating a new vote-desk, a user select for the desk: Entreprise, desk-name, number of voters and the status (Unopen/Open).
A vote-desk has ever the following attributs:
    *school/Compagnie
    *school_class/Desk-name
    *opening_vote
    *closing_vote
    *status
    *winners
    *number_voters
    *tickets_amount
    *candidates

Each vote-desk can be modify and colsulted from the organizer's space, clicking "My account".
The elections results are calculate after the organizer close the desk-vote and select "result" in its  organizer's space.


For organizer login an email adress and a password are required.
For voting no login is requiered.

## Settings:
For developpement only the debug mode and the debug toolbar are activated.
For more informations about program's settings consult the file settings.py in folder "project_CondorVote".

## Librairies:
Python libraries are specified in the file "requirements.txt".

## Running program:
### On the Web:
For running this program on the web connect to https://. 

### On local:
For running it localy:
    1-Install Postgre SQL and create a: database "condor_db" / a superuser "condor".
    2-Install the requirements.txt settings.
    3-Create a file .env like ./condorvote_project/.env
        You have to put inside the fallowing global variables:
        SKEY=                   "your secret key".
        ALLOWED_HOSTS=          "url of the web site for production".
        USER_DB=                "condor" or the name of postgres super user.
        PASSWORD_DB=            "the password for postgreSQL database."
        EMAIL_HOST=             "your email for smtp service" for production only.
        EMAIL_PORT=             "587" for production only.
        EMAIL_HOST_USER=""
        EMAIL_HOST_PASSWORD=""

    4-Create tables within your database using the command "python manage.py migrate" in the consol.
    5-Insert datas in nutella database using the command "python manage.py init_db".
    5-Finally run the program with the command "python manage.py runserver".
The home page is being displayed at local port:8000.

# AUTHOR:
T.Salgues.

# LICENCE:
Projet_8_DjangoNutella is a public project with a public licence.
For more information read the file: license

# CONVENTIONS:
## Python code:
    Python code respect the PEP8 convention.
    Each class have its file.
    
    For docstring apply the following field
    """" <Description>
    <Arguments>
        Arg 1: type (default value, description)
        Arg 2: type (default value, description)
        ...
    <Return>
        Return 1: type (default value, description)
        Return 2: type (default value, description)
        ...
    <Example>
    """

## Tests:
    Tests are running with Django module test and Selenium.
    Each module is tested by a specofic test's file and use constants of config.py to control right answer of the program.

    Test coverage has to be higher than 80%.

    When adding new APP or any modification to initial APP's, please put your tests in the "tests" folder of the appropriate APP. 

## Constants:
    Global constants are contained in te config.py file in "food_selector" folder.
    When adding constants, please respect the type "dict" of those module's objects.
    

# CONTRIBUTIONs:
Source code is on https://github.com/Thibault231/P_8_django_nutella.
Use a  CONTRIBUTING.md type file to contribute.

# CREDITS:
Special thanks for Cyril.C, Openclassrooms and OpenFoodFact.

