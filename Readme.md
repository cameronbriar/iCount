## iCount

This simple Django app allows you to create __counters__.

#### What is a counter?
A counter is a text label with an integer value. The value can increase or decrease. Counters can be added, removed and updated.

#### Why?
I needed to count every outlet in my home. This helped me easily count the number of each outlet type in my home. (e.g. dual power outlet, dual lightswitch, quad lightswitch, etc...)

#### How to Run

Adjust the directory variables and create a SECRET_KEY in iCount/settings.py, then run:


    python manage.py runserver 0.0.0.0:8000


Visit http://0.0.0.0:8000/count in your browser and start counting!
