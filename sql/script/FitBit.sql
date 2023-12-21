-- training goal
INSERT INTO training_goal (training_goal_id, name) VALUES (1, 'Redukcja wagi');
INSERT INTO training_goal (training_goal_id, name) VALUES (2, 'Zbudowanie masy');
INSERT INTO training_goal (training_goal_id, name) VALUES (3, 'Zwiï¿½kszenie wytrzymaï¿½oï¿½ci');
INSERT INTO training_goal (training_goal_id, name) VALUES (4, 'Zwiï¿½kszenie gibkoï¿½ci');
INSERT INTO training_goal (training_goal_id, name) VALUES (5, 'Poprawa zdrowia ogï¿½lnego');

-- equipment
INSERT INTO equipment (equipment_id, name) VALUES (1, 'Bieï¿½nia');
INSERT INTO equipment (equipment_id, name) VALUES (2, 'Rower treningowy');
INSERT INTO equipment (equipment_id, name) VALUES (3, 'Wioï¿½larz');
INSERT INTO equipment (equipment_id, name) VALUES (4, 'ï¿½awka do wyciskania');
INSERT INTO equipment (equipment_id, name) VALUES (5, 'Suwnica do martwego ciï¿½gu');
INSERT INTO equipment (equipment_id, name) VALUES (6, 'Maszyna do przysiadï¿½w');
INSERT INTO equipment (equipment_id, name) VALUES (7, 'Drï¿½ï¿½ek do podciï¿½gania');
INSERT INTO equipment (equipment_id, name) VALUES (8, 'Hantle');
INSERT INTO equipment (equipment_id, name) VALUES (9, 'Orbitrek');
INSERT INTO equipment (equipment_id, name) VALUES (10, 'Piï¿½ka do stabilizacji');
INSERT INTO equipment (equipment_id, name) VALUES (11, 'Stepper');
INSERT INTO equipment (equipment_id, name) VALUES (12, 'Hula-hop');
INSERT INTO equipment (equipment_id, name) VALUES (13, 'Kostka do jogi');
INSERT INTO equipment (equipment_id, name) VALUES (14, 'Roller');
INSERT INTO equipment (equipment_id, name) VALUES (15, 'Suwnica na nogi');
INSERT INTO equipment (equipment_id, name) VALUES (16, 'Atlas');
INSERT INTO equipment (equipment_id, name) VALUES (17, 'Piï¿½ka do stabilizacji');

-- gym
INSERT INTO gym (gym_id, name, phone_number, city, street, house_number, county, zip_code,
                 monday_opening, monday_closing, tuesday_opening, tuesday_closing,
                 wednesday_opening, wednesday_closing, thursday_opening, thursday_closing,
                 friday_opening, friday_closing, saturday_opening, saturday_closing,
                 sunday_opening, sunday_closing)
VALUES
(1, 'FitBit Zero Fat', '123456789', 'Tï¿½uszcz', 'ul. Warszawska', '37', 'Polska', '05-240',
 '08:00', '21:00', '08:00', '21:00', '08:00', '20:00', '08:00', '22:00',
 '08:00', '20:00', '06:00', '23:00', '10:00', '18:00');

INSERT INTO gym (gym_id, name, phone_number, city, street, house_number, county, zip_code,
                 monday_opening, monday_closing, tuesday_opening, tuesday_closing,
                 wednesday_opening, wednesday_closing, thursday_opening, thursday_closing,
                 friday_opening, friday_closing, saturday_opening, saturday_closing,
                 sunday_opening, sunday_closing)
VALUES
(2, 'FitBit Plus', '111111111', 'Warszawa', 'ul. Jadowska', '100A', 'Polska', '03-761',
 '06:00', '22:00', '06:00', '22:00', '06:00', '22:00', '06:00', '22:00',
 '06:00', '22:00', '06:00', '22:00', '06:00', '22:00');

INSERT INTO gym (gym_id, name, phone_number, city, street, house_number, county, zip_code,
                 monday_opening, monday_closing, tuesday_opening, tuesday_closing,
                 wednesday_opening, wednesday_closing, thursday_opening, thursday_closing,
                 friday_opening, friday_closing, saturday_opening, saturday_closing,
                 sunday_opening, sunday_closing)
VALUES
(3, 'FitBit Minus', '111222333', 'Woï¿½omin', 'ul. Wileï¿½ska', '25', 'Polska', '05-200',
 '07:00', '20:00', '07:00', '20:00', '07:00', '22:00', '07:00', '19:00',
 '07:00', '20:00', '07:00', '20:00', '07:00', '20:00');

INSERT INTO gym (gym_id, name, phone_number, city, street, house_number, county, zip_code,
                 monday_opening, monday_closing, tuesday_opening, tuesday_closing,
                 wednesday_opening, wednesday_closing, thursday_opening, thursday_closing,
                 friday_opening, friday_closing, saturday_opening, saturday_closing,
                 sunday_opening, sunday_closing)
VALUES
(4, 'FitBit Malinka', '789789789', 'Zakopane', 'ul. Krzeptï¿½wki', '99', 'Polska', '34-500',
 '08:00', '22:00', '08:00', '22:00', '08:00', '22:00', '08:00', '22:00',
 '08:00', '22:00', '08:00', '22:00', '10:00', '22:00');


INSERT INTO gym (gym_id, name, phone_number, city, street, house_number, county, zip_code,
                 monday_opening, monday_closing, tuesday_opening, tuesday_closing,
                 wednesday_opening, wednesday_closing, thursday_opening, thursday_closing,
                 friday_opening, friday_closing, saturday_opening, saturday_closing,
                 sunday_opening, sunday_closing)
VALUES
(5, 'FitBit Polna', '159159159', 'Warszawa', 'ul. Polna', '99', 'Polska', '00-666',
 '06:00', '20:00', '06:00', '21:00', '07:00', '22:00', '07:00', '22:00',
 '06:00', '21:00', '06:00', '20:00', '16:00', '20:00');

 INSERT INTO gym (gym_id, name, phone_number, city, street, house_number, county, zip_code,
                 monday_opening, monday_closing, tuesday_opening, tuesday_closing,
                 wednesday_opening, wednesday_closing, thursday_opening, thursday_closing,
                 friday_opening, friday_closing, saturday_opening, saturday_closing,
                 sunday_opening, sunday_closing)
