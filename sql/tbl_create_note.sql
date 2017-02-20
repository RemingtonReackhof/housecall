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
