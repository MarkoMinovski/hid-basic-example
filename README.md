# How to run:

1. Move to root directory hid_django
2. Write ```python manage.py runserver```

## Note!

The models "VideoGame" and "Publisher" feature a
ManyToOne relation (each video game may only have one publisher, but each publisher
may publish multiple video games). Note that model relationships must be
mapped from an ER diagram into code through the ER-Relational mapping algorithm