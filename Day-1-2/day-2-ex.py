from typing import Union, Optional


def calculate_total(items: list[dict[str, Union[str, int, float]]]) -> float:

    total = 0.0

    for item in items:
        price = item.get("price", 0.0)
        count = item.get("count", 0)
        
        if price <= 0 or count <= 0:
            continue
            
        total += price * count

    return total


def apply_coupon(total: float, coupon: Optional[str]) -> float:

    if coupon == "SAVE10":
        return total - 10.0

    if coupon == "HALF" and total > 50:
        return total * 0.5

    return total


def write_log(items: list[dict]) -> None:

    with open("log.txt", "a") as f:

        for item in items:

            if item.get("price", 0) > 0 and item.get("count", 0) > 0:
                f.write(f"Item: {item.get('name')}\n")


def run_pipeline(
    cart_id: str, 
    coupon: Optional[str] = None, 
    items: Optional[list] = None
) -> str:

    safe_items = items if items is not None else []
    
    raw_total = calculate_total(safe_items)

    final_total = apply_coupon(raw_total, coupon)
    
    write_log(safe_items)
    
    if final_total > 100:
        print("Alert: Premium cart updated")
        
    return f"Cart {cart_id} total is {final_total}"


if __name__ == "__main__":

    goods = [
        {"name": "Book", "price": 20, "count": 3}, 
        {"name": "Pen", "price": 5, "count": 2}
    ]

    print(run_pipeline("C1", "SAVE10", goods))
