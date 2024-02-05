-- Arrest Dimension
select
arrests.id,
arrests.officer_id,
rank.name as officer_rank,
arrests.arrest_date,
arrests.arrest_time,
arrest_type.name as arrest_type,
arrests.subject_race,
crime_type.name as crime_type
from postgres.kafka.arrests
inner join postgres.kafka.arrest_type on arrests.arrest_type_id = arrest_type.id
inner join postgres.kafka.crime_type on arrests.crime_type_id = crime_type.id
inner join postgres.kafka.officer on arrests.officer_id = officer.id
inner join postgres.kafka.rank on officer.rank_id = rank.id
;