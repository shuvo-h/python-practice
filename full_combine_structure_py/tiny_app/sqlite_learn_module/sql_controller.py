# from .sql_service import insertSingleDoc
from . import sql_service

def insertSingleDocCtl(bodyDataDict):
    result = sql_service.insertSingleDoc(bodyDataDict)
    return result,201


def getAllDocsCtl(query_params):
    result = sql_service.get_all_docs_fromDb(query_params)
    return result,200

def insertPetWithRefCtl(bodyDataDict):
    result = sql_service.insertPetWithRefDoc(bodyDataDict)
    return result,201

def retrivedPetListWithPeople():
    result = sql_service.getPetList()
    return result,200