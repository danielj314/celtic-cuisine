from celticcuisine import db


class Nations(db.model):
    # schema for the Nations model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


#class Recipe  #### needs to be linked to mongodb

#class Users (sql)