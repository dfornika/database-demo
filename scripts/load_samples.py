#!/usr/bin/env python3

import argparse
import csv
import datetime
import glob
import json
import os
import re

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import database_demo.crud as crud
import database_demo.models as models


def create_db_session(db_url):
    """
    """
    engine = create_engine(
        db_url, connect_args={"check_same_thread": False}
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    session = SessionLocal()

    return session


def parse_samples_csv(samples_csv_path):
    """
    """
    samples = []
    with open(samples_csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            samples.append(row)

    return samples


def main(args):
    db_url = "sqlite:///" + args.db
    db = create_db_session(db_url)

    samples = parse_samples_csv(args.input)

    crud.create_samples(db, samples)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('--db')
    args = parser.parse_args()
    main(args)
