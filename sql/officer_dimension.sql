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
from postgres.kafka.officer
inner join postgres.kafka.rank on officer.rank_id = rank.id
inner join postgres.kafka.race on officer.race_id = race.id
inner join postgres.kafka.gender on officer.gender_id = gender.id
left join postgres.kafka.arrests on officer.id = arrests.officer_id
left join postgres.kafka.complaints on officer.id = complaints.officer_id
left join postgres.kafka.complaint_action on complaints.action_taken_id = complaint_action.id
group by officer.id, officer.employment_start_date, officer.age, officer.military_experience, rank.name, race.name, gender.name
;