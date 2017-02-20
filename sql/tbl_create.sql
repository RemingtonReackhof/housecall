CREATE TABLE Hospital (
	hospital_id INT AUTO_INCREMENT,
	name VARCHAR(100),
	PRIMARY KEY (hospital_id)
);

CREATE TABLE User (
	user_id INT AUTO_INCREMENT,
	email VARCHAR(40),
	skype_username VARCHAR(30),
    firstname VARCHAR(20),
    lastname VARCHAR(20),
    password VARCHAR(256),
    specialty VARCHAR(40),
    hospital_id INT,
    Doctor BOOLEAN,     # TRUE for doctor, FALSE for emt
    PRIMARY KEY (user_id),
    FOREIGN KEY (hospital_id) REFERENCES Hospital(hospital_id)
    	ON DELETE CASCADE
);

CREATE TABLE Notes (
    note_id INT AUTO_INCREMENT,
    is_note BOOLEAN,
    is_instruction BOOLEAN,
    is_snapshot BOOLEAN,
    title VARCHAR(100),
    time_stamp VARCHAR(100),
    content TEXT,
    PRIMARY KEY (note_id)
);


