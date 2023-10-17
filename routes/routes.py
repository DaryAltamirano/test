from routes.product import routeProduct


def register(app):
    app.register_blueprint(routeProduct)
