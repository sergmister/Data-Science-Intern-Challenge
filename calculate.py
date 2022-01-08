import csv


if __name__ == "__main__":
    with open("dataset.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0

        total_orders = 0
        total_items_sum = 0
        order_amount_sum = 0

        total_orders_small = 0
        total_items_sum_small = 0
        order_amount_sum_small = 0

        for row in csv_reader:
            if line_count == 0:
                pass
            else:
                order_amount = int(row[3])
                total_items = int(row[4])

                total_orders += 1
                total_items_sum += total_items
                order_amount_sum += order_amount

                if total_items < 10:
                    total_orders_small += 1
                    total_items_sum_small += total_items
                    order_amount_sum_small += order_amount

            line_count += 1

        print(f"Average Order Value: ${order_amount_sum / total_orders:.2f}")
        print(f"Average Value per Ordered Item: ${order_amount_sum / total_items_sum:.2f}")
        print(f"Average Order Value of orders under 10 items: ${order_amount_sum_small / total_orders_small:.2f}")
