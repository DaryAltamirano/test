import datetime
from flask import Blueprint, request
from src.controllers.Product import Product as ProductController

routeProduct = Blueprint("Product", __name__)

'''
    Routes for Product controller 
'''

@routeProduct.route('/', methods=["GET"])
def getAll():
    return ProductController.getAll() 

@routeProduct.route('/<id>', methods=["GET"])
def getOne(id):
    return ProductController.getOne(id) 

@routeProduct.route('/', methods=['POST'])
def create():
    return ProductController.create(request.form) 

@routeProduct.route('/<id>', methods=['PUT'])
def update(id):
    return ProductController.update(id, request.form) 

@routeProduct.route('/<id>', methods=['DELETE'])
def delete(id):
    return ProductController.delete(id) 