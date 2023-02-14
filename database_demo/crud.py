import logging

from sqlalchemy import select, delete, and_
from sqlalchemy.orm import Session

from . import models

###### Samples
def get_samples(db: Session):
    """
    """
    samples = db.query(models.Sample)

    return samples

def create_samples(db: Session, samples: list[dict[Object, Object]]):
    """
    Create a set of sample records in the database.

    :param db: Database session.
    :type db: sqlalchemy.orm.Session
    :param samples:
    :type samples: list[dict[Object, Object]]
    :return: None
    :rtype: NoneType
    """
    db_samples = []
    for sample in samples:
        db_sample = models.Sample(
            sample_id = sample["sample_id"],
        )
        db.add(db_sample)

    db.commit()
