## API calls implemented

#### POST/facebook_profile/add/


| Item        | Description |
--------------------------------
| Description | Adds Facebook profile to the database (or updates the existing profile, if one already exists) |
| Parameters | None |
| Type | Application/JSON | 
| Body | JSON keyed on "profile" | 
| Example JSON | ```{
  "profile": {
    "fb_entity_id": "2321",
    "fb_name": "Breitbart",
    "fb_username": "Breitbart",
    ...
    }
    ``` |

**Parameters**: 

#### POST /twitter_profile/add/

#### POST /youtube_profile/add/

#### POST /whois_profile/add/

#### POST /website_profile/add/

#### POST /entity/add/

#### GET /sources/\<entity>

#### GET /sources

#### /lookup/\<domain>
