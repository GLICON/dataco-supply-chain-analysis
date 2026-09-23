# Metric definitions

Every number in this project is calculated as defined below. SQL, Python, Excel and Power BI all use these definitions.

Grain: the raw data has one row per ORDER ITEM. Metrics marked "Order" are calculated after grouping by Order Id.

## Volume

| Metric | Formula | Grain | Filter |
|---|---|---|---|
| Order items | Count of rows | Item | All |
| Orders | Count of distinct Order Id | Order | All |
| Customers | Count of distinct Customer Id | Customer | All |
| Products | Count of distinct Product Card Id | Product | All |

## Financial (Q2)

| Metric | Formula | Grain | Filter |
|---|---|---|---|
| Gross sales | Sum of Sales (before discount) | Item | All |
| Discount given | Sum of Order Item Discount | Item | All |
| Revenue | Sum of Order Item Total (after discount) | Item | All |
| Profit | Sum of Order Profit Per Order (item-level profit despite its name) | Item | All |
| Margin % | Profit / Revenue | Item | All |
| Loss-making item | An item where Order Profit Per Order < 0 | Item | All |
| Loss item rate | Loss-making items / all items | Item | All |
| Losses | Sum of profit on loss-making items | Item | All |
| Discount band | Order Item Discount Rate grouped: 0-5%, 6-10%, 11-15%, 16-25% | Item | All |
| Extra profit from a discount cap | Sum of Sales x (Discount Rate - cap), where positive | Item | Calendar 2017 |

## Delivery (Q1)

| Metric | Formula | Grain | Filter |
|---|---|---|---|
| Shipped order | Delivery Status is not "Shipping canceled" | Order | - |
| Late order | Late_delivery_risk = 1 (actual days > scheduled days) | Order | Shipped orders |
| Late rate | Late orders / shipped orders | Order | Shipped orders |
| Promised days | Days for shipment (scheduled) | Order | Shipped orders |
| Actual days | Days for shipping (real) | Order | Shipped orders |
| Shipping delay | Actual days - promised days | Order | Shipped orders |
| Late rate if promises reset | Late rate with First Class promise = 2 days and Second Class = 4 days | Order | Shipped orders |

## Fraud (Q3)

| Metric | Formula | Grain | Filter |
|---|---|---|---|
| Fraud order | Order Status = SUSPECTED_FRAUD | Order | All |
| Fraud rate | Fraud orders / all orders | Order | All |
| Fraud value | Revenue of fraud orders | Order | All |
| Fraud as % of profit | Fraud value / profit, same period | Order | Calendar 2017 |
| Review workload | Orders flagged by a review rule | Order | Calendar 2017 |
| Precision | Fraud orders flagged / all orders flagged | Order | Test period |
| Recall | Fraud orders flagged / all fraud orders | Order | Test period |

## Scope rules and assumptions

1. Delivery metrics exclude cancelled and suspected-fraud orders, because they never shipped.
2. "Last full year" means calendar 2017, because the data ends in January 2018.
3. Revenue always means the amount after discount (Order Item Total), never Sales.
4. Discount-cap estimates assume sales volume stays the same (to be checked in Q2).
5. Currency is US dollars, as in the source data.
6. Fraud models may only use information known before an order ships.