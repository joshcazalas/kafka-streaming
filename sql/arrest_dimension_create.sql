create table if not exists postgres.reporting.arrest_dimension (
	id int4 NULL,
	officer_id int4 NULL,
	officer_rank varchar NULL,
	arrest_date date NULL,
	arrest_time varchar(50) NULL,
	arrest_type varchar NULL,
	subject_race varchar(50) NULL,
	crime_type varchar NULL
);