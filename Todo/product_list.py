# Define product data as a list of dictionaries
products = [
    {
        "name": "T-Shirt",
        "price": 19.99,
        "description": "A comfortable and stylish T-shirt.",
        "image_url": "https://www.amazon.com/sspa/click?ie=UTF8&spc=MToxMTkwMzM1NTQxMzkyMDU4OjE3MDkxMDYwOTU6c3BfYXRmOjMwMDEyNjg5MTIyODMwMjo6MDo6&url=%2FTrue-Classic-Staple-6-Pack-X-Large%2Fdp%2FB0BJZ9GT1J%2Fref%3Dsr_1_1_sspa%3Fcrid%3D2T7FUKOKZS60F%26dib%3DeyJ2IjoiMSJ9.u7UMJvadpHc_f_wZiYQu23mXkUuWrUeJwa6sZW6hxYlE5kRo038_Ei5KqAktGh1glYATXbMaMvvTVtrGpW9CEkeAFL5kBJny9ziboRrbmbMBvEE1lzuRtsJFISkGaRU_ssrfB_ObzlqK4RjEXIyJRPME13n4nX18ym53ZU08lFn6CoZwTx9Kckrt921viJjXIayLSBOd3YI0h_T-SNXG-um0jpDTZnK4vfdc6gVOvM0qKiK1RPbTHKD3I3n1i4Aofj2RbfIL5Tt_z328srTcgERnuKvM7QLOtl23JkjjzXM.2zuwPZVLZAcTS10TJXDolZwbmxgZvMCYkS2tjR7cSoY%26dib_tag%3Dse%26keywords%3Dtshirts%2Bshirts%2Bfor%2Bmen%26qid%3D1709106095%26sprefix%3Dtsh%252Caps%252C533%26sr%3D8-1-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1%26smid%3DA3FM5SASE2RH9V"
    },
    {
        "name": "Laptop",
        "price": 799.99,
        "description": "A powerful laptop for work and play.",
        "image_url": "https://example.com/images/laptop.jpg"
    },
    # ... Add more products if desired
]

# Function to display product details in a formatted string
def display_product(product):
    return f"""
    **Name:** {product["name"]}
    **Price:** ${product["price"]:.2f}
    **Description:** {product["description"]}
    **Image:** {product["image_url"]}
    """

# Loop through products and display them
for product in products:
    print(display_product(product))
    print("-" * 50)  # Separator between products