VALUES
(6, 'FitBit Neptun', '753753753', 'Gdaï¿½sk', 'ul. Gotycka', '20', 'Polska', '80-253',
 '07:00', '22:00', '07:00', '22:00', '06:00', '21:00', '07:00', '22:00',
 '07:00', '21:00', '08:00', '20:00', '10:00', '20:00');

 -- parameter
INSERT INTO parameter (parameter_id, name, units) VALUES (1, 'Obciï¿½ï¿½enie', 'kg');
INSERT INTO parameter (parameter_id, name, units) VALUES (2, 'Dystans', 'm');
INSERT INTO parameter (parameter_id, name, units) VALUES (3, 'Wysokoï¿½ï¿½', 'cm');

-- ticket
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (1, 'Standardowy', 60, 250, 'Dniowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (2, 'Standardowy', 30, 150, 'Dniowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (3, 'Standardowy', 7, 50, 'Dniowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (4, 'Standardowy', 1, 15, 'Wejï¿½ciowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (5, 'Standardowy', 5, 70, 'Wejï¿½ciowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (6, 'Standardowy', 10, 130, 'Wejï¿½ciowy');
--INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (7, 'Studencki', 60, 200, 'Dniowy');
--INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (8, 'Studencki', 30, 110, 'Dniowy');
--INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (9, 'Studencki', 7, 30, 'Dniowy');
--INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (10, 'Seniorski', 60, 220, 'Dniowy');
--INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (11, 'Seniorski', 30, 135, 'Dniowy');
--INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (12, 'Seniorski', 7, 40, 'Dniowy');
--INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (13, 'Studencki', 1, 12, 'Wejï¿½ciowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (14, 'Studencki', 5, 55, 'Wejï¿½ciowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (15, 'Studencki', 10, 100, 'Wejï¿½ciowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (16, 'Seniorski', 1, 13, 'Wejï¿½ciowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (17, 'Seniorski', 5, 60, 'Wejï¿½ciowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (18, 'Seniorski', 10, 110, 'Wejï¿½ciowy');

-- discount
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (1, 'Studencki', TO_DATE('2023-12-01', 'YYYY-MM-DD'), Null, 20, 1);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (2, 'Seniorski', TO_DATE('2023-12-01', 'YYYY-MM-DD'), Null, 12, 1);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (3, 'Studencki', TO_DATE('2023-12-01', 'YYYY-MM-DD'), Null, 15, 2);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (4, 'Seniorski', TO_DATE('2023-12-01', 'YYYY-MM-DD'), Null, 10, 2);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (5, 'Studencki', TO_DATE('2023-12-01', 'YYYY-MM-DD'), Null, 10, 3);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (6, 'Seniorski', TO_DATE('2023-12-01', 'YYYY-MM-DD'), Null, 8, 3);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (7, 'Studencki', TO_DATE('2023-12-01', 'YYYY-MM-DD'), Null, 20, 4);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (8, 'Seniorski', TO_DATE('2023-12-01', 'YYYY-MM-DD'), Null, 10, 4);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (9, 'Studencki', TO_DATE('2023-12-01', 'YYYY-MM-DD'), Null, 15, 5);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (10, 'Seniorski', TO_DATE('2023-12-01', 'YYYY-MM-DD'), Null, 8, 5);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (11, 'Studencki', TO_DATE('2023-12-01', 'YYYY-MM-DD'), Null, 20, 6);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (12, 'Seniorski', TO_DATE('2023-12-01', 'YYYY-MM-DD'), Null, 10, 6);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (13, 'ï¿½wiï¿½ta 2023', TO_DATE('2023-12-01', 'YYYY-MM-DD'), TO_DATE('2024-01-31', 'YYYY-MM-DD'), 20, 1);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (14, 'ï¿½wiï¿½ta 2023', TO_DATE('2023-12-01', 'YYYY-MM-DD'), TO_DATE('2024-01-31', 'YYYY-MM-DD'), 20, 2);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (15, 'ï¿½wiï¿½ta 2023', TO_DATE('2023-12-01', 'YYYY-MM-DD'), TO_DATE('2024-01-31', 'YYYY-MM-DD'), 20, 3);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (16, 'ï¿½wiï¿½ta 2023', TO_DATE('2023-12-01', 'YYYY-MM-DD'), TO_DATE('2024-01-31', 'YYYY-MM-DD'), 20, 4);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (17, 'ï¿½wiï¿½ta 2023', TO_DATE('2023-12-01', 'YYYY-MM-DD'), TO_DATE('2024-01-31', 'YYYY-MM-DD'), 20, 5);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (18, 'ï¿½wiï¿½ta 2023', TO_DATE('2023-12-01', 'YYYY-MM-DD'), TO_DATE('2024-01-31', 'YYYY-MM-DD'), 20, 6);


-- user
insert into client (client_id, login, password_hash, email, phone_number, name, surname,
gender, height, birth_year, advancement, target_weight, training_frequency, training_time, training_goal_id, gym_id)
VALUES (1, 'grisza2', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'grisza_to_ja@edu.pl', '123123123', 'Alina', 'Starkow', 'K', 155, TO_DATE('2000-01-01', 'YYYY-MM-DD'),
    'zaawansowany', 55, 3, 60, 1, 1);

insert into client (client_id, login, password_hash, email, phone_number, name, surname,
gender, height, birth_year, advancement, target_weight, training_frequency, training_time, training_goal_id, gym_id)
VALUES (2, 'krol_wron', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'wron6@edu.pl', '789598412', 'Kaz', 'Brekker', 'M', 180, TO_DATE('1999-05-01', 'YYYY-MM-DD'),
    'zaawansowany', 80, 5, 45, 2, 5);

insert into client (client_id, login, password_hash, email, phone_number, name, surname,
gender, height, birth_year, advancement, target_weight, training_frequency, training_time, training_goal_id, gym_id)
VALUES (3, 'chlopi', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'jagus123@edu.pl', '157426852', 'Jagna', 'Paczesiï¿½wna', 'K', 185, TO_DATE('2003-07-01', 'YYYY-MM-DD'),
    'œredniozaawansowany', 80, 1, 80, 4, 1);

insert into client (client_id, login, password_hash, email, phone_number, name, surname,
gender, height, birth_year, advancement, target_weight, training_frequency, training_time, training_goal_id, gym_id)
VALUES (4, 'blyskawica', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'hedwiga@edu.pl', '456456456', 'Henryk', 'Garncarz', 'M', 165, TO_DATE('1980-07-31', 'YYYY-MM-DD'),
    'zaawansowany', 65, 2, 60, 2, 1);

insert into client (client_id, login, password_hash, email, phone_number, name, surname,
gender, height, birth_year, advancement, target_weight, training_frequency, training_time, training_goal_id, gym_id)
VALUES (5, 'diuna3000', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'diuna456@edu.pl', '157157157', 'Paweï¿½', 'Atryda', 'M', 178, TO_DATE('1976-12-12', 'YYYY-MM-DD'),
    'pocz¹tkuj¹cy', 75, 4, 50, 5, 4);

insert into client (client_id, login, password_hash, email, phone_number, name, surname,
gender, height, birth_year, advancement, target_weight, training_frequency, training_time, training_goal_id, gym_id)
VALUES (6, 'miodek', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'pszczolki@edu.pl', '157426854', 'Kubuï¿½', 'Puchatek', 'M', 160, TO_DATE('2000-07-01', 'YYYY-MM-DD'),
    'poczï¿½tkujï¿½cy', 65, 1, 30, 4, 1);

insert into client (client_id, login, password_hash, email, phone_number, name, surname,
gender, height, birth_year, advancement, target_weight, training_frequency, training_time, training_goal_id, gym_id)
VALUES (7, 'bennet_e', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'dumaiuprzedzenie@edu.pl', '157426745', 'Elï¿½bieta', 'Bennet', 'K', 170, TO_DATE('1990-08-01', 'YYYY-MM-DD'),
    'ï¿½redniozaawansowany', 70, 1, 90, 5, 1);

insert into client (client_id, login, password_hash, email, phone_number, name, surname,
gender, height, birth_year, advancement, target_weight, training_frequency, training_time, training_goal_id, gym_id)
VALUES (8, 'edward123', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'o_zmierzchu@edu.pl', '157789789', 'Edward', 'Cullen', 'M', 179, TO_DATE('1910-09-11', 'YYYY-MM-DD'),
    'ï¿½redniozaawansowany', 75, 3, 60, 3, 1);

insert into client (client_id, login, password_hash, email, phone_number, name, surname,
gender, height, birth_year, advancement, target_weight, training_frequency, training_time, training_goal_id, gym_id)
VALUES (9, 'dewajtis', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'poswicie@edu.pl', '157456325', 'Marek', 'Czertwan', 'M', 200, TO_DATE('1986-04-04', 'YYYY-MM-DD'),
    'zaawansowany', 90, 2, 90, 1, 1);

insert into client (client_id, login, password_hash, email, phone_number, name, surname,
gender, height, birth_year, advancement, target_weight, training_frequency, training_time, training_goal_id, gym_id)
VALUES (10, 'monet_monet', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'perelka@edu.pl', '652358745', 'Hailie', 'Monet', 'K', 174, TO_DATE('2004-10-21', 'YYYY-MM-DD'),
    'zaawansowany', 65, 1, 60, 1, 1);
    
insert into client_data_history (weight, fat_body_level, measurement_date, client_id) VALUES (56, null, TO_DATE('2023-12-01', 'YYYY-MM-DD'), 1);
insert into client_data_history (weight, fat_body_level, measurement_date, client_id) VALUES (91, null, TO_DATE('2023-12-01', 'YYYY-MM-DD'), 2);
insert into client_data_history (weight, fat_body_level, measurement_date, client_id) VALUES (86, null, TO_DATE('2023-12-01', 'YYYY-MM-DD'), 3);
insert into client_data_history (weight, fat_body_level, measurement_date, client_id) VALUES (74, null, TO_DATE('2023-12-01', 'YYYY-MM-DD'), 4);
insert into client_data_history (weight, fat_body_level, measurement_date, client_id) VALUES (83, null, TO_DATE('2023-12-01', 'YYYY-MM-DD'), 5);
insert into client_data_history (weight, fat_body_level, measurement_date, client_id) VALUES (71, null, TO_DATE('2023-12-01', 'YYYY-MM-DD'), 6);
insert into client_data_history (weight, fat_body_level, measurement_date, client_id) VALUES (76, null, TO_DATE('2023-12-01', 'YYYY-MM-DD'), 7);
insert into client_data_history (weight, fat_body_level, measurement_date, client_id) VALUES (82, null, TO_DATE('2023-12-01', 'YYYY-MM-DD'), 8);
insert into client_data_history (weight, fat_body_level, measurement_date, client_id) VALUES (102, null, TO_DATE('2023-12-01', 'YYYY-MM-DD'), 9);
insert into client_data_history (weight, fat_body_level, measurement_date, client_id) VALUES (70, null, TO_DATE('2023-12-01', 'YYYY-MM-DD'), 10);

-- employee trener

insert into employee (employee_id, login, password_hash, email, phone_number, name, surname, gender,type, standar_salary, locker_id, gym_id)
VALUES (1, 'zacmienie', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'bella_trener@edu.pl', '457125485', 'Bella', 'Swan',
'K', 'trener', 3000, Null, 1);

insert into employee (employee_id, login, password_hash, email, phone_number, name, surname, gender,type, standar_salary, locker_id, gym_id)
VALUES (2, 'pan_tadeusz', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 't_soplica@edu.pl', '547126359', 'Tadeusz', 'Soplica',
'M', 'trener', 2800, Null, 1);

insert into employee (employee_id, login, password_hash, email, phone_number, name, surname, gender,type, standar_salary, locker_id, gym_id)
VALUES (3, 'laleczka', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'laleczka@edu.pl', '555555555', 'Izabela', 'ï¿½ï¿½cka',
'K', 'trener', 3100, Null, 1);

insert into employee (employee_id, login, password_hash, email, phone_number, name, surname, gender,type, standar_salary, locker_id, gym_id)
VALUES (4, 'trener_stachu', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'stasiek_w@edu.pl', '141141141', 'Stanisï¿½aw', 'Wokulski',
'M', 'trener', 4000, Null, 1);

insert into employee (employee_id, login, password_hash, email, phone_number, name, surname, gender,type, standar_salary, locker_id, gym_id)
VALUES (5, 'stary_subiekt', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'napoleon@edu.pl', '854753621', 'Ignacy', 'Rzecki',
'M', 'trener', 2000, Null, 1);

insert into employee (employee_id, login, password_hash, email, phone_number, name, surname, gender,type, standar_salary, locker_id, gym_id)
VALUES (6, 'trener_zbyszko', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'krzyzacy@edu.pl', '754862156', 'Zbyszko', 'Bogdaï¿½ski',
'M', 'trener', 2500, Null, 1);

insert into employee (employee_id, login, password_hash, email, phone_number, name, surname, gender,type, standar_salary, locker_id, gym_id)
VALUES (7, 'legia_warszawa', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'my_slowianie@edu.pl', '124124124', 'Ligia', 'Winicjusz',
'K', 'trener', 2800, Null, 1);

insert into employee (employee_id, login, password_hash, email, phone_number, name, surname, gender,type, standar_salary, locker_id, gym_id)
VALUES (8, 'mereczek', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'mereczek@edu.pl', '456523621', 'Marek', 'Winicjusz',
'M', 'trener', 3000, Null, 1);

insert into employee (employee_id, login, password_hash, email, phone_number, name, surname, gender,type, standar_salary, locker_id, gym_id)
VALUES (9, 'silacz', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'traktor@edu.pl', '458541126', 'Ursus', 'Rolnik',
'M', 'trener', 3000, Null, 1);

insert into employee (employee_id, login, password_hash, email, phone_number, name, surname, gender,type, standar_salary, locker_id, gym_id)
VALUES (10, 'michalki', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'pan_michal@edu.pl', '456269845', 'Michaï¿½', 'Woï¿½odyjowski',
'M', 'trener', 2600, Null, 1);


-- employee menadÅ¼er
insert into employee(employee_id, login, password_hash, email, phone_number, name, surname, gender, type, standar_salary, gym_id)
values (12, 'alek', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'szef@edu.pl', '234123673', 'Aleksander', 'Dawidowski', 'M', 'menadÅ¼er', 5000, 1);


-- employee portier
insert into employee(employee_id, login, password_hash, email, phone_number, name, surname, gender, type, standar_salary, gym_id)
values (11, 'kleks', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'akademia@edu.pl', '111111111', 'AmbroÅ¼y', 'Kleks', 'M', 'portier', 3000, 1);


-- exercise
INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (1, 'Bieganie na bie¿ni', 'Cardio', 300, 1800, 'Œredniozaawansowany', 0, 'Biegnij na bie¿ni', 1);
-- dystans 5km czyli 5000m
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (1, 5000, 2, 1);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (2, 'Jazda na rowerku', 'Cardio', 250, 1200, 'Pocz¹tkuj¹cy', 0, 'JedŸ na rowerku stacjonarnym', 2);
-- dystans 7km czyli 7000m
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (2, 7000, 2, 2);


INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (3, 'Wios³owanie', 'Si³owe', 200, 1500, 'Œredniozaawansowany', 0, 'Trening si³owy na wioœlarzu', 3);
-- dystans 5km czyli 5000m
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (3, 5000, 2, 3);


INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (4, 'Wyciskanie sztangi', 'Si³owe', 80, 100, 'Zaawansowany', 10, 
'Po³ó¿ siê na ³awce p³askiej. Chwyæ sztangê nachwytem na tak¹ szerokoœæ, aby w po³owie wykonywania ruchu k¹t miêdzy ramieniem a przedramieniem wynosi³ 90 stopni. £opatki œci¹gniête, barki opuszczone i mocno dociœniête do ³aweczki. Zachowaj naturalne ustawienie krêgos³upa – odcinek lêdŸwiowy lekko uniesiony, poœladki na ³aweczce.Utrzymuj¹c prawid³ow¹ pozycjê wyjœciow¹, wykonaj wdech i powolnym ruchem opuœæ sztangê do œrodkowej czêœci klatki piersiowej, uginaj¹c ramiona w ³okciach. Po przytrzymaniu sztangi w okolicach klatki przez u³amek sekundy zacznij unosiæ sztangê z powrotem do pozycji wyjœciowej, wykonuj¹c wydech powietrza. Skup siê, aby wyciskanie nastêpowa³o z miêœnia piersiowego. W momencie wyprostowania ramion ze sztang¹ (unikaj przeprostu w ³okciach) mocno dopnij miêsieñ piersiowy, po czym ponownie zacznij opuszczaæ sztangê.', 4);
-- obci¹¿enie 20 kg wysokoœæ 40 cm
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (4, 20, 1, 4);
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (5, 40, 3, 4);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (5, 'Martwy ci¹g', 'Si³owe', 6, 60, 'Zaawansowany', 10, 
'Pó³przysiad przed sztang¹, cia³o mocno pochylone. Sztanga nad stopami, blisko piszczeli. Ramiona wyprostowane, ustawione na szerokoœæ barków. Plecy wyprostowane, g³owa powinna stanowiæ przed³u¿enie krêgos³upa. Utrzymuj¹c prawid³ow¹ pozycjê wyjœciow¹, wykonaj mocny wdech powietrza do brzucha. Wybierz luz na sztandze, a nastêpnie zacznij unosiæ sztangê z ziemi, wykonuj¹c wyprost w stawach biodrowych oraz kolanowych. Sztangê prowadŸ blisko nóg, nie pozwól, aby podczas ruchu plecy wygiê³y siê w ³uk. Koñcz¹c ruch, utrzymuj mocne napiêcie miêœni brzucha oraz poœladków i wykonaj wydech. Utrzymaj pozycjê przez sekundê, nastêpnie nabieraj¹c kolejny wdech, w kontrolowany sposób odstaw sztangê na pod³ogê. Utrzymuj plecy proste, a miêœnie brzucha mocno napiête. Wykonaj wyznaczon¹ liczbê powtórzeñ, za ka¿dym razem odk³adaj sztangê na pod³ogê.', 5);
-- obci¹¿enie 20 kg wysokoœæ 80cm
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (6, 20, 1, 5);
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (7, 80, 3, 5);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (6, 'Poliquin step-up', 'Si³owe', 5, 60, 'Œredniozaawansowane', 15, 
'Pozycja stoj¹ca na jednej nodze na podwy¿szeniu ok. 20 cm. Pod piêt¹ minimalne podniesienie ok. 2 cm. Sylwetka wyprostowana, ramiona ustawione na biodrach lub wzd³u¿ cia³a. Druga noga w powietrzu, stopa ustawiona w zgiêciu grzbietowym (palce koñcami skierowane w górê).Wykonaj g³êboki wdech. Powoli rozpocznij uginanie nogi w kolanie, zachowuj¹c biodra na jednej wysokoœci. Utrzymuj¹c prawid³ow¹ postawê, schodŸ przez oko³o 4 sekundy, tak aby druga wyprostowana noga dotknê³a piêt¹ pod³ogi. Nastêpnie bez wsparcia (odbicia) nogi na pod³odze wyprostuj nogê w kolanie i wraz z wdechem wróæ do pozycji pocz¹tkowej. W pozycji pocz¹tkowej pamiêtaj o utrzymaniu kolana w aktywnym wyproœcie (bez przeprostu). ', 11);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (7, 'Podci¹ganie na dr¹¿ku', 'Si³owe', 3, 30, 'Pocz¹tkuj¹cy', 6, 
'Dr¹¿ek z³apany nachwytem (kciuki skierowane do wewn¹trz), szerzej ni¿ rozstaw barków. Ramiona wyprostowane, wzrok skierowany w górê. WeŸ wdech, ruch rozpocznij od bardzo dynamicznego, mocnego œci¹gniêcia ³opatek w dó³ i do siebie po³¹czonego z mocn¹ prac¹ ramion. Podci¹gaj siê tak, jakbyœ chcia³ dotkn¹æ dr¹¿ka brzuchem w okolicy pasa. W najwy¿szym punkcie spróbuj zatrzymaæ ruch poprzez mocne spiêcie miêœni. Nastêpnie kontrolowanym ruchem opuœæ cia³o.', 7);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (8, 'Z-press', 'Si³owe', 6, 60, 'Pocz¹tkuj¹cy', 12, 
'Pozycja siedz¹ca, nogi rozstawione tak, aby zapewnia³y stabiln¹ postawê. Ramiona w górze, hantle na wysokoœci g³owy. £okcie skierowane w dó³. Utrzymuj¹c prawid³ow¹ pozycjê wyjœciow¹, weŸ wdech i zacznij wyciskaæ ciê¿ar nad g³owê. W koñcowej fazie ruchu wykonaj wydech. Nastêpnie powolnym ruchem opuœæ hantle, wykonuj¹c p³ynny wdech.', 8);
-- obci¹¿enie 2kg
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (8, 2, 1, 8);


INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (9, 'Trening na orbitreku', 'Cardio', 160, 1800, 'Œredniozaawansowany', 0, 'Intensywny trening na orbitreku', 9);
-- dystans 5km 5000m
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (9, 5000, 2, 9);


INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (10, 'Przyci¹ganie kolan na pi³ce', 'Si³owe', 160, 60, 'Pocz¹tkuj¹cy', 10, 
'Podpór przodem z nogami ustawionymi na pi³ce. Z pozycji wyjœciowej rozpocznij wykonywanie unoszenia bioder. Równoczeœnie uginaj kolana, kieruj¹c je do klatki piersiowej. W momencie maksymalnego spiêcia utrzymaj pozycjê przez u³amek sekundy. Spokojnym, kontrolowanym ruchem wróæ do pozycji wyjœciowej.', 10);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (11, 'Obroty szyi', 'Rozci¹gaj¹ce', 3, 30, 'Pocz¹tkuj¹cy', 6, 'Wykonuj skrêty szyi. Wykonuj je powoli i ostro¿nie, w lewo i w prawo.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (12, 'Kobra', 'Rozci¹gaj¹ce', 3, 20, 'Pocz¹tkuj¹cy', 1, 'Le¿enie przodem, d³onie oparte na wysokoœci klatki piersiowej. Z pozycji wyjœciowej unieœ tu³ów, trzymaj¹c biodra oparte na pod³odze. Wzrok skieruj przed siebie. Utrzymaj pozycjê przez 20 sekund, a nastêpnie wróæ do pozycji wyjœciowej.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (13, 'Rozci¹ganie miêœni grzbietu', 'Rozci¹gaj¹ce', 3, 20, 'Pocz¹tkuj¹cy', 2, 
'W klêku podpartym wysuñ rêkê w przód po stronie rozci¹ganej za oœ œrodkow¹ cia³a. D³oñ wysuniêtej rêki ustaw wierzchni¹ stron¹ do pod³o¿a. Drug¹ rêkê u³ó¿ na wysuniêtej rêce, jednoczeœnie naciskaj na ni¹ tak, by nie zmieni³a swojej pozycji. Opieraj ciê¿ar cia³a na kolanach oraz wysuniêtej rêce, postaraj siê delikatnie skrêcaæ tu³ów, przenoœ ciê¿ar cia³a w bok na stronê wysuniêtej rêki. Podczas wykonywania skrêtu tu³owia postaraj siê wykonaæ lekkie ty³opochylenie miednicy, szczególnie po stronie rozci¹ganej. W tej pozycji pozostañ przez oko³o 90–120 sekund, systematycznie pog³êbiaj pozycjê co ok. 30 sekund.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (14, 'Rozci¹ganie miêœni naramiennych', 'Rozci¹gaj¹ce', 3, 20, 'Pocz¹tkuj¹cy', 2, 
'W pozycji stoj¹cej zegnij ³okieæ, postaraj siê za³o¿yæ d³oñ rêki zginanej za plecy. Z pozycji wyjœciowej zacznij przesuwaæ rêkê ku górze, w stronê g³owy. Postaraj siê równie¿ cofn¹æ bark po stronie rozci¹ganej poprzez przyci¹gniecie ³opatki do krêgos³upa. Rozci¹ganie wykonuj przez oko³o 90–120 sekund dla jednej koñczyny, staraj¹c siê systematycznie pog³êbiaæ pozycjê rozci¹gania co oko³o 30 sekund.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (15, 'Rozci¹ganie miêœni dwug³owych', 'Rozci¹gaj¹ce', 4, 30, 'Œredniozaawansowany', 2, 
'Pozycja le¿¹ca, jedna noga wyprostowana, druga ugiêta w kolanie. Ugiêt¹ nogê unieœ tak, by móc zapleœæ d³onie z ty³u uda. Postaraj siê, aby udo by³o ustawione prostopadle do pod³o¿a. W pozycji wyjœciowej zacznij delikatnie prostowaæ kolano do momentu odczucia napiêcia na tylnej œcianie uda. Staraj siê minimalnie mocniej wyprostowaæ trzyman¹ nogê i pozostañ w tej pozycji oko³o 30 sekund.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (16, 'Rozci¹ganie miêœni poœladkowych', 'Rozci¹gaj¹ce', 6, 60, 'Pocz¹tkuj¹cy', 2, 'Siad wykroczny podparty, noga zakroczna wyprostowana, tu³ów wyprostowany. Noga wykroczna zgiêta w kolanie, miednica skierowana w przód. Po uzyskaniu stabilnej pozycji sprawdŸ, czy kolano nogi wykrocznej znajduje siê w jednej linii z biodrem. Utrzymuj naturaln¹ krzywiznê krêgos³upa, miednicê skieruj ku przodowi, klatkê piersiow¹ lekko wypchnij.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (17, 'Rozci¹ganie miêœni poœladkowych', 'Rozci¹gaj¹ce', 6, 60, 'Pocz¹tkuj¹cy', 2, 
'Le¿¹c na plecach z nogami ugiêtymi w kolanach, za³ó¿ stopê jednej nogi na kolano drugiej nogi asystuj¹cej. Postaraj siê skierowaæ na zewn¹trz kolano nogi zgiêtej. Unieœ tu³ów oraz rêce, zaplataj¹c je na górnej czêœci piszczeli lub z ty³u uda nogi znajduj¹cej siê na pod³o¿u. Zacznij delikatnie przyci¹gaæ za³o¿on¹ nogê w kierunku klatki piersiowej.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (18, 'Rozci¹ganie bicepsów', 'Rozci¹gaj¹ce', 6, 60, 'Pocz¹tkuj¹cy', 2, 
'Stañ bokiem do œciany na odleg³oœæ wyprostowanej rêki, unieœ w bok prost¹ rêkê na wysokoœæ barku, skieruj palce w ty³. Delikatnie odwodz¹c rêkê w ty³, u³ó¿ d³oñ wewnêtrzn¹ stron¹ do œciany. Zachowaj naturaln¹ krzywiznê krêgos³upa, g³owa stanowi przed³u¿enie krêgos³upa, klatka piersiowa wypchniêta. Z pozycji wyjœciowej zacznij delikatnie skrêcaæ tu³ów i biodra w przeciwn¹ stronê do rêki rozci¹ganej.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (19, 'Rozci¹ganie tricepsów', 'Rozci¹gaj¹ce', 6, 60, 'Pocz¹tkuj¹cy', 2, 
'Pozycja stoj¹ca, zginaj¹c ³okieæ, unieœ rêkê ponad g³owê. Postaraj siê siêgn¹æ d³oni¹ i przedramieniem za g³owê. Drug¹ rêk¹ z³ap za ³okieæ rêki czynnej. Zachowaj naturaln¹ krzywiznê krêgos³upa, g³owa stanowi przed³u¿enie krêgos³upa, klatka piersiowa wypchniêta. Z pozycji wyjœciowej postaraj siê za pomoc¹ si³y rêki asystuj¹cej obni¿aæ pozycjê ³okcia rêki rozci¹ganej i jednoczeœnie przyci¹gaæ j¹ w przeciwleg³¹ stronê. Postaraj siê utrzymywaæ maksymalnie zgiêty ³okieæ rêki rozci¹ganej. ', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (20, 'Rozci¹ganie miêœni czworog³owych', 'Rozci¹gaj¹ce', 45, 12, 'Pocz¹tkuj¹cy', 0, 
'Klêk wykroczny, noga zakroczna spoczywa swobodnie na pod³o¿u. Miednica skierowana w przód, g³owa stanowi przed³u¿enie krêgos³upa, ca³a stopa nogi wykrocznej przylega do pod³o¿a. Postaraj siê zachowaæ fizjologiczn¹ krzywiznê krêgos³upa, szczególnie w odcinku lêdŸwiowym. Z pozycji wyjœciowej unieœ nogê zakroczn¹, jednoczeœnie staraj siê z³apaæ okolicê kostki unoszonej nogi. Unosz¹c nogê, postaraj siê rêk¹ przyci¹gn¹æ stopê nogi rozci¹ganej do poœladka. ', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (21, 'Plank', 'Si³owe', 3, 30, 'Pocz¹tkuj¹cy', 0, 'Trzymanie pozycji plank', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (22, 'Pompki', 'Si³owe', 7, 60, 'Pocz¹tkuj¹cy', 15, 'Pompki na p³asko', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (23, 'Przysiady', 'Si³owe', 6, 60, 'Pocz¹tkuj¹cy', 15, 'Stañ w rozkroku na szerokoœæ bider i zrób przysiad', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (24, 'Poziomka', 'Si³owe', 3, 30, 'Zaawansowany', 0, 
' Siad prosty na pod³odze. Rêce u³o¿one na pod³odze w okolicy bioder. Z pozycji wyjœciowej wykonaj podpór na ramionach, unosz¹c wyprostowane nogi w górê, tak aby pozosta³y w pozycji bliskiej równoleg³ej do pod³ogi. Utrzymaj nogi w górnej pozycji przez okreœlony czas, nastêpnie spokojnym ruchem opuœæ cia³o do pozycji wyjœciowej.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (25, 'Mountain climbers', 'Cardio', 3, 30, 'Œredniozaawansowany', 15, 'Pozycjê wyjœciow¹ zaczynamy od podporu przodem, a kontakt z pod³o¿em maj¹ jedynie d³onie i stopy. Utrzymuj¹c wspomnian¹ pozycjê przyci¹gamy dynamicznie na zmianê raz jedno, raz drugie kolano do klatki piersiowej. Miêœnie brzucha oraz miêœnie poœladkowe powinny byæ w ci¹g³ym napiêciu. Æwiczenie wykonujemy dynamicznie wykonuj¹c kontrolowany ruch.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (26, 'Deska boczna', 'Si³owe', 4, 30, 'Œredniozaawansowany', 2, 'Trzymanie pozycji deski bocznej', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (27, 'Deska na kolanach', 'Si³owe', 3, 30, 'Pocz¹tkuj¹cy', 0, 'Pozycja klêku podpartego. Z klêku podpartego przejdŸ do podporu na przedramionach. Podczas utrzymywania pozycji pamiêtaj o równym oddechu, utrzymuj napiêcie w miêœniach brzucha oraz poœladków.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (28, 'No¿yce nogami', 'Si³owe', 4, 40, 'Œredniozaawansowany', 20, 
'Pozycja le¿¹ca. Ramiona ustawione wzd³u¿ cia³a, d³onie pod poœladkami. Nogi ugiête w kolanach. Stopy oparte o pod³o¿e. Odcinek lêdŸwiowy krêgos³upa dotyka maty. Broda przyklejona do klatki piersiowej. WeŸ wdech, unieœ nogi ustawione pod k¹tem 45 stopni. Wykonuj naprzemienne wznosy nogami góra–dó³. Wykonuj krótkie wdechy, utrzymuj¹c sta³e napiêcie miêœni brzucha.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (29, 'Krab', 'Si³owe', 6, 60, 'Pocz¹tkuj¹cy', 20, 
'Podpór ty³em, kolana ugiête, ramiona wyprostowane. Utrzymuj¹c pozycjê wyjœciow¹, rozpocznij wykonywanie ma³ych kroków po kwadracie. Podczas ruchu stale utrzymuj biodra nad pod³og¹. Æwiczenie wykonuj okreœlony czas.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (30, 'Przeskoki ³y¿wiarza', 'Si³owe', 6, 60, 'Pocz¹tkuj¹cy', 20, 'Æwiczenie polega na wykonywaniu dynamicznych przeskoków na boki, z nogi na nogê. Wraz z prac¹ nóg postaraj siê zsynchronizowaæ pracê ramion.', NULL);

-- gym equipment
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (1, 1, 1, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (2, 1, 1, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (3, 1, 1, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (4, 1, 2, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (5, 1, 2, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (6, 1, 3, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (7, 1, 3, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (8, 1, 4, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (9, 1, 4, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (10, 1, 5, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (11, 1, 5, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (12, 1, 5, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (13, 1, 6, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (14, 1, 6, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (15, 1, 7, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (16, 1, 7, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (17, 1, 7, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (18, 1, 8, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (19, 1, 8, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (20, 1, 8, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (21, 1, 9, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (22, 1, 9, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (23, 1, 10, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (24, 1, 11, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (25, 1, 12, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (26, 1, 13, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (27, 1, 14, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (28, 1, 15, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (29, 1, 16, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (30, 1, 17, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (31, 1, 17, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (32, 1, 16, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (33, 1, 15, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (34, 1, 14, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (35, 1, 13, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (36, 1, 12, TO_DATE('2023-12-01', 'YYYY-MM-DD'));
INSERT INTO gym_equipment (gym_equipment_id, gym_id, equipment_id, purchase_date) 
values (37, 1, 11, TO_DATE('2023-12-01', 'YYYY-MM-DD'));

-- gym classe
INSERT INTO gym_classe (gym_classe_id, name, price, duration, max_people, description)
values (1, 'Aerobik', 18, 60, 30, 'Opis aerobiku');
INSERT INTO gym_classe (gym_classe_id, name, price, duration, max_people, description)
values (2, 'Trening indywidualny', 100, 60, 1, 'Opis treningu indywidualnego');
INSERT INTO gym_classe (gym_classe_id, name, price, duration, max_people, description)
values (3, 'Zumba', 20, 80, 25, 'Opis zumby');
INSERT INTO gym_classe (gym_classe_id, name, price, duration, max_people, description)
values (4, 'Tabata', 30, 45, 30, 'Opis tabaty');
INSERT INTO gym_classe (gym_classe_id, name, price, duration, max_people, description)
values (5, 'Joga', 50, 60, 15, 'Opis jogi');
INSERT INTO gym_classe (gym_classe_id, name, price, duration, max_people, description)
values (6, 'Streching', 15, 60, 30, 'Opis strechingu');
INSERT INTO gym_classe (gym_classe_id, name, price, duration, max_people, description)
values (7, 'P³aski brzuch', 30, 45, 25, 'Opis p³askiego brzucha');
INSERT INTO gym_classe (gym_classe_id, name, price, duration, max_people, description)
values (8, 'Pilates', 25, 60, 30, 'Opis pilatesu');
INSERT INTO gym_classe (gym_classe_id, name, price, duration, max_people, description)
values (9, 'Zdrowy krêgos³up', 40, 90, 20, 'Opis zdrowego krêgos³upu');
INSERT INTO gym_classe (gym_classe_id, name, price, duration, max_people, description)
values (10, 'TBC', 40, 55, 30, 'Opis TBC');

-- locker
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (1, 101, 1);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (2, 102, 1);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (3, 103, 1);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (4, 104, 1);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (5, 105, 1);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (6, 106, 1);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (7, 107, 1);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (8, 108, 1);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (9, 109, 1);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (10, 110, 1);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (11, 111, 1);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (12, 112, 1);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (13, 113, 1);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (14, 114, 1);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (15, 101, 2);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (16, 102, 2);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (17, 103, 2);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (18, 104, 2);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (19, 105, 2);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (20, 106, 2);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (21, 107, 2);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (22, 108, 2);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (23, 109, 2);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (24, 110, 2);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (25, 111, 2);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (26, 112, 2);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (27, 113, 2);
INSERT INTO LOCKER (LOCKER_ID, locker_number, gym_id) values (28, 114, 2);


-- week schedule
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (15, 'wtorek', '17:15', 4, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (16, 'wtorek', '16:00', 2, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (3, 'wtorek', '14:45', 2, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (4, 'wtorek', '18:15', 2, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (5, 'œroda', '15:00', 2, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (6, 'œroda', '16:00', 2, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (7, 'œroda', '15:00', 2, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (8, 'œroda', '14:00', 2, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (9, 'czwartek', '12:00', 2, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (10, 'czwartek', '13:15', 2, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (11, 'pi¹tek', '12:00', 2, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (12, 'czwartek', '18:00', 6, 5);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (13, 'œroda', '20:00', 9, 5);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (14, 'poniedzia³ek', '17:00', 5, 5);

-- gym visit
INSERT INTO GYM_VISIT (entry_time, departure_time, gym_gym_id, client_user_id, locker_locker_id)
VALUES (TO_DATE('2023-12-15 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2023-12-15 12:00:00', 'YYYY-MM-DD HH24:MI:SS'), 1, 1, 1);

INSERT INTO GYM_VISIT (entry_time, departure_time, gym_gym_id, client_user_id, locker_locker_id)
VALUES (TO_DATE('2023-12-14 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2023-12-14 12:00:00', 'YYYY-MM-DD HH24:MI:SS'), 1, 1, 1);

INSERT INTO GYM_VISIT (entry_time, departure_time, gym_gym_id, client_user_id, locker_locker_id)
VALUES (TO_DATE('2023-12-13 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2023-12-13 12:00:00', 'YYYY-MM-DD HH24:MI:SS'), 1, 1, 1);

-- exercise history
INSERT INTO EXERCISE_HISTORY (EXERCISE_DATE, DURATION, REPETITIONS_NUMBER, EXERCISE_COMMENT, GYM_ID, EXERCISE_ID, TRAINER_ID, CLIENT_ID)
VALUES (TIMESTAMP '2023-12-15 10:10:00', 1800, 0, '', 1, 1, null, 1);

INSERT INTO EXERCISE_HISTORY_PARAM_VALUE (VALUE, PARAMETER_ID, EXERCISE_HISTORY_ID)
VALUES (4968, 2, 51);

INSERT INTO EXERCISE_HISTORY (EXERCISE_DATE, DURATION, REPETITIONS_NUMBER, EXERCISE_COMMENT, GYM_ID, EXERCISE_ID, TRAINER_ID, CLIENT_ID, CALORIES)
VALUES (TIMESTAMP '2023-12-15 10:45:00', 60, 2, '', 1, 12, null, 1, 9);

INSERT INTO EXERCISE_HISTORY (EXERCISE_DATE, DURATION, REPETITIONS_NUMBER, EXERCISE_COMMENT, GYM_ID, EXERCISE_ID, TRAINER_ID, CLIENT_ID, CALORIES)
VALUES (TIMESTAMP '2023-12-15 10:46:45', 60, 2, '', 1, 16, null, 1, 6);

-- gym ticket history
-- dniowe
INSERT INTO GYM_ticket_history (purchase_date, activation_date, gym_ticket_offer_id, discount_id, client_id)
VALUES (TO_DATE('2023-11-01', 'YYYY-MM-DD'), TO_DATE('2023-11-01', 'YYYY-MM-DD'), 2, null, 1);

INSERT INTO GYM_ticket_history (purchase_date, activation_date, gym_ticket_offer_id, discount_id, client_id)
VALUES (TO_DATE('2023-12-15', 'YYYY-MM-DD'), TO_DATE('2023-11-15', 'YYYY-MM-DD'), 2, 3, 1);

INSERT INTO GYM_ticket_history (purchase_date, activation_date, gym_ticket_offer_id, discount_id, client_id)
VALUES (TO_DATE('2023-12-16', 'YYYY-MM-DD'), null, 2, null, 1);

-- wejsciowe
-- wygas³y
INSERT INTO GYM_ticket_history (purchase_date, activation_date, gym_ticket_offer_id, discount_id, client_id)
VALUES (TO_DATE('2023-11-01', 'YYYY-MM-DD'), TO_DATE('2023-11-01', 'YYYY-MM-DD'), 4, null, 2);

INSERT INTO GYM_VISIT (entry_time, departure_time, gym_gym_id, client_user_id, locker_locker_id)
VALUES (TO_DATE('2023-11-01 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2023-11-01 12:00:00', 'YYYY-MM-DD HH24:MI:SS'), 1, 2, 1);

-- aktywny
INSERT INTO GYM_ticket_history (purchase_date, activation_date, gym_ticket_offer_id, discount_id, client_id)
VALUES (TO_DATE('2023-12-01', 'YYYY-MM-DD'), TO_DATE('2023-12-01', 'YYYY-MM-DD'), 5, null, 2);

INSERT INTO GYM_VISIT (entry_time, departure_time, gym_gym_id, client_user_id, locker_locker_id)
VALUES (TO_DATE('2023-12-01 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2023-12-01 12:00:00', 'YYYY-MM-DD HH24:MI:SS'), 1, 2, 1);

INSERT INTO GYM_VISIT (entry_time, departure_time, gym_gym_id, client_user_id, locker_locker_id)
VALUES (TO_DATE('2023-12-02 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2023-12-02 12:00:00', 'YYYY-MM-DD HH24:MI:SS'), 1, 2, 1);

-- nieaktywny
INSERT INTO GYM_ticket_history (purchase_date, activation_date, gym_ticket_offer_id, discount_id, client_id)
VALUES (TO_DATE('2023-12-01', 'YYYY-MM-DD'), null, 5, null, 2);