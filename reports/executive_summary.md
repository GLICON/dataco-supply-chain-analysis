# DataCo Supply Chain – Executive Summary

**Prepared for:** Chief Operating Officer
**Data:** DataCo Smart Supply Chain (public dataset) · 65,752 orders · 180,519 order lines · Jan 2015 – Jan 2018
**Tools:** SQL, Python (pandas), Power BI (DAX)

---

## The headline

DataCo sold **$33.05M** and kept **$3.97M** in profit (a **12.0% margin**). Three problems hold that margin back, and each one has a practical fix:

| Problem | Size | Fix | Impact |
|---|---|---|---|
| Late deliveries | **57.3%** of shipped orders arrive late | Reset the delivery promise for First and Second Class | Late rate falls to **34.3%** |
| Loss-making discounts | **18.7%** of items sell at a loss (**−$3.88M**) | Cap discounts at 10% | **+$1.14M** profit (**+28.9%**) |
| Payment fraud | **$741K** suspected fraud = **18.7% of profit** | Hold bank-transfer orders until payment clears | Catches **100%** of suspected fraud |

---

## Q1. Why are so many deliveries late?

- **36,048 of 62,897** shipped orders (**57.3%**) arrived later than promised, by **1.6 days** on average.
- The problem is the **promise, not the warehouse**. Each shipping mode delivers consistently, but two of them promise faster than they ever deliver:

| Shipping mode | Promised (days) | Actual (days) | Late rate |
|---|---|---|---|
| Same Day | 0 | 0.5 | ~47% |
| First Class | 1 | 2 | **100%** |
| Second Class | 2 | 4 | ~80% |
| Standard Class | 4 | 4 | ~40% |

- First Class is late on **every single order, in every market**, so this is a policy problem rather than a regional one.

**Recommendation:** Change the promised times to match reality: **First Class 2 days, Second Class 4 days**. This alone cuts the late rate from **57.3% to 34.3%** without moving a single parcel faster.

---

## Q2. Where is profit being lost, and do discounts help?

- **18.7%** of items sold at a loss, costing **$3.88M** over the period.
- The average discount is **10.1%** of gross sales.
- **Discounts don't buy volume.** Customers buy about **2.1 units per order line** whether the discount is 0% or 25%, so a bigger discount just gives margin away.
- Revenue is concentrated: the **top 9 products bring in 88.2%** of revenue, so losing any one of them is a real risk.

**Recommendation:** Cap discounts at **10%**. Applied to past orders, this would have added **$1.14M** of profit (**+28.9%**), or about **$367K** in 2017 alone. Then review costs on the loss-making product lines.

---

## Q3. How much does fraud cost, and can we stop it?

- **1,488** orders were flagged as suspected fraud, worth **$741K**, which is **18.7% of total profit**.
- **Every suspected fraud order was paid by bank transfer.** Transfers have an **8.2%** fraud rate; debit, cash and card payments have **0%**.
- Fraud is growing: **$256K in 2017, up 7.1%** on 2016.

**Recommendation:** Hold bank-transfer orders until the payment clears. Tested on the historical data, this rule:

| Measure | Result |
|---|---|
| Fraud caught (recall) | **100%** |
| Orders held for checking | **27.5%** |
| Held orders that are fraud (precision) | **8.2%** (about 1 in 12) |
| Checks needed | about **112 a week** (~3 per working hour) |

---

## Priorities

1. **Fix delivery promises (quick win).** This is a policy change with no cost, and on-time performance improves straight away.
2. **Hold bank-transfer orders.** This protects about $256K a year of profit for roughly 3 checks an hour.
3. **Cap discounts at 10%.** This is the largest profit gain; monitor sales volume for 1–2 quarters to confirm there's no drop.

---

## Method notes and limitations

- **Data leakage avoided:** `delivery_status` was excluded from the fraud analysis because it is set *after* an order is flagged (all fraud orders show "Shipping canceled").
- "Fraud" means orders labelled *suspected fraud* in the source data, not confirmed cases.
- The discount-cap impact assumes sales volume stays the same. The flat units-per-line pattern supports this, but it should be tested in practice.
- The data ends in January 2018, so January 2018 is a partial month.
- This is a portfolio project on a public dataset. DataCo is not a real client.
