from ext import app


if __name__ == "__main__":
    from routes import index,contact,reviews,signin,signup,services,products
    app.run(debug=True)


# contact_list = []