# Generated Database Schema

## PostgreSQL Database

This database schema was auto-generated from database specifications.

### Tables Generated

- user_managements
- resource_managements
- community_platforms
- ai_assistants
- care_provider_portals

### Setup

```bash
# Create database
createdb your_database_name

# Run migration
psql -d your_database_name -f migrations/001_initial.sql

# Verify
psql -d your_database_name -c "\dt"
```

### Project Structure

```
db/
├── migrations/
│   └── 001_initial.sql
└── README.md
```

### Database URL

```
postgresql://user:password@localhost/your_database_name
```
