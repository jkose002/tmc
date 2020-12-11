from flask import ( g, redirect, url_for )
from tmc.db import get_db

# Insert relation adversary per tool
def insert_adversary_x_event(adversary_id, event_id):
    author_id = g.user['id']

    g.db = get_db()
    query='INSERT INTO {} ({}, {}, {}) VALUES (?, ?, ?)'.format('adversaries_x_events', 'author_id', 'adversary_id', 'event_id')

    result = g.db.execute(query, (author_id, adversary_id, event_id))
    g.db.commit()
    element_id = result.lastrowid

    return element_id