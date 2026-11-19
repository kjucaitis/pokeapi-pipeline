INSTALL excel;
LOAD excel;

-- One row per Pokémon from the API files
CREATE OR REPLACE TABLE pokemon AS
SELECT
    id AS pokedex_number
    , name
    , types[1].type.name AS type_1
    , types[2].type.name AS type_2
    , height / 10 AS height_m
    , weight / 10 AS weight_kg
    , stats[1].base_stat AS hp
    , stats[2].base_stat AS attack
    , stats[3].base_stat AS defense
    , stats[4].base_stat AS sp_attack
    , stats[5].base_stat AS sp_defense
    , stats[6].base_stat AS speed
    , sprites.other."official-artwork".front_default AS artwork_url
FROM read_json('data/raw/pokemon/*.json')
WHERE is_default
;

-- Survey results from the spreadsheet
CREATE OR REPLACE TABLE survey AS
SELECT
    "Rank" AS survey_rank
    , CAST("Dex #" AS INTEGER) AS pokedex_number
    , "Pokémon Name" AS survey_name
    , "Generation" AS generation
    , CAST("Votes" AS INTEGER) AS votes
FROM read_xlsx('data/raw/2025 Pokemon Survey RESULTS - Sparklez  Squad.xlsx', range = 'A1:E2000')
WHERE "Dex #" IS NOT NULL
;

-- Join them
CREATE OR REPLACE TABLE survey_results AS
SELECT
    s.*
    , p.* EXCLUDE (pokedex_number)
FROM survey s
LEFT JOIN pokemon p
    ON s.pokedex_number = p.pokedex_number
;