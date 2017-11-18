To make any of the API calls, call the base url (e.g. http://localhost/ or http://127.0.0.1/) followed by the actual call. So, to get all sources, you would simply invoke `http://127.0.0.1/sources`.

## API calls implemented:
- Add Facebook Profile (`/facebook_profile/add`)
- Add Twitter Profile (`/twitter_profile/add`)
- Add YouTube Profile (`/youtube_profile/add`)
- Add Whois Profile (`/whois_profile/add`)
- Add Website Profile (`/website_profile/add`)
- Add Entity (`entity/add`)
- Get All Sources (`/sources`)
- Get Source By Entity ID (`/sources/<id>`)
- Get Entity for Domain (`/lookup/<domain>`)

#### POST/facebook_profile/add/

| Item  | Description |
| ------------- | ------------- |
| Description  |  Adds Facebook profile to the database (or updates the existing profile, if one already exists) |
| Parameters  | None |
| Type | Application/JSON
| Body | JSON body keyed on 'profile'

Example JSON:

```
{
  "profile": {
    "fb_name": "The+Wall+Street+Journal",
    "fb_username": "wsj",
    "fb_fan_count": "5991861",
    ...
  }
}
```

#### POST /twitter_profile/add/

| Item  | Description |
| ------------- | ------------- |
| Description  |  Adds Twitter profile to the database (or updates the existing profile, if one already exists) |
| Parameters  | None |
| Type | Application/JSON
| Body | JSON body keyed on 'profile'

Example JSON:

```
{
  "profile": {
    "twitter_entity_id": "22",
    "twitter_id": "3108351",
    "twitter_name": "The+Wall+Street+Journal",
    "twitter_screen_name": "WSJ",
    ...
    }
}
```

#### POST /youtube_profile/add/

| Item  | Description |
| ------------- | ------------- |
| Description  |  Adds YouTube profile to the database (or updates the existing profile, if one already exists) |
| Parameters  | None |
| Type | Application/JSON
| Body | JSON body keyed on 'profile'

Example JSON:

```
{
  "profile": {
    "youtube_entity_id": "22",
    "youtube_username": null,
    "youtube_id": "UCK7tptUDHh-RYDsdxO1-5QQ",
    "youtube_title": "Wall+Street+Journal",
    ...
    }
}
```

#### POST /whois_profile/add/


| Item  | Description |
| ------------- | ------------- |
| Description  |  Adds Whois profile to the database (or updates the existing profile, if one already exists) |
| Parameters  | None |
| Type | Application/JSON
| Body | JSON body keyed on 'profile'

Example JSON:

```
{
  "profile": {
    "youtube_entity_id": "22",
    "youtube_username": null,
    "youtube_id": "UCK7tptUDHh-RYDsdxO1-5QQ",
    "youtube_title": "Wall+Street+Journal",
    ...
    }
}
```

#### POST /website_profile/add/

| Item  | Description |
| ------------- | ------------- |
| Description  |  Adds website profile to the database (or updates the existing profile, if one already exists). This includes CSS scripts, JS includes, ads.txt, Google Analytics ID, schema.org tags, etc. |
| Parameters  | None |
| Type | Application/JSON
| Body | JSON body keyed on 'profile'

Example JSON:

```
{
  "profile": {
    "youtube_entity_id": "22",
    "youtube_username": null,
    "youtube_id": "UCK7tptUDHh-RYDsdxO1-5QQ",
    "youtube_title": "Wall+Street+Journal",
    ...
    }
}
```

#### POST /entity/add/
| Item  | Description |
| ------------- | ------------- |
| Description  |  Adds a "publisher" and a domain to the main list of entities, on the back of which all the other profiles run.|
| Parameters  | None |
| Type | Application/JSON
| Body | JSON body keyed on 'profile'

Example JSON:

```
{
  "profile": {
    "name": "Wall Street Journal",
    "url": "wsj.com",
    ...
    }
}
```

#### GET /sources/\<entity>

#### GET /sources

#### /lookup/\<domain>
