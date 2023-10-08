from flask import Flask
from src.bootstrap import bootstrap_database, initialize_product_service
from src.routers.v1 import product


app: Flask = Flask(__name__)
app.register_blueprint(product.products)

db = bootstrap_database()
app.product_service = initialize_product_service(db)

if __name__ == "__main__":
    app.run()
