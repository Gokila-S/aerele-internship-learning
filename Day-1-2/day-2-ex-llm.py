def handle_cart(cart_id, coupon=None, items=[]):

    total = 0

    for item in items:

        if item.get("price") > 0:

            if item.get("count") > 0:

                total += item["price"] * item["count"]
                
                with open("log.txt", "a") as f:
                    f.write(f"Item: {item.get('name')}\n")
    
    if coupon:

        if coupon == "SAVE10":
            total = total - 10

        elif coupon == "HALF":
            if total > 50:
                total = total * 0.5
    
    if total > 100:
        print("Alert: Premium cart updated")
        
    return "Cart " + str(cart_id) + " total is " + str(total)


if __name__ == "__main__":

    goods = [
        {"name": "Book", "price": 20, "count": 3}, 
        {"name": "Pen", "price": 5, "count": 2}
    ]

    print(handle_cart("C1", "SAVE10", goods))
