import logging
import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(format="%(message)s", level=logging.DEBUG)

# Part 1.
order = pd.read_csv(
    os.path.join(curr_dir, "input_day_2.txt"), sep="x", names=["l", "w", "h"]
)
areas = pd.DataFrame(
    {
        "Side 1": order["l"] * order["w"] * 2,
        "Side 2": order["l"] * order["h"] * 2,
        "Side 3": order["w"] * order["h"] * 2,
    }
)
areas["slack"] = areas.min(axis=1) / 2

logging.info(f"Part 1 - Order size: {int(areas.sum().sum())}")

# Part 2.
ribbon = pd.DataFrame(
    {
        "wrap": (2 * order.sum(axis=1)) - (2 * order.max(axis=1)),
        "bow": order.prod(axis=1),
    }
)

logging.info(f"Part 2 - Ribbon: {ribbon.sum().sum()}")
