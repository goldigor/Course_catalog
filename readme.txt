The Course catalog app link: http://goldigor.pythonanywhere.com/
---------------------------------------------

Create a virtual environment and activate it:
python -m venv course_catalog_venv
source course_catalog_venv\Scriptes\activate


Install the packages:
pip install -r requirements.txt


Lunch migration script:
python manage.py migrate catalog


Run the server:
python manage.py runserver



