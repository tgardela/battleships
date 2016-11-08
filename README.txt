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
        <your_dir>\venv\venvBattleships\Scripts\activate.bat
    (Linux):
        source <your_dir>\venv/venvBattleships/bin/activate
        
- go inside battleships/app
    cd battleships
        
- run the manage.py script with 'runserver' option
    (Windows):
        python manage.py runserver
    (Linux):
        ./manage.py runserver
        
- open you faworite internet browser and go to:
    http://localhost:5000/
