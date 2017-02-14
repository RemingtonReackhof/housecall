CREATE TABLE Emt (
	email VARCHAR(40),
	skype_username VARCHAR(30),
    firstname VARCHAR(20),
    lastname VARCHAR(20),
    password VARCHAR(256),
    PRIMARY KEY (email)
);

CREATE TABLE Hospital (
	hospital_id INT AUTO_INCREMENT,
	name VARCHAR(100),
	PRIMARY KEY (hospital_id)
);

CREATE TABLE Doctor (
	email VARCHAR(40),
	skype_username VARCHAR(30),
    firstname VARCHAR(20),
    lastname VARCHAR(20),
    password VARCHAR(256),
    specialty VARCHAR(40),
    hospital_id INT,
    PRIMARY KEY (email),
    FOREIGN KEY (hospital_id) REFERENCES Hospital(hospital_id)
    	ON DELETE CASCADE
);