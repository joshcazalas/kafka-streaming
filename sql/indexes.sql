-- Index on arrests table for officer_id
CREATE INDEX idx_arrests_officer_id ON postgres.kafka.arrests(officer_id);

-- Index on arrests table for arrest_type_id
CREATE INDEX idx_arrests_arrest_type_id ON postgres.kafka.arrests(arrest_type_id);

-- Index on arrests table for crime_type_id
CREATE INDEX idx_arrests_crime_type_id ON postgres.kafka.arrests(crime_type_id);

-- Index on officer table for rank_id
CREATE INDEX idx_officer_rank_id ON postgres.kafka.officer(rank_id);

-- Index on rank table for id
CREATE INDEX idx_rank_id ON postgres.kafka.rank(id);

-- Index on arrest_type table for id
CREATE INDEX idx_arrest_type_id ON postgres.kafka.arrest_type(id);

-- Index on crime_type table for id
CREATE INDEX idx_crime_type_id ON postgres.kafka.crime_type(id);

-- Index on officer table for race_id
CREATE INDEX idx_officer_race_id ON postgres.kafka.officer(race_id);

-- Index on officer table for gender_id
CREATE INDEX idx_officer_gender_id ON postgres.kafka.officer(gender_id);

-- Index on complaints table for officer_id
CREATE INDEX idx_complaints_officer_id ON postgres.kafka.complaints(officer_id);

-- Index on complaints table for action_taken_id
CREATE INDEX idx_complaints_action_taken_id ON postgres.kafka.complaints(action_taken_id);

-- Index on complaint_action table for id
CREATE INDEX idx_complaint_action_id ON postgres.kafka.complaint_action(id);