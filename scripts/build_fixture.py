"""
Run with:  python manage.py shell < scripts/build_fixture.py
Creates:
  products/fixtures/new_tshirts.json
  (and categories/fixtures/categories.json if you want)
"""
import os, json, random, decimal, itertools
from django.conf import settings
from products.models import Category, Product

# --- CONFIG ----
DEFAULT_DESC = "Premium cotton crew‑neck T‑shirt. 150 gsm, regular fit."
PRICE_RANGE  = (9.99, 24.99)
MEN_PREFIX   = "M‑"
WOMEN_PREFIX = "W‑"
IMAGE_DIR    = settings.MEDIA_ROOT          # absolute path to /media
FIXTURE_OUT  = os.path.join(
    "products", "fixtures", "new_tshirts.json"
)
# ---------------

men_cat   = Category.objects.get(name="mens_tshirts")
women_cat = Category.objects.get(name="womens_tshirts")

def next_sku(counter):          # simple SKU generator
    return f"TSH{counter:04}"

pk_start = (Product.objects.last().pk if Product.objects.exists() else 0) + 1
fixture  = []
counter  = 1

for fname in sorted(os.listdir(IMAGE_DIR)):
    if not fname.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    # crude gender split: odd numbers = men, even = women
    gender_cat = men_cat if counter % 2 else women_cat

    fixture.append(
        {
            "model": "products.product",
            "pk":   pk_start + counter - 1,
            "fields": {
                "category": gender_cat.pk,
                "sku": next_sku(counter),
                "name": f"{'Mens' if gender_cat==men_cat else 'Womens'} T‑Shirt {counter}",
                "description": DEFAULT_DESC,
                "price": str(round(random.uniform(*PRICE_RANGE), 2)),
                "rating": random.randint(4, 5),
                "image": fname
            },
        }
    )
    counter += 1

os.makedirs(os.path.dirname(FIXTURE_OUT), exist_ok=True)
with open(FIXTURE_OUT, "w") as fp:
    json.dump(fixture, fp, indent=2)

print(f"✅  Wrote {len(fixture)} products to {FIXTURE_OUT}")
