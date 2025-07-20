# Database Schema

## Table: pokemon_stats
- **id**: Integer, Primary Key, Auto-increment
- **name**: String, Unique, Not Null — Pokémon species name
- **height**: Integer — Height of the Pokémon
- **weight**: Integer — Weight of the Pokémon
- **types**: String — Pokémon types (comma-separated)
- **abilities**: String — Pokémon abilities (comma-separated)
- **hp**: Integer — Hit points
- **attack**: Integer — Attack stat
- **defense**: Integer — Defense stat
- **special_attack**: Integer — Special attack stat
- **special_defense**: Integer — Special defense stat
- **speed**: Integer — Speed stat

---

## Table: predictions
- **id**: Integer, Primary Key, Auto-increment
- **filename**: String, Not Null — Name of the uploaded image file
- **species**: String, Not Null — Predicted species by the model
- **verified**: String, Default 'not_verified' — User feedback: 'correct', 'wrong', 'not_verified'
- **correct_species**: String, Nullable — If 'wrong', user provides the correct species name; else NULL
- **timestamp**: DateTime, Default current UTC time — When the prediction was made

---

> **Note:**
> - For each new table, define a new SQLAlchemy model class with a unique `__tablename__`.
> - Update this file whenever you add or modify tables in the database. 