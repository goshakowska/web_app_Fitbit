-- training goal
INSERT INTO training_goal (training_goal_id, name) VALUES (1, 'Redukcja wagi');
INSERT INTO training_goal (training_goal_id, name) VALUES (2, 'Zbudowanie masy');
INSERT INTO training_goal (training_goal_id, name) VALUES (3, 'Zwi�kszenie wytrzyma�o�ci');
INSERT INTO training_goal (training_goal_id, name) VALUES (4, 'Zwi�kszenie gibko�ci');
INSERT INTO training_goal (training_goal_id, name) VALUES (5, 'Poprawa zdrowia og�lnego');

-- equipment
INSERT INTO equipment (equipment_id, name) VALUES (1, 'Bie�nia');
INSERT INTO equipment (equipment_id, name) VALUES (2, 'Rower treningowy');
INSERT INTO equipment (equipment_id, name) VALUES (3, 'Wio�larz');
INSERT INTO equipment (equipment_id, name) VALUES (4, '�awka do wyciskania');
INSERT INTO equipment (equipment_id, name) VALUES (5, 'Suwnica do martwego ci�gu');
INSERT INTO equipment (equipment_id, name) VALUES (6, 'Maszyna do przysiad�w');
INSERT INTO equipment (equipment_id, name) VALUES (7, 'Dr��ek do podci�gania');
INSERT INTO equipment (equipment_id, name) VALUES (8, 'Hantle');
INSERT INTO equipment (equipment_id, name) VALUES (9, 'Orbitrek');
INSERT INTO equipment (equipment_id, name) VALUES (10, 'Pi�ka do stabilizacji');
INSERT INTO equipment (equipment_id, name) VALUES (11, 'Stepper');
INSERT INTO equipment (equipment_id, name) VALUES (12, 'Hula-hop');
INSERT INTO equipment (equipment_id, name) VALUES (13, 'Kostka do jogi');
INSERT INTO equipment (equipment_id, name) VALUES (14, 'Roller');
INSERT INTO equipment (equipment_id, name) VALUES (15, 'Suwnica na nogi');
INSERT INTO equipment (equipment_id, name) VALUES (16, 'Atlas');
INSERT INTO equipment (equipment_id, name) VALUES (17, 'Pi�ka do stabilizacji');

-- gym
INSERT INTO gym (gym_id, name, phone_number, city, street, house_number, county, zip_code,
                 monday_opening, monday_closing, tuesday_opening, tuesday_closing,
                 wednesday_opening, wednesday_closing, thursday_opening, thursday_closing,
                 friday_opening, friday_closing, saturday_opening, saturday_closing,
                 sunday_opening, sunday_closing)
