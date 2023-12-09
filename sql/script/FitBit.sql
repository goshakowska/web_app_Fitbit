INSERT INTO training_goal (training_goal_id, name) VALUES (1, 'Redukcja wagi');
INSERT INTO training_goal (training_goal_id, name) VALUES (2, 'Zbudowanie masy');
INSERT INTO training_goal (training_goal_id, name) VALUES (3, 'Zwiêkszenie wytrzyma³oœci');
INSERT INTO training_goal (training_goal_id, name) VALUES (4, 'Zwiêkszenie gibkoœci');
INSERT INTO training_goal (training_goal_id, name) VALUES (5, 'Poprawa zdrowia ogólnego');


INSERT INTO equipment (equipment_id, name) VALUES (1, 'Bie¿nia');
INSERT INTO equipment (equipment_id, name) VALUES (2, 'Rower treningowy');
INSERT INTO equipment (equipment_id, name) VALUES (3, 'Wioœlarz');
INSERT INTO equipment (equipment_id, name) VALUES (4, '£awka do wyciskania');    --?
INSERT INTO equipment (equipment_id, name) VALUES (5, 'Suwnica do martwego ci¹gu'); --?
INSERT INTO equipment (equipment_id, name) VALUES (6, 'Maszyna do przysiadów'); --?
INSERT INTO equipment (equipment_id, name) VALUES (7, 'Dr¹¿ek do podci¹gania');
INSERT INTO equipment (equipment_id, name) VALUES (8, 'Hantle');
INSERT INTO equipment (equipment_id, name) VALUES (9, 'Orbitrek');
INSERT INTO equipment (equipment_id, name) VALUES (10, 'Pi³ka do stabilizacji');
INSERT INTO equipment (equipment_id, name) VALUES (11, 'Stepper');
INSERT INTO equipment (equipment_id, name) VALUES (12, 'Hula-hop');
INSERT INTO equipment (equipment_id, name) VALUES (13, 'Kostka do jogi');
INSERT INTO equipment (equipment_id, name) VALUES (14, 'Roller');
INSERT INTO equipment (equipment_id, name) VALUES (15, 'Suwnica na nogi');
INSERT INTO equipment (equipment_id, name) VALUES (16, '');
INSERT INTO equipment (equipment_id, name) VALUES (17, 'Pi³ka do stabilizacji');

INSERT INTO gym (gym_id, name, phone_number, city, street, house_number, county, zip_code, 
                 monday_opening, monday_closing, tuesday_opening, tuesday_closing, 
                 wednesday_opening, wednesday_closing, thursday_opening, thursday_closing, 
                 friday_opening, friday_closing, saturday_opening, saturday_closing, 
                 sunday_opening, sunday_closing)
VALUES 
(1, 'Fitness Plus', '123-456-7890', 'City1', 'Street1', '12A', 'County1', '12345', 
 '08:00 AM', '09:00 PM', '08:00 AM', '09:00 PM', '08:00 AM', '09:00 PM', '08:00 AM', '09:00 PM', 
 '08:00 AM', '09:00 PM', '10:00 AM', '06:00 PM', '12:00 PM', '05:00 PM');