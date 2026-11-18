SELECT id
    , name
    , height
    , weight
FROM read_json('data/raw/pokemon/*.json')
ORDER BY id
LIMIT 10
;
