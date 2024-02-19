from tiny_app.sqlite_learn_module.sql_user_model import People
from .sql_pet_model import Pet

from config.database import db
from datetime import datetime
import math

def insertSingleDoc(newUserInfo):
    try:
        name = newUserInfo.get('name')
        email = newUserInfo.get('email')
        password = newUserInfo.get('password')
        date_joined = datetime.utcnow()

        # create the new doc
        newUser = People(name=name,email=email,date_joined=date_joined)

        # make hash and set password
        newUser.set_hashed_password_myModelTils(password)

        db.session.add(newUser)
        db.session.commit()

        # retun the new doc without password
        result = newUser.to_dict_MYTILS()
        result.pop('password',None)
        
        return result

    except Exception as e:
        print(e)
        db.session.rollback()
        return {'message': str(e)}



def get_all_docs_fromDb(query_params):
    try:
        print(query_params)
        # get query values 
        page = int(query_params.get('page',1))
        limit = int(query_params.get('limit',10))
        nameQuery = query_params.get('name')
        emailQuery = query_params.get('email')
        min_date_joined = query_params.get('min_date_joined')
        max_date_joined = query_params.get('max_date_joined')


        # implement filter by query and search
        baseQuery = People.query

        # Construct filter conditions
        filter_conditions = []

        if nameQuery:
            # baseQuery = baseQuery.filter(People.name.like(f'%{nameQuery}%'))
            filter_conditions.append(People.name.like(f'%{nameQuery}%'))
        if emailQuery:
            # baseQuery = baseQuery.filter(People.email.like(f'%{emailQuery}%'))
            filter_conditions.append(People.email.like(f'%{emailQuery}%'))
        if min_date_joined:
            min_date = datetime.strptime(min_date_joined,'%Y-%m-%d').date()
            # baseQuery = baseQuery.filter(People.date_joined >= min_date)
            filter_conditions.append(People.date_joined >= min_date)
        if max_date_joined:
            max_date = datetime.strptime(max_date_joined,'%Y-%m-%d').date()
            # baseQuery = baseQuery.filter(People.date_joined <= max_date)
            filter_conditions.append(People.date_joined <= max_date)
        
        if filter_conditions:
            baseQuery = baseQuery.filter(*filter_conditions)
        
        # get all row instance from db
        # docInstanceList = People.query.all()
        # docInstanceList = baseQuery.order_by(People.name.desc()).all()
        paginated_query = baseQuery.order_by(People.name.desc()).paginate(page=page, per_page=limit, error_out=False)
        print(paginated_query)
        docInstanceList = paginated_query.items
        
        # convert to dictionary for each row
        allPeopleList = [docInstance.to_dict_MYTILS() for docInstance in docInstanceList]

        # get all row with filter
        print(query_params)

        # generate pagination 
        count = baseQuery.count()
        # count = paginated_query.count()
        total_pages = math.ceil(count/limit)

        return {
            "meta":{
                "count": count,
                "limit": limit,
                "page": page,
                "total_pages": total_pages
            },
            "data": allPeopleList
        }
    except Exception as e:
        print(e)
        db.session.rollback()
        return {'err_message': str(e)} 
    


def insertPetWithRefDoc(petInfo):
    try:
        name = petInfo.get('name')
        age = petInfo.get('age')
        owner_id = petInfo.get('owner_id')

        # create the new doc
        newPet = Pet(name=name,age=age,owner_id=owner_id)

        db.session.add(newPet)
        db.session.commit()

        # retun the new doc without password
        result = newPet.to_dict_MYTILS()
        
        return result

    except Exception as e:
        print(e)
        db.session.rollback()
        return {'message': str(e)}



# get all pet list with People info
def getPetList():
    try:
        petInstances = Pet.query.all()
        petDictList = [(petInstance.to_dict_MYTILS()) for petInstance in petInstances]
        return {
            "data": petDictList
        }
    except Exception as e:
        print(e)
        db.session.rollback()
        return {'err_message': str(e)} 