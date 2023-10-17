
def serializer(ObjectsModel):
    ''' Returns a serialized object.

    Parameters:
        ObjectsModel (Object): Objects for serialize.

    Returns:
        list: Objects serialize.   
    '''

    if isinstance( ObjectsModel, list ):
        return [Object.to_dict() for Object in ObjectsModel]
  
    return ObjectsModel.to_dict()
