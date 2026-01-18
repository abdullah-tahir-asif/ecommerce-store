import requests
from flask import Flask, render_template,  redirect, url_for, session, request, Response

app = Flask(__name__)
app.secret_key="1234"

products=[
    {"id":1, "name":"2 Piece Khaddar (Pret)","price":4999},
    {"id":2, "name":"Slub Khaddar suit-Embroidered (Pret)","price":4999},
    {"id":3, "name":"Slub Khaddar suit (Pret)","price":4999},
    {"id":4, "name":"3 Piece Slub Khaddar Suit-Embroidered (Unstitched)","price":4999},
    {"id":5, "name":"3 Piece Slub Khaddar Suit-Embroidered (Unstitched)","price":4999},
    {"id":6, "name":"3 Piece Slub Khaddar Suit-Embroidered (Unstitched)","price":4999},
    {"id":7, "name":"Cotton suit","price":4999},
    {"id":8, "name":"Wash & Wear suit","price":4999},
    {"id":9, "name":"Satin suit","price":4999},
    {"id":10, "name":"Regular Fit Tees","price":4999},
    {"id":11, "name":"Regular Fit Casual Shirt","price":4999},
     {"id":12, "name":"Regular Fit Casual Shirt","price":4999},
     {"id":13, "name":"Regular Fit Sweater (grey)","price":4999},
    {"id":14, "name":"Regular Fit Sweater (brown)","price":4999},
     {"id":15, "name":"Regular Fit Sweater (zipper)","price":4999},

       {"id":16, "name":"Purpel Coat","price":4999},
    {"id":17, "name":"Blue Prince Coat","price":4999},
     {"id":18, "name":"Brown Casual Coat,","price":4999},

     {"id":19, "name":"Men's Blue Sweatshirt","price":4999},
    {"id":20, "name":"Men's Dark Navy Sweatshirt","price":4999},
     {"id":21, "name":"Men's Fawn Sweatshirt","price":4999},
     
     {"id":22, "name":"Joyous Women's Perfume 100ml","price":4999},
    {"id":23, "name":"Forbidden Unisex Perfume 100ML","price":4999},
     {"id":24, "name":"Monarc Men's Perfume 100ML","price":4999}
]




# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')



# Route for the stitched page
@app.route('/stitched')
def stitched():
    return render_template('stitched.html')

# Route for the unstitched page
@app.route('/unstitched')
def unstitched():
    return render_template('unstitched.html')

# Route for the unstitched page
@app.route('/shalwar_kameez')
def shalwar_kameez():
    return render_template('shalwar_kameez.html')


# Route for the western page
@app.route('/western')
def western():
    return render_template('western.html')

# Route for the sweaters page
@app.route('/sweaters')
def sweaters():
    return render_template('sweaters.html')

# Route for the coat and blazers
@app.route('/coat')
def coat():
    return render_template('coat.html')

@app.route('/sweatshirt')
def sweatshirt():
    return render_template('sweatshirt.html')

@app.route('/perfume')
def perfume():
    return render_template('perfume.html')






@app.route("/add-to-crat/<int:product_id>")
def adding_to_cart(product_id):
    if "cart" not in session:
        session["cart"]=[]
    session["cart"].append(product_id)
    session.modified=True
    return redirect(url_for("cart"))

@app.route('/cart')
def cart():
    total_price=0
    cart_items=[]
    if "cart" in session:
        for item_id in session["cart"]:

            for product in products:
                if product["id"]==item_id:
                    cart_items.append(product)
                    total_price=total_price+product["price"]
    
    total_item=len(cart_items)
    

    return render_template("cart.html", product=cart_items, total_item=total_item, total_price=total_price)



@app.route("/clear_cart")
def clear():
    session.pop("cart",None)
    return render_template("cart.html")


# login system
@app.route('/signup' ,methods=['GET','POST'])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        # password=request.form.get("password")
        email=request.form.get("email")
        contact=request.form.get("contact")
        

        webhook_url = "https://tahir1.app.n8n.cloud/webhook/2674adf3-3933-4a2a-a7f5-a4f6137abf38"

        data = {
            "name": username,
            "email": email,
            "contact": contact
        }

        requests.post(webhook_url, json=data)
        return render_template("index.html")
       
    return render_template('signup.html')
    


@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


def get_cart_items():
    cart_products = []

    if "cart" in session:
        for item_id in session["cart"]:
            for product in products:
                if product["id"] == item_id:
                    cart_products.append(product)

    return cart_products





@app.route("/buynow",methods=["GET","POST"])
def buy():
    if request.method=="POST":
        name=request.form.get("username")
        phone=request.form.get("phone")
        city=request.form.get("city")
        address=request.form.get("address")
        cart_items= get_cart_items()

        webhook="https://tahir1.app.n8n.cloud/webhook/0ae2f948-bddc-487c-b7c4-9bdff9414bf5"

        data={
            "phone":phone,
            "name":name,
            "city":city,
            "address":address,
            "cart_items":cart_items
        }

        requests.post(webhook,json=data)
        return render_template("thanku.html")

    return render_template("checkout.html")

if __name__ == '__main__':
    app.run(debug=True)



