## Medical Appointment 

```

#Clone the repo👾 https://github.com/DJGuruji/MedicalAppointment 

#Open The Folder📂 cd MedicalAppointment

#create virtual environment

python -m venv <venv name>

#Activate venv
source <your venv name>/bin/activate

#Install requirements🎯
pip install -r requirements.txt

#include a .env file having smtp for django and secret key for django and debug = False

#SECRET_KEY=give django secret key here

#DEBUG=False

#EMAIL_HOST=smtp.gmail.com
#EMAIL_PORT=587
#EMAIL_USE_TLS=True
#EMAIL_HOST_USER=give your email which must be registered in developing website
#EMAIL_HOST_PASSWORD='your email password'


#migrate 
 python manage.py migrate

#Finally Run The project by

python manage.py runserver
```