VALUES
(1, 'FitBit Zero Fat', '123456789', 'T�uszcz', 'ul. Warszawska', '37', 'Polska', '05-240',
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
(3, 'FitBit Minus', '111222333', 'Wo�omin', 'ul. Wile�ska', '25', 'Polska', '05-200',
 '07:00', '20:00', '07:00', '20:00', '07:00', '22:00', '07:00', '19:00',
 '07:00', '20:00', '07:00', '20:00', '07:00', '20:00');

INSERT INTO gym (gym_id, name, phone_number, city, street, house_number, county, zip_code,
                 monday_opening, monday_closing, tuesday_opening, tuesday_closing,
                 wednesday_opening, wednesday_closing, thursday_opening, thursday_closing,
                 friday_opening, friday_closing, saturday_opening, saturday_closing,
                 sunday_opening, sunday_closing)
VALUES
(4, 'FitBit Malinka', '789789789', 'Zakopane', 'ul. Krzept�wki', '99', 'Polska', '34-500',
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
(6, 'FitBit Neptun', '753753753', 'Gda�sk', 'ul. Gotycka', '20', 'Polska', '80-253',
 '07:00', '22:00', '07:00', '22:00', '06:00', '21:00', '07:00', '22:00',
 '07:00', '21:00', '08:00', '20:00', '10:00', '20:00');

 -- parameter
INSERT INTO parameter (parameter_id, name, units) VALUES (1, 'Obci��enie', 'kg');
INSERT INTO parameter (parameter_id, name, units) VALUES (2, 'Dystans', 'm');
INSERT INTO parameter (parameter_id, name, units) VALUES (3, 'Wysoko��', 'cm');

-- ticket
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (1, 'Standardowy', 60, 250, 'Dniowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (2, 'Standardowy', 30, 150, 'Dniowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (3, 'Standardowy', 7, 50, 'Dniowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (4, 'Standardowy', 1, 15, 'Wej�ciowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (5, 'Standardowy', 5, 70, 'Wej�ciowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (6, 'Standardowy', 10, 130, 'Wej�ciowy');
--INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (7, 'Studencki', 60, 200, 'Dniowy');
--INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (8, 'Studencki', 30, 110, 'Dniowy');
--INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (9, 'Studencki', 7, 30, 'Dniowy');
--INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (10, 'Seniorski', 60, 220, 'Dniowy');
--INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (11, 'Seniorski', 30, 135, 'Dniowy');
--INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (12, 'Seniorski', 7, 40, 'Dniowy');
--INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (13, 'Studencki', 1, 12, 'Wej�ciowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (14, 'Studencki', 5, 55, 'Wej�ciowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (15, 'Studencki', 10, 100, 'Wej�ciowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (16, 'Seniorski', 1, 13, 'Wej�ciowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (17, 'Seniorski', 5, 60, 'Wej�ciowy');
INSERT INTO gym_ticket_offer (gym_ticket_offer_id, name, duration, price, type) VALUES (18, 'Seniorski', 10, 110, 'Wej�ciowy');

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
VALUES (13, '�wi�ta 2023', TO_DATE('2023-12-01', 'YYYY-MM-DD'), TO_DATE('2024-01-31', 'YYYY-MM-DD'), 20, 1);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (14, '�wi�ta 2023', TO_DATE('2023-12-01', 'YYYY-MM-DD'), TO_DATE('2024-01-31', 'YYYY-MM-DD'), 20, 2);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (15, '�wi�ta 2023', TO_DATE('2023-12-01', 'YYYY-MM-DD'), TO_DATE('2024-01-31', 'YYYY-MM-DD'), 20, 3);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (16, '�wi�ta 2023', TO_DATE('2023-12-01', 'YYYY-MM-DD'), TO_DATE('2024-01-31', 'YYYY-MM-DD'), 20, 4);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (17, '�wi�ta 2023', TO_DATE('2023-12-01', 'YYYY-MM-DD'), TO_DATE('2024-01-31', 'YYYY-MM-DD'), 20, 5);
INSERT INTO discount (discount_id, name, start_date, stop_date, discount_percentages, gym_ticket_offer_id)
VALUES (18, '�wi�ta 2023', TO_DATE('2023-12-01', 'YYYY-MM-DD'), TO_DATE('2024-01-31', 'YYYY-MM-DD'), 20, 6);


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
VALUES (3, 'chlopi', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'jagus123@edu.pl', '157426852', 'Jagna', 'Paczesi�wna', 'K', 185, TO_DATE('2003-07-01', 'YYYY-MM-DD'),
    '�redniozaawansowany', 80, 1, 80, 4, 1);

insert into client (client_id, login, password_hash, email, phone_number, name, surname,
gender, height, birth_year, advancement, target_weight, training_frequency, training_time, training_goal_id, gym_id)
VALUES (4, 'blyskawica', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'hedwiga@edu.pl', '456456456', 'Henryk', 'Garncarz', 'M', 165, TO_DATE('1980-07-31', 'YYYY-MM-DD'),
    'zaawansowany', 65, 2, 60, 2, 1);

insert into client (client_id, login, password_hash, email, phone_number, name, surname,
gender, height, birth_year, advancement, target_weight, training_frequency, training_time, training_goal_id, gym_id)
VALUES (5, 'diuna3000', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'diuna456@edu.pl', '157157157', 'Pawe�', 'Atryda', 'M', 178, TO_DATE('1976-12-12', 'YYYY-MM-DD'),
    'pocz�tkuj�cy', 75, 4, 50, 5, 4);

insert into client (client_id, login, password_hash, email, phone_number, name, surname,
gender, height, birth_year, advancement, target_weight, training_frequency, training_time, training_goal_id, gym_id)
VALUES (6, 'miodek', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'pszczolki@edu.pl', '157426854', 'Kubu�', 'Puchatek', 'M', 160, TO_DATE('2000-07-01', 'YYYY-MM-DD'),
    'pocz�tkuj�cy', 65, 1, 30, 4, 1);

insert into client (client_id, login, password_hash, email, phone_number, name, surname,
gender, height, birth_year, advancement, target_weight, training_frequency, training_time, training_goal_id, gym_id)
VALUES (7, 'bennet_e', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'dumaiuprzedzenie@edu.pl', '157426745', 'El�bieta', 'Bennet', 'K', 170, TO_DATE('1990-08-01', 'YYYY-MM-DD'),
    '�redniozaawansowany', 70, 1, 90, 5, 1);

insert into client (client_id, login, password_hash, email, phone_number, name, surname,
gender, height, birth_year, advancement, target_weight, training_frequency, training_time, training_goal_id, gym_id)
VALUES (8, 'edward123', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'o_zmierzchu@edu.pl', '157789789', 'Edward', 'Cullen', 'M', 179, TO_DATE('1910-09-11', 'YYYY-MM-DD'),
    '�redniozaawansowany', 75, 3, 60, 3, 1);

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
VALUES (3, 'laleczka', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'laleczka@edu.pl', '555555555', 'Izabela', '��cka',
'K', 'trener', 3100, Null, 1);

insert into employee (employee_id, login, password_hash, email, phone_number, name, surname, gender,type, standar_salary, locker_id, gym_id)
VALUES (4, 'trener_stachu', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'stasiek_w@edu.pl', '141141141', 'Stanis�aw', 'Wokulski',
'M', 'trener', 4000, Null, 1);

insert into employee (employee_id, login, password_hash, email, phone_number, name, surname, gender,type, standar_salary, locker_id, gym_id)
VALUES (5, 'stary_subiekt', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'napoleon@edu.pl', '854753621', 'Ignacy', 'Rzecki',
'M', 'trener', 2000, Null, 1);

insert into employee (employee_id, login, password_hash, email, phone_number, name, surname, gender,type, standar_salary, locker_id, gym_id)
VALUES (6, 'trener_zbyszko', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'krzyzacy@edu.pl', '754862156', 'Zbyszko', 'Bogda�ski',
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
VALUES (10, 'michalki', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'pan_michal@edu.pl', '456269845', 'Micha�', 'Wo�odyjowski',
'M', 'trener', 2600, Null, 1);


-- employee menadżer
insert into employee(employee_id, login, password_hash, email, phone_number, name, surname, gender, type, standar_salary, gym_id)
values (12, 'alek', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'szef@edu.pl', '234123673', 'Aleksander', 'Dawidowski', 'M', 'menadżer', 5000, 1);


-- employee portier
insert into employee(employee_id, login, password_hash, email, phone_number, name, surname, gender, type, standar_salary, gym_id)
values (11, 'kleks', 'pbkdf2_sha256$600000$RTDRIBN0ZLuYMCbfdILsco$ef/H2RLGxnHS+A4h5XXUeU20dt5FqiFb0QnBaB3/LvI=', 'akademia@edu.pl', '111111111', 'Ambroży', 'Kleks', 'M', 'portier', 3000, 1);


-- exercise
INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (1, 'Bieganie na bie�ni', 'Cardio', 300, 1800, '�redniozaawansowany', 0, 'Biegnij na bie�ni', 1);
-- dystans 5km czyli 5000m
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (1, 5000, 2, 1);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (2, 'Jazda na rowerku', 'Cardio', 250, 1200, 'Pocz�tkuj�cy', 0, 'Jed� na rowerku stacjonarnym', 2);
-- dystans 7km czyli 7000m
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (2, 7000, 2, 2);


INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (3, 'Wios�owanie', 'Si�owe', 200, 1500, '�redniozaawansowany', 0, 'Trening si�owy na wio�larzu', 3);
-- dystans 5km czyli 5000m
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (3, 5000, 2, 3);


INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (4, 'Wyciskanie sztangi', 'Si�owe', 80, 100, 'Zaawansowany', 10, 
'Po�� si� na �awce p�askiej. Chwy� sztang� nachwytem na tak� szeroko��, aby w po�owie wykonywania ruchu k�t mi�dzy ramieniem a przedramieniem wynosi� 90 stopni. �opatki �ci�gni�te, barki opuszczone i mocno doci�ni�te do �aweczki. Zachowaj naturalne ustawienie kr�gos�upa � odcinek l�d�wiowy lekko uniesiony, po�ladki na �aweczce.Utrzymuj�c prawid�ow� pozycj� wyj�ciow�, wykonaj wdech i powolnym ruchem opu�� sztang� do �rodkowej cz�ci klatki piersiowej, uginaj�c ramiona w �okciach. Po przytrzymaniu sztangi w okolicach klatki przez u�amek sekundy zacznij unosi� sztang� z powrotem do pozycji wyj�ciowej, wykonuj�c wydech powietrza. Skup si�, aby wyciskanie nast�powa�o z mi�nia piersiowego. W momencie wyprostowania ramion ze sztang� (unikaj przeprostu w �okciach) mocno dopnij mi�sie� piersiowy, po czym ponownie zacznij opuszcza� sztang�.', 4);
-- obci��enie 20 kg wysoko�� 40 cm
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (4, 20, 1, 4);
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (5, 40, 3, 4);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (5, 'Martwy ci�g', 'Si�owe', 6, 60, 'Zaawansowany', 10, 
'P�przysiad przed sztang�, cia�o mocno pochylone. Sztanga nad stopami, blisko piszczeli. Ramiona wyprostowane, ustawione na szeroko�� bark�w. Plecy wyprostowane, g�owa powinna stanowi� przed�u�enie kr�gos�upa. Utrzymuj�c prawid�ow� pozycj� wyj�ciow�, wykonaj mocny wdech powietrza do brzucha. Wybierz luz na sztandze, a nast�pnie zacznij unosi� sztang� z ziemi, wykonuj�c wyprost w stawach biodrowych oraz kolanowych. Sztang� prowad� blisko n�g, nie pozw�l, aby podczas ruchu plecy wygi�y si� w �uk. Ko�cz�c ruch, utrzymuj mocne napi�cie mi�ni brzucha oraz po�ladk�w i wykonaj wydech. Utrzymaj pozycj� przez sekund�, nast�pnie nabieraj�c kolejny wdech, w kontrolowany spos�b odstaw sztang� na pod�og�. Utrzymuj plecy proste, a mi�nie brzucha mocno napi�te. Wykonaj wyznaczon� liczb� powt�rze�, za ka�dym razem odk�adaj sztang� na pod�og�.', 5);
-- obci��enie 20 kg wysoko�� 80cm
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (6, 20, 1, 5);
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (7, 80, 3, 5);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (6, 'Poliquin step-up', 'Si�owe', 5, 60, '�redniozaawansowane', 15, 
'Pozycja stoj�ca na jednej nodze na podwy�szeniu ok. 20 cm. Pod pi�t� minimalne podniesienie ok. 2 cm. Sylwetka wyprostowana, ramiona ustawione na biodrach lub wzd�u� cia�a. Druga noga w powietrzu, stopa ustawiona w zgi�ciu grzbietowym (palce ko�cami skierowane w g�r�).Wykonaj g��boki wdech. Powoli rozpocznij uginanie nogi w kolanie, zachowuj�c biodra na jednej wysoko�ci. Utrzymuj�c prawid�ow� postaw�, schod� przez oko�o 4 sekundy, tak aby druga wyprostowana noga dotkn�a pi�t� pod�ogi. Nast�pnie bez wsparcia (odbicia) nogi na pod�odze wyprostuj nog� w kolanie i wraz z wdechem wr�� do pozycji pocz�tkowej. W pozycji pocz�tkowej pami�taj o utrzymaniu kolana w aktywnym wypro�cie (bez przeprostu). ', 11);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (7, 'Podci�ganie na dr��ku', 'Si�owe', 3, 30, 'Pocz�tkuj�cy', 6, 
'Dr��ek z�apany nachwytem (kciuki skierowane do wewn�trz), szerzej ni� rozstaw bark�w. Ramiona wyprostowane, wzrok skierowany w g�r�. We� wdech, ruch rozpocznij od bardzo dynamicznego, mocnego �ci�gni�cia �opatek w d� i do siebie po��czonego z mocn� prac� ramion. Podci�gaj si� tak, jakby� chcia� dotkn�� dr��ka brzuchem w okolicy pasa. W najwy�szym punkcie spr�buj zatrzyma� ruch poprzez mocne spi�cie mi�ni. Nast�pnie kontrolowanym ruchem opu�� cia�o.', 7);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (8, 'Z-press', 'Si�owe', 6, 60, 'Pocz�tkuj�cy', 12, 
'Pozycja siedz�ca, nogi rozstawione tak, aby zapewnia�y stabiln� postaw�. Ramiona w g�rze, hantle na wysoko�ci g�owy. �okcie skierowane w d�. Utrzymuj�c prawid�ow� pozycj� wyj�ciow�, we� wdech i zacznij wyciska� ci�ar nad g�ow�. W ko�cowej fazie ruchu wykonaj wydech. Nast�pnie powolnym ruchem opu�� hantle, wykonuj�c p�ynny wdech.', 8);
-- obci��enie 2kg
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (8, 2, 1, 8);


INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (9, 'Trening na orbitreku', 'Cardio', 160, 1800, '�redniozaawansowany', 0, 'Intensywny trening na orbitreku', 9);
-- dystans 5km 5000m
INSErT INTO standard_parameter_value (standard_parameter_value_id, value, parameter_id, exercise_id)
values (9, 5000, 2, 9);


INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (10, 'Przyci�ganie kolan na pi�ce', 'Si�owe', 160, 60, 'Pocz�tkuj�cy', 10, 
'Podp�r przodem z nogami ustawionymi na pi�ce. Z pozycji wyj�ciowej rozpocznij wykonywanie unoszenia bioder. R�wnocze�nie uginaj kolana, kieruj�c je do klatki piersiowej. W momencie maksymalnego spi�cia utrzymaj pozycj� przez u�amek sekundy. Spokojnym, kontrolowanym ruchem wr�� do pozycji wyj�ciowej.', 10);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (11, 'Obroty szyi', 'Rozci�gaj�ce', 3, 30, 'Pocz�tkuj�cy', 6, 'Wykonuj skr�ty szyi. Wykonuj je powoli i ostro�nie, w lewo i w prawo.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (12, 'Kobra', 'Rozci�gaj�ce', 3, 20, 'Pocz�tkuj�cy', 1, 'Le�enie przodem, d�onie oparte na wysoko�ci klatki piersiowej. Z pozycji wyj�ciowej unie� tu��w, trzymaj�c biodra oparte na pod�odze. Wzrok skieruj przed siebie. Utrzymaj pozycj� przez 20 sekund, a nast�pnie wr�� do pozycji wyj�ciowej.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (13, 'Rozci�ganie mi�ni grzbietu', 'Rozci�gaj�ce', 3, 20, 'Pocz�tkuj�cy', 2, 
'W kl�ku podpartym wysu� r�k� w prz�d po stronie rozci�ganej za o� �rodkow� cia�a. D�o� wysuni�tej r�ki ustaw wierzchni� stron� do pod�o�a. Drug� r�k� u�� na wysuni�tej r�ce, jednocze�nie naciskaj na ni� tak, by nie zmieni�a swojej pozycji. Opieraj ci�ar cia�a na kolanach oraz wysuni�tej r�ce, postaraj si� delikatnie skr�ca� tu��w, przeno� ci�ar cia�a w bok na stron� wysuni�tej r�ki. Podczas wykonywania skr�tu tu�owia postaraj si� wykona� lekkie ty�opochylenie miednicy, szczeg�lnie po stronie rozci�ganej. W tej pozycji pozosta� przez oko�o 90�120 sekund, systematycznie pog��biaj pozycj� co ok. 30 sekund.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (14, 'Rozci�ganie mi�ni naramiennych', 'Rozci�gaj�ce', 3, 20, 'Pocz�tkuj�cy', 2, 
'W pozycji stoj�cej zegnij �okie�, postaraj si� za�o�y� d�o� r�ki zginanej za plecy. Z pozycji wyj�ciowej zacznij przesuwa� r�k� ku g�rze, w stron� g�owy. Postaraj si� r�wnie� cofn�� bark po stronie rozci�ganej poprzez przyci�gniecie �opatki do kr�gos�upa. Rozci�ganie wykonuj przez oko�o 90�120 sekund dla jednej ko�czyny, staraj�c si� systematycznie pog��bia� pozycj� rozci�gania co oko�o 30 sekund.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (15, 'Rozci�ganie mi�ni dwug�owych', 'Rozci�gaj�ce', 4, 30, '�redniozaawansowany', 2, 
'Pozycja le��ca, jedna noga wyprostowana, druga ugi�ta w kolanie. Ugi�t� nog� unie� tak, by m�c zaple�� d�onie z ty�u uda. Postaraj si�, aby udo by�o ustawione prostopadle do pod�o�a. W pozycji wyj�ciowej zacznij delikatnie prostowa� kolano do momentu odczucia napi�cia na tylnej �cianie uda. Staraj si� minimalnie mocniej wyprostowa� trzyman� nog� i pozosta� w tej pozycji oko�o 30 sekund.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (16, 'Rozci�ganie mi�ni po�ladkowych', 'Rozci�gaj�ce', 6, 60, 'Pocz�tkuj�cy', 2, 'Siad wykroczny podparty, noga zakroczna wyprostowana, tu��w wyprostowany. Noga wykroczna zgi�ta w kolanie, miednica skierowana w prz�d. Po uzyskaniu stabilnej pozycji sprawd�, czy kolano nogi wykrocznej znajduje si� w jednej linii z biodrem. Utrzymuj naturaln� krzywizn� kr�gos�upa, miednic� skieruj ku przodowi, klatk� piersiow� lekko wypchnij.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (17, 'Rozci�ganie mi�ni po�ladkowych', 'Rozci�gaj�ce', 6, 60, 'Pocz�tkuj�cy', 2, 
'Le��c na plecach z nogami ugi�tymi w kolanach, za�� stop� jednej nogi na kolano drugiej nogi asystuj�cej. Postaraj si� skierowa� na zewn�trz kolano nogi zgi�tej. Unie� tu��w oraz r�ce, zaplataj�c je na g�rnej cz�ci piszczeli lub z ty�u uda nogi znajduj�cej si� na pod�o�u. Zacznij delikatnie przyci�ga� za�o�on� nog� w kierunku klatki piersiowej.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (18, 'Rozci�ganie biceps�w', 'Rozci�gaj�ce', 6, 60, 'Pocz�tkuj�cy', 2, 
'Sta� bokiem do �ciany na odleg�o�� wyprostowanej r�ki, unie� w bok prost� r�k� na wysoko�� barku, skieruj palce w ty�. Delikatnie odwodz�c r�k� w ty�, u�� d�o� wewn�trzn� stron� do �ciany. Zachowaj naturaln� krzywizn� kr�gos�upa, g�owa stanowi przed�u�enie kr�gos�upa, klatka piersiowa wypchni�ta. Z pozycji wyj�ciowej zacznij delikatnie skr�ca� tu��w i biodra w przeciwn� stron� do r�ki rozci�ganej.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (19, 'Rozci�ganie triceps�w', 'Rozci�gaj�ce', 6, 60, 'Pocz�tkuj�cy', 2, 
'Pozycja stoj�ca, zginaj�c �okie�, unie� r�k� ponad g�ow�. Postaraj si� si�gn�� d�oni� i przedramieniem za g�ow�. Drug� r�k� z�ap za �okie� r�ki czynnej. Zachowaj naturaln� krzywizn� kr�gos�upa, g�owa stanowi przed�u�enie kr�gos�upa, klatka piersiowa wypchni�ta. Z pozycji wyj�ciowej postaraj si� za pomoc� si�y r�ki asystuj�cej obni�a� pozycj� �okcia r�ki rozci�ganej i jednocze�nie przyci�ga� j� w przeciwleg�� stron�. Postaraj si� utrzymywa� maksymalnie zgi�ty �okie� r�ki rozci�ganej. ', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (20, 'Rozci�ganie mi�ni czworog�owych', 'Rozci�gaj�ce', 45, 12, 'Pocz�tkuj�cy', 0, 
'Kl�k wykroczny, noga zakroczna spoczywa swobodnie na pod�o�u. Miednica skierowana w prz�d, g�owa stanowi przed�u�enie kr�gos�upa, ca�a stopa nogi wykrocznej przylega do pod�o�a. Postaraj si� zachowa� fizjologiczn� krzywizn� kr�gos�upa, szczeg�lnie w odcinku l�d�wiowym. Z pozycji wyj�ciowej unie� nog� zakroczn�, jednocze�nie staraj si� z�apa� okolic� kostki unoszonej nogi. Unosz�c nog�, postaraj si� r�k� przyci�gn�� stop� nogi rozci�ganej do po�ladka. ', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (21, 'Plank', 'Si�owe', 3, 30, 'Pocz�tkuj�cy', 0, 'Trzymanie pozycji plank', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (22, 'Pompki', 'Si�owe', 7, 60, 'Pocz�tkuj�cy', 15, 'Pompki na p�asko', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (23, 'Przysiady', 'Si�owe', 6, 60, 'Pocz�tkuj�cy', 15, 'Sta� w rozkroku na szeroko�� bider i zr�b przysiad', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (24, 'Poziomka', 'Si�owe', 3, 30, 'Zaawansowany', 0, 
' Siad prosty na pod�odze. R�ce u�o�one na pod�odze w okolicy bioder. Z pozycji wyj�ciowej wykonaj podp�r na ramionach, unosz�c wyprostowane nogi w g�r�, tak aby pozosta�y w pozycji bliskiej r�wnoleg�ej do pod�ogi. Utrzymaj nogi w g�rnej pozycji przez okre�lony czas, nast�pnie spokojnym ruchem opu�� cia�o do pozycji wyj�ciowej.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (25, 'Mountain climbers', 'Cardio', 3, 30, '�redniozaawansowany', 15, 'Pozycj� wyj�ciow� zaczynamy od podporu przodem, a kontakt z pod�o�em maj� jedynie d�onie i stopy. Utrzymuj�c wspomnian� pozycj� przyci�gamy dynamicznie na zmian� raz jedno, raz drugie kolano do klatki piersiowej. Mi�nie brzucha oraz mi�nie po�ladkowe powinny by� w ci�g�ym napi�ciu. �wiczenie wykonujemy dynamicznie wykonuj�c kontrolowany ruch.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (26, 'Deska boczna', 'Si�owe', 4, 30, '�redniozaawansowany', 2, 'Trzymanie pozycji deski bocznej', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (27, 'Deska na kolanach', 'Si�owe', 3, 30, 'Pocz�tkuj�cy', 0, 'Pozycja kl�ku podpartego. Z kl�ku podpartego przejd� do podporu na przedramionach. Podczas utrzymywania pozycji pami�taj o r�wnym oddechu, utrzymuj napi�cie w mi�niach brzucha oraz po�ladk�w.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (28, 'No�yce nogami', 'Si�owe', 4, 40, '�redniozaawansowany', 20, 
'Pozycja le��ca. Ramiona ustawione wzd�u� cia�a, d�onie pod po�ladkami. Nogi ugi�te w kolanach. Stopy oparte o pod�o�e. Odcinek l�d�wiowy kr�gos�upa dotyka maty. Broda przyklejona do klatki piersiowej. We� wdech, unie� nogi ustawione pod k�tem 45 stopni. Wykonuj naprzemienne wznosy nogami g�ra�d�. Wykonuj kr�tkie wdechy, utrzymuj�c sta�e napi�cie mi�ni brzucha.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (29, 'Krab', 'Si�owe', 6, 60, 'Pocz�tkuj�cy', 20, 
'Podp�r ty�em, kolana ugi�te, ramiona wyprostowane. Utrzymuj�c pozycj� wyj�ciow�, rozpocznij wykonywanie ma�ych krok�w po kwadracie. Podczas ruchu stale utrzymuj biodra nad pod�og�. �wiczenie wykonuj okre�lony czas.', NULL);

INSERT INTO exercise (exercise_id, name, type, calories, duration, advancement_level, repetitions_number, description, equipment_id)
VALUES (30, 'Przeskoki �y�wiarza', 'Si�owe', 6, 60, 'Pocz�tkuj�cy', 20, '�wiczenie polega na wykonywaniu dynamicznych przeskok�w na boki, z nogi na nog�. Wraz z prac� n�g postaraj si� zsynchronizowa� prac� ramion.', NULL);

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
values (7, 'P�aski brzuch', 30, 45, 25, 'Opis p�askiego brzucha');
INSERT INTO gym_classe (gym_classe_id, name, price, duration, max_people, description)
values (8, 'Pilates', 25, 60, 30, 'Opis pilatesu');
INSERT INTO gym_classe (gym_classe_id, name, price, duration, max_people, description)
values (9, 'Zdrowy kr�gos�up', 40, 90, 20, 'Opis zdrowego kr�gos�upu');
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
VALUES (5, '�roda', '15:00', 2, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (6, '�roda', '16:00', 2, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (7, '�roda', '15:00', 2, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (8, '�roda', '14:00', 2, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (9, 'czwartek', '12:00', 2, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (10, 'czwartek', '13:15', 2, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (11, 'pi�tek', '12:00', 2, 4);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (12, 'czwartek', '18:00', 6, 5);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (13, '�roda', '20:00', 9, 5);
INSERT INTO WEEK_SCHEDULE (week_schedule_id, week_day, start_time, gym_classe_id, trainer_id)
VALUES (14, 'poniedzia�ek', '17:00', 5, 5);

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
-- wygas�y
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