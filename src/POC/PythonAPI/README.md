# Doodle POC Python Service

## Usage


### List all Requirements

**Definition**
`GET /requirements`

**Arguments**
- `N/A`

**Response**
- `200 OK` on success

```json
[
    {
        "_id": {
            "$oid": "5c826327af503435c8d309eb"
        },
        "name": "Store Room 1",
        "length": "20",
        "width": "10",
        "height": "3"
    },
    {
        "_id": {
            "$oid": "5c82b45faf50340d8860f2ef"
        },
        "name": "Store Room 2",
        "length": "20",
        "width": "20",
        "height": "3"
    }
]
```

