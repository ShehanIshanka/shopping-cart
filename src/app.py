from flask import Flask
from src.bootstrap import bootstrap_database, initialize_services
from src.routers.v1 import cart, product


app: Flask = Flask(__name__)
app.register_blueprint(product.products)
app.register_blueprint(cart.carts)

db = bootstrap_database()
initialize_services(db, app)

if __name__ == "__main__":
    app.run(debug=True)
