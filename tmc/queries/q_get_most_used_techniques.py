from flask import ( g, redirect, url_for )
from tmc.db import get_db, make_dicts

# Get list of most used techniques
def get_most_used_techniques():

    db = get_db()
    try:
        db.row_factory = make_dicts
        query = db.execute(
            'SELECT  t.technique_id as \'TechniqueID\', t.technique_name as Technique, count(*) as Hits FROM techniques t \
                inner join tools_x_techniques txt on txt.technique_id=t.id \
                GROUP by t.technique_name \
                ORDER BY Hits Desc').fetchall()
        return query
    except TypeError:
        #embed()
        return False #Change this for something more meaningful -- warning/alert 