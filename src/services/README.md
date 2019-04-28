# Doodle API

## Usage


### List all Requirement Documents

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

### Create Document

**Definition**
`POST /requirement`

**Arguments**
```json
{
    "width": "10",
    "name": "Store Room 8",
    "length": "20",
    "height": "3"
}
```

**Response**
- `201 CREATED` on success

```json
{
    "$oid": "5c9248193173c01594ab9c0f"
}
```

###  Single Requirement Document

**Definition**
`GET /requirement<documnent id>`

**Arguments**
_Id

**Response**
- `200 OK` on success

```json
{
    "_id": {
        "$oid": "5c8cea393173c018b28b3a49"
    },
    "width": "14",
    "length": "20",
    "height": "3",
    "name": "Store Room 5"
}
```

### Delete Document

**Definition**
`DELETE /requirement<document id>`

**Arguments**
_Id

**Response**  
- `404 NOT FOUND` document not found  
- `204 NO CONTENT` document deleted

### Update Document

**Definition**
`PUT /requirement`

**Arguments**

```json
{
    "name": "Store Room 10",
    "_id": {
        "$oid": "5c8cea393173c018b28b3a49"
    },
    "width": "14",
    "length": "20",
    "height": "3",
    "lan connections":    "16"
}
```

**Response**
- `404 NOT FOUND` document not found 
- `204 NO CONTENT` on updated
