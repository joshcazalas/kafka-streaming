SELECT * FROM postgres.public.user_datastore_value limit 100;
select * from postgres.public.user_organizational_unit limit 100;
select * from postgres.public.tenant limit 100;

-- Scenario 1 Bullet Point 1: Pull all users from public.user_datastore_value with the following values (alias users_distinct): 24-31-315: 5 Years, 24-31-315: 6 Months
select distinct (user_id) as users_distinct from postgres.public.user_datastore_value where value in ('24-31-315: 5 Years','24-31-315: 6 Months');

--Checking count of original table vs distinct query to make sure it looks right
select count(*) from postgres.public.user_datastore_value as original_count union all
select count(*) from (select distinct (user_id) as users_distinct from postgres.public.user_datastore_value where value in ('24-31-315: 5 Years','24-31-315: 6 Months')) as user_count;

-- Scenario 1 Bullet Point 2: Create a query that creates a table public.users from the distinct list of users from the above users_distinct list.
create table postgres.public.users as select * from (select distinct (user_id) as users_distinct from postgres.public.user_datastore_value where value in ('24-31-315: 5 Years','24-31-315: 6 Months')) as a;

-- Validating table creation
select * from postgres.public.users;

-- Scenario 1 Bullet Point 3:
select * from postgres.public.user_organizational_unit
inner join postgres.public.organizational_unit
on user_organizational_unit.organizational_unit_id = organizational_unit.id
inner join postgres.public.tenant on organizational_unit.tenant_id = tenant.id
where tenant.name = 'Colorado Post';

-- Scenario 1 Bullet Point 4
select * from (
select user_id, count(*) as rank from postgres.public.user_datastore_value group by user_id having count(*) > 1
) a where a.rank > 100 and a.rank < 135;

-- Scenario 1 Bullet Point 5
with cte as (
    select * from (
	select user_id, count(*) as rank from postgres.public.user_datastore_value group by user_id having count(*) > 1 and count(*) > 100 and count(*) < 135
	) a
)
select
user_id, 
rank,
max(rank) over () - rank as rank_difference,
case
	when max(rank) over() - rank < 15 then 'smooth'
	else 'jump ahead'
end
from cte order by rank desc;