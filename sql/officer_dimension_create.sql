create table if not exists postgres.reporting.officer_dimension (
	id int4 NULL,
	employment_start_date date NULL,
	age varchar(50) NULL,
	military_experience varchar(50) NULL,
	"rank" varchar NULL,
	race varchar NULL,
	gender varchar NULL,
	num_arrests int8 NULL,
	num_complaints int8 NULL,
	num_complaints_with_action int8 NULL
);