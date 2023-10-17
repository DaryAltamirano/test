from marshmallow import Schema, fields, ValidationError

PRICE_SIZE = 2

def validatePrice(n):
    '''Validation for price.

    Parameters:
        n (price): price value.
    '''

    if len(str(n)) != PRICE_SIZE:
        raise ValidationError("invalid size for price")

class ProductSchema(Schema):
    '''
        Schema to validate for request information
    '''
    price = fields.Integer(validate=validatePrice, required=True)
    name = fields.Str(required=True, error_messages={"required": "Name is required."})
