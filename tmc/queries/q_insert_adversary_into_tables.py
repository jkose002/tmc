from flask import ( g, redirect, url_for )
from tmc.db import get_db
from attackcti import attack_client
from tmc.auth import login_required
from IPython import embed

# Isert into db from any table
def insert_adversary_into_tables(table, element_id, element_name, element_description, element_identifiers):

    table_id = 'adversary_id'
    table_name = 'adversary_name'
    table_description = 'adversary_description'
    adversary_identifiers = 'adversary_identifiers'
    
    author_id = g.user['id']

    g.db = get_db()
    query='INSERT INTO {} ({}, {}, {}, {}, {}) VALUES (?, ?, ?, ?, ?)'.format(table, 'author_id', table_id, table_name, table_description, adversary_identifiers)
    g.db.execute(query, (author_id, element_id, element_name, element_description, element_identifiers))
    g.db.commit()
    return redirect(url_for('maps.completed'))