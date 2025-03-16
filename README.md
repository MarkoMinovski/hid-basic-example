# How to run:

1. Create postgres_data folder on D drive
   - The mounted volume at D:/postgres_data requires manual creation.
     - Move to the folder via ``cd D:/``
     - Write ``mkdir postgres_data`

2. Move to this project's root directory _hid_django_
   
3. Write ```docker compose up --build```

## Note!

The models "VideoGame" and "Publisher" feature a
ManyToOne relation (each video game may only have one publisher, but each publisher
may publish multiple video games). Note that model relationships must be
mapped from an ER diagram into code through the ER-Relational mapping algorithm

