-- Officer Dimension
select 
officer.id,
officer.employment_start_date,
officer.age,
officer.military_experience,
rank.name as rank,
race.name as race,
gender.name as gender,
count(arrests.officer_id) as num_arrests,
count(complaints.officer_id) as num_complaints,
count(CASE WHEN complaint_action.id not in (1,2) THEN 1 END) as num_complaints_with_action
from postgres.public.officer
inner join postgres.public.rank on officer.rank_id = rank.id
inner join postgres.public.race on officer.race_id = race.id
inner join postgres.public.gender on officer.gender_id = gender.id
left join postgres.public.arrests on officer.id = arrests.officer_id
left join postgres.public.complaints on officer.id = complaints.officer_id
left join postgres.public.complaint_action on complaints.action_taken_id = complaint_action.id
group by officer.id, officer.employment_start_date, officer.age, officer.military_experience, rank.name, race.name, gender.name
;

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
from postgres.public.arrests
inner join postgres.public.arrest_type on arrests.arrest_type_id = arrest_type.id
inner join postgres.public.crime_type on arrests.crime_type_id = crime_type.id
inner join postgres.public.officer on arrests.officer_id = officer.id
inner join postgres.public.rank on officer.rank_id = rank.id
;