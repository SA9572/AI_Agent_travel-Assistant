"""
Budget Estimation Tool (FINAL – Stable & Standalone)

Run:
python -m tools.budget_tool
"""


def estimate_budget(
    flight_price: int,
    hotel_price_per_night: int,
    days: int,
    food_cost_per_day: int = 800,
    local_travel_per_day: int = 500
) -> dict:
    """
    Estimate total trip budget.

    Args:
        flight_price (int): Flight cost
        hotel_price_per_night (int): Hotel cost per night
        days (int): Number of trip days
        food_cost_per_day (int): Daily food cost (default ₹800)
        local_travel_per_day (int): Daily local travel cost (default ₹500)

    Returns:
        dict: Budget breakdown
    """

    if days <= 0:
        return {
            "status": "error",
            "message": "Number of days must be greater than zero"
        }

    hotel_total = hotel_price_per_night * days
    food_total = food_cost_per_day * days
    local_travel_total = local_travel_per_day * days

    total_cost = flight_price + hotel_total + food_total + local_travel_total

    return {
        "status": "success",
        "days": days,
        "breakdown": {
            "flight": flight_price,
            "hotel": hotel_total,
            "food": food_total,
            "local_travel": local_travel_total
        },
        "total_cost": total_cost
    }


# ✅ Terminal output guaranteed
if __name__ == "__main__":
    print(
        estimate_budget(
            flight_price=5356,
            hotel_price_per_night=1232,
            days=3
        )
    )
