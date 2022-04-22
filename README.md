# TEST-INGENOSYA
# DJANGO BACK END
-Créer virtual env => "python -m venv env"

-Activer virtual env => ". .\env\Scripts\activate.bat"

-installer requirements.txt => "pip install -r requirements.txt"

-Configurer votre base de données:(base postgresql)
    =>Manager_user -> settings.py -> DATABASES = {}

-Lancer la migration 

=> "python manage.py runserver makemigration"

=> "python manage.py runserver migrate"

-Run server "python manage.py runserver 127.0.0.1:4641"


# PS
-Toutes les fonctionnalités sont disponibles dans le fichier Test-ing.postman_collection.json (requête pour POSTMAN)

-La requête "Import and save randomUser" enregistre tout les user dupuis randomuser mais en cas de besoin, utiliser "ing_test_fi.sql"