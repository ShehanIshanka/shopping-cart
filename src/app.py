from flask import Flask
from src.bootstrap import bootstrap_database, initialize_services
from src.routers.v1 import cart, product, swagger

app: Flask = Flask(__name__)
app.register_blueprint(product.products)
app.register_blueprint(cart.carts)
app.register_blueprint(swagger.swagger_ui)

db = bootstrap_database()
initialize_services(db, app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
