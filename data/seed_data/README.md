# Seed Data

Exactly 1000 rows are generated.

| Table | Rows |
|---|---:|
| User | 50 |
| Receipt | 120 |
| Ingredient | 300 |
| Instructions | 120 |
| Favorites | 120 |
| Likes_Receipt | 80 |
| Comment | 80 |
| Likes_Comment | 40 |
| Suggestion | 50 |
| Likes_Suggestion | 30 |
| ChatHistory | 10 |
| **Total** | **1000** |

Event is intentionally empty. Recommendations contains one dummy record for testing: `(user_id=1, receipt_id=1, seen=false)`.

Ingredient `unit` values are restricted to:
`g`, `kg`, `ml`, `l`, `tsp`, `tbsp`, `cup`, `piece`

The exact ERD column names are preserved, including:
- `receipt_id`
- `user_id`
- `isAssigned`
- `isApproved`
- `ChatHistory`
- `Instructions`
- `Likes_Receipt`
- `Likes_Comment`
- `Likes_Suggestion`

The SQL file is ready for MySQL import after the tables have been created.
