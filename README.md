# database-demo

This is a small demo application that shows how to create a database-based application using [SQLAlchemy](https://www.sqlalchemy.org)
and [alembic](https://alembic.sqlalchemy.org).

## Getting Started

Clone this repo:
```
git clone git@github.com:dfornika/database-demo.git
cd database-demo
```

Create a conda env to install the dependencies into, and activate it:
```
conda create -n database-demo python=3
conda activate database-demo
```

Install this project and its dependencies in 'editable' mode:
```
pip install -e .
```

Create a directory named `alembic`. This is where our database 'migration' files will be written:
```
mkdir alembic
```

## Defining our Models

The `database_demo/models.py` file is where we will define our models, which correspond to our database tables. The file is
pre-populated with a basic `Sample` model.

```python
class Sample(Base):
    __tablename__ = "sample"

    id = Column(Integer, primary_key=True)
    sample_id = Column(String)
```

You can add more fields to the `Sample` model using the appropriate SQLAlchemy class (`String`, `Integer`, `Float`, `Date`, etc.).

You can also add more model classes to this file, following the same pattern as we've used for the `Sample` class. For example:

```python
class MyNewEntity(Base):
    __tablename__ = "my_new_entity"

    id = Column(Integer, primary_key=True)
    entity_id = Column(String)
    size = Column(Float)
    weight = Column(Float)
    some_significant_date = Column(Date)
```

## Updating the Database Schema
Use the `regen_db.sh` script to:

1. Delete your existing copy of the db.
2. Delete any existing migration files from the `alembic` directory.
3. Generate a new 'migration' file in the `alembic` directory.
4. Apply the migration to set up the database schema in a new copy of the db.

**Note**: This script is a handy way of refreshing your database structure when you are early in the
database development process. Once a database schema has been established, we would keep our migration files
and add new ones when changes are made to the database schema.
