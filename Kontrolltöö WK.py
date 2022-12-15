def money_euros(num_buckets: int, price_per_kilo: int) -> float:
    euros = num_buckets * 5 * (price_per_kilo / 100)
    return round(euros, 1)

if __name__ == '__main__':
    boxes_picked = [14, 15, 16, 15, 14, 14, 10]

    total_boxes = sum(boxes_picked)
    price_per_kilo = int(input("Sisestage maasikakilo hind sentides: "))
    kokku = 245.0
    total_euros = 0
for boxes in boxes_picked:
    euros = money_euros(boxes, price_per_kilo)
    print(f"Mart sai {euros} eurot {boxes} kastide maasikate eest.")
    total_euros += euros


print(f"Kokku sai: {kokku} eurot.")