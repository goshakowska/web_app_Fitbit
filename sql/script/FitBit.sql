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
