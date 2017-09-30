create database eecs481;

use eecs481;

CREATE TABLE eecs481.Hospital (
	hospital_id INT AUTO_INCREMENT,
	name VARCHAR(100),
	PRIMARY KEY (hospital_id)
);

CREATE TABLE eecs481.User (
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


CREATE TABLE eecs481.Notes (
    note_id INT AUTO_INCREMENT,
    is_note BOOLEAN,
    is_instruction BOOLEAN,
    is_snapshot BOOLEAN,
    title VARCHAR(100),
    time_stamp VARCHAR(100),
    content TEXT,
    PRIMARY KEY (note_id)
);


/* CREATE TABLE eecs481.Call( */
/* ) */

INSERT INTO Hospital
VALUES ('1', "University Hospital");

INSERT INTO Hospital
VALUES ('2', "C.S. Mott's Children's Hospital");

INSERT INTO Hospital
VALUES ('3', "Magnetic Resonance Imaging (MRI) at University Hospital");

INSERT INTO Hospital
VALUES ('4', "Neurology at Mott's Children's Hospital");

INSERT INTO Hospital
VALUES ('5', "Nephrology Clinic at Mott's Children's Hospital");

INSERT INTO Hospital
VALUES ('6', "Medical Procedures Unit at University Hospital");

INSERT INTO Hospital
VALUES ('7', "Med Inn Building");

INSERT INTO Hospital
VALUES ('8', "Pulmonary Clinic at Mott's Children's Hospital");

INSERT INTO Hospital
VALUES ('9', "Neurology Clinic at Taubman Center");

INSERT INTO Hospital
VALUES ('10', "Ultrasound at University Hospital");

INSERT INTO Hospital
VALUES ('11', "Gastroenterology at Mott's Children's Hospital");

INSERT INTO Hospital
VALUES ('12', "Univesity Hospital Psychiatric Emergency Service");

INSERT INTO Hospital
VALUES ('13', "U of M Hospital");

INSERT INTO Hospital
VALUES ('14', "Department of Radiation Oncology");

INSERT INTO Hospital
VALUES ('15', "Von Voigtlander Women's Hospital");

INSERT INTO Hospital
VALUES ('16', "Urology Clinic at Taubman Center");

INSERT INTO Hospital
VALUES ('17', "Emergency Room at University Hospital");

INSERT INTO Hospital
VALUES ('18', "Multidisciplinary Developmental Evaluation Clinic (M-DEC)");

INSERT INTO Hospital
VALUES ('19', "Department of Pediatrics and Communicable Diseases");

INSERT INTO Hospital
VALUES ('20', "Apheresis Procedure Unit at University Hospital");

INSERT INTO Hospital
VALUES ('21', "VA Ann Arbor Healthcare System");

INSERT INTO Hospital
VALUES ('22', "Henry Ford Health System");

INSERT INTO Hospital
VALUES ('23', "St. Joseph Mercy Ann Arbor");

INSERT INTO Hospital
VALUES ('24', "Select Specialty Hospital - Ann Arbor");

INSERT INTO Hospital
VALUES ('25', "Michigan Heart & Vascular Institute");

INSERT INTO Hospital
VALUES ('26', "South Main Orthopaedics");

insert into Notes values (1,1,0,0,"Notes", '4:23', "Put Your Notes Here!!");  
