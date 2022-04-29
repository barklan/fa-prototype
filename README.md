# fa-prototype

Clean IoC seems possible with FastAPI+SA

- `db` "package" is **Secondary adapter level**
- `rest` "package" is **Primary adapter level**
- `users` "package" contains **Entity** (`User`) and **Entity use cases** under `registry.Users` class
- Everything top-level under `app` (`main.py` and `deps.py`) can be considered **Infrastructure level**
