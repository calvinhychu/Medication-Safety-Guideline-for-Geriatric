from models import User, Note, Drugclass, Drug
from extensions import db
from medication import *
def create_tables():
    db.create_all()
    for a in drug_classes.keys():
        new_drug_class = Drugclass(name=a, beers_criteria=drug_classes[a][0],
        stopp_start_criteria=drug_classes[a][1])
        try:
            db.session.add(new_drug_class)
            db.session.commit()
        except:
            pass
    for a in medications.keys():
        new_med = Drug(name=a, beers_criteria=medications[a][0],
        stopp_start_criteria=medications[a][1], drug_class_id=medications[a][2])
        try:
            db.session.add(new_med)
            db.session.commit()
        except:
            pass