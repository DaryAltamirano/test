from utils.db import db
from models.product.product import Product as ProductModel  
from src.mappers.productMapper import ProductMapper
from src.validationsRequest.validateProduct import ProductSchema
from src.controllers.Controller import Controller
from utils.serializer import serializer
from marshmallow import Schema, ValidationError

class Product(Controller):
    '''
        Controller for Model Product
    '''

    def getAll():
        '''Returns the all product values.

        Returns:
            tuple: Product objects and status code.   
        '''

        return serializer(ProductModel.query.all()), 200

    def getOne(id):
        ''' Returns the one product value.

        Parameters:
            id (int):Key product.

        Returns:
            tuple: Product objects and status code.   
        '''

        data = ProductModel.query.get(id)
        result = ({'error':'Not exist' }, 400) if data is None else ({'product': serializer(data)}, 200)
        return result

    def create(form):
        '''Create an product object.

        Parameters:
            form (form):Request values object.

        Returns:
            tuple: Product objects and status code.   
        '''

        data = ProductMapper.mapper(form)
        try:
            result = ProductSchema().load(data)
            Product = ProductModel(
                name=result['name'],
                price=result['name']
                )
            db.session.add(Product)
            db.session.commit()
            return {'product': serializer(Product)}, 200 

        except ValidationError as err:
            return {'errors': err.messages}, 400

    def update(id, form):
        '''Updates an product object.

        Parameters:
            form (form):Request values object.
            id (int):Key product.

        Returns:
            tuple: Product objects and status code.   
        '''

        Product = ProductModel.query.get(id)
        data = ProductMapper.mapper(form)

        try:
            result = ProductSchema().load(data)
            Product.name = result['name']
            Product.price = result['price']
            db.session.add(Product)
            db.session.commit()
            return {'product': serializer(Product)}, 200 

        except ValidationError as err:
            return {'errors': err.messages}, 400

    def delete(id):
        '''Removes an Product object.

        Parameters:
            id (int):Key Product.

        Returns:
            tuple: Product objects and status code.   
        '''
        Product = ProductModel.query.get(id)
        db.session.delete(Product)
        db.session.commit()

        return {'product': serializer(Product)}, 200 