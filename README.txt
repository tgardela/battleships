Requirements:
Python 3.4 or newer
Virtualenv

Commands:
- get repository:
    git clone https://github.com/tgardela/battleships
    
- go to the folder containing the dowloaded repo
    cd <path_to_you_downloaded_repo>
    
- create a virtualenv for this project
    virtualenv venvBattleships
    
- run your virtualenv
    (Windows):
        venvBattleships\Scripts\activate
    (Linux):
        venvBattleships\bin\activate
        
- install desired addins for the app in your venv:
    pip install -r "requirements.txt"
        
- go inside battleships/app
    cd battleships
        
- run the manage.py script with 'runserver' option
    (Windows):
        python manage.py runserver
    (Linux):
        ./manage.py runserver
        
- open you faworite internet browser and go to:
    http://localhost:5000/