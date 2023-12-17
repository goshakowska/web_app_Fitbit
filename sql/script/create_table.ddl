/** Clean scheme
if tables already exist
*/

DECLARE
    v_count  INT;
    v_name VARCHAR2(40);
    TYPE namesarray IS VARRAY(30) OF VARCHAR2(30);   -- ta pierwsza liczba to liczba tabelek
    names    namesarray;
BEGIN
    names := namesarray('client', 'client_data_history', 'client_illness', 'discount', 'employee', 'equipment',
    'exercise_muscle', 'exercise', 'exercise_history', 'exercise_history_param_value', 'exercise_illness',
    'exercise_plan', 'exercise_plan_position', 'exercise_position_value', 'favourite_exercises', 'gym', 'gym_classe',
    'gym_equipment', 'gym_ticket_history', 'gym_ticket_offer', 'gym_visit', 'illness', 'locker', 'muscle_groups',
    'ordered_schedule', 'parameter', 'rating', 'standard_parameter_value', 'training_goal', 'week_schedule');

    FOR i IN 1..names.count LOOP
        v_name := names(i);

        SELECT COUNT(*) INTO v_count FROM user_tables WHERE table_name = upper(v_name);
        IF v_count = 1 THEN
            DBMS_OUTPUT.PUT_LINE('Dropping table: ' || v_name);
            EXECUTE IMMEDIATE 'DROP TABLE '|| v_name || ' CASCADE CONSTRAINTS';
        END IF;
    END LOOP;
END;

/

CREATE TABLE client (
    client_id          INTEGER NOT NULL,
    login              VARCHAR2(25) UNIQUE NOT NULL,
    password_hash      VARCHAR2(100) NOT NULL,
    email              VARCHAR2(30) UNIQUE NOT NULL,
    phone_number       VARCHAR2(13),
    name               VARCHAR2(40) NOT NULL,
    surname            VARCHAR2(40) NOT NULL,
    gender             VARCHAR2(1) NOT NULL,
    height             INTEGER,
    birth_year         DATE NOT NULL,
    advancement        VARCHAR2(40),
    target_weight      INTEGER,
    training_frequency INTEGER,
    training_time      INTEGER,
    training_goal_id   INTEGER,
    gym_id             INTEGER,
    CONSTRAINT gender_check CHECK (gender IN ('M', 'K')),
    CONSTRAINT advancement_check CHECK (advancement IN (('pocz�tkuj�cy', '�redniozaawansowany', 'zaawansowany') OR advancement IS NULL)

LOGGING;

ALTER TABLE client ADD CONSTRAINT client_pk PRIMARY KEY ( client_id );
ALTER TABLE client MODIFY (client_id DEFAULT client_id_seq.NEXTVAL);

CREATE TABLE client_data_history (
    client_data_history_id INTEGER NOT NULL,
    weight                 INTEGER NOT NULL,
    fat_body_level         INTEGER,
    measurement_date       DATE NOT NULL,
    client_id         INTEGER NOT NULL
)
LOGGING;

ALTER TABLE client_data_history ADD CONSTRAINT client_data_history_pk PRIMARY KEY ( client_data_history_id );

CREATE TABLE client_illness (
    illness_id INTEGER NOT NULL,
    client_id  INTEGER NOT NULL
)
LOGGING;

ALTER TABLE client_illness ADD CONSTRAINT client_illness_pk PRIMARY KEY ( illness_id,
                                                                          client_id );

CREATE TABLE discount (
    discount_id          INTEGER NOT NULL,
    name                 VARCHAR2(40),
    start_date           DATE NOT NULL,
    stop_date            DATE,
    discount_percentages INTEGER NOT NULL,
    gym_ticket_offer_id  INTEGER NOT NULL
)
LOGGING;

ALTER TABLE discount ADD CONSTRAINT discount_pk PRIMARY KEY ( discount_id );

CREATE TABLE employee (
    employee_id    INTEGER NOT NULL,
    login          VARCHAR2(25) UNIQUE NOT NULL,
    password_hash  VARCHAR2(100) NOT NULL,
    email          VARCHAR2(30) NOT NULL,
    phone_number   VARCHAR2(13) NOT NULL,
    name           VARCHAR2(40) NOT NULL,
    surname        VARCHAR2(40) NOT NULL,
    gender         VARCHAR2(1) NOT NULL,
    type           VARCHAR2(10) NOT NULL,
    standar_salary INTEGER,
    locker_id      INTEGER,
    gym_id         INTEGER NOT NULL
    CONSTRAINT gender_check CHECK (gender IN ('M', 'K')),
    CONSTRAINT type_check CHECK (type IN ('trener', 'portier', 'menad�er'))
)
LOGGING;

ALTER TABLE employee ADD CONSTRAINT employee_pk PRIMARY KEY ( employee_id );

CREATE TABLE equipment (
    equipment_id INTEGER NOT NULL,
    name         VARCHAR2(40) NOT NULL
)
LOGGING;

ALTER TABLE equipment ADD CONSTRAINT equipment_pk PRIMARY KEY ( equipment_id );

CREATE TABLE exercise_muscle (
    exercise_id      INTEGER NOT NULL,
    muscle_groups_id INTEGER NOT NULL
)
LOGGING;

ALTER TABLE exercise_muscle ADD CONSTRAINT exercise_muscle_pk PRIMARY KEY ( exercise_id,
                                                                              muscle_groups_id );

CREATE TABLE exercise (
    exercise_id        INTEGER NOT NULL,
    name               VARCHAR2(40) NOT NULL,
    type               VARCHAR2(40) NOT NULL,
    calories           INTEGER NOT NULL,
    duration           INTEGER NOT NULL,
    advancement_level  VARCHAR2(40) NOT NULL,
    repetitions_number INTEGER NOT NULL,
    description        CLOB NOT NULL,
    equipment_id       INTEGER
)
LOGGING;

ALTER TABLE exercise ADD CONSTRAINT exercise_pk PRIMARY KEY ( exercise_id );

CREATE TABLE exercise_history (
    exercise_history_id INTEGER NOT NULL,
    exercise_date       DATE NOT NULL,
    duration            INTEGER,
    repetitions_number  INTEGER NOT NULL,
    exercise_comment    CLOB,
    gym_id              INTEGER NOT NULL,
    exercise_id         INTEGER NOT NULL,
    trainer_id          INTEGER,
    client_id           INTEGER NOT NULL
)
LOGGING;

ALTER TABLE exercise_history ADD CONSTRAINT exercise_history_pk PRIMARY KEY ( exercise_history_id );

CREATE TABLE exercise_history_param_value (
    param_value_id      INTEGER NOT NULL,
    value               INTEGER NOT NULL,
    parameter_id        INTEGER NOT NULL,
    exercise_history_id INTEGER
)
LOGGING;

ALTER TABLE exercise_history_param_value ADD CONSTRAINT ehpv_pk PRIMARY KEY ( param_value_id );

CREATE TABLE exercise_illness (
    exercise_exercise_id INTEGER NOT NULL,
    illness_illness_id   INTEGER NOT NULL
)
LOGGING;

ALTER TABLE exercise_illness ADD CONSTRAINT exercise_illness_pk PRIMARY KEY ( exercise_exercise_id,
                                                                              illness_illness_id );

CREATE TABLE exercise_plan (
    exercise_plan_id INTEGER NOT NULL,
    ordered_id       INTEGER NOT NULL,
    done             CHAR(1),
)
LOGGING;

ALTER TABLE exercise_plan ADD CONSTRAINT exercise_plan_pk PRIMARY KEY ( exercise_plan_id );

CREATE TABLE exercise_plan_position (
    exercise_plan_position_id INTEGER NOT NULL,
    position                  INTEGER NOT NULL,
    duration                  INTEGER,
    repetitions_number        INTEGER,
    plan_comment              CLOB,
    exercise_id               INTEGER NOT NULL,
    exercise_plan_id          INTEGER NOT NULL
)
LOGGING;

ALTER TABLE exercise_plan_position ADD CONSTRAINT exercise_plan_position_pk PRIMARY KEY ( exercise_plan_position_id );

CREATE TABLE exercise_position_value (
    exercise_position_value_id INTEGER NOT NULL,
    value                      INTEGER NOT NULL,
    parameter_id               INTEGER NOT NULL,
    exercise_plan_position_id  INTEGER
)
LOGGING;

ALTER TABLE exercise_position_value ADD CONSTRAINT exercise_position_value_pk PRIMARY KEY ( exercise_position_value_id );

CREATE TABLE favourite_exercises (
    exercise_id INTEGER NOT NULL,
    client_id   INTEGER NOT NULL
)
LOGGING;

ALTER TABLE favourite_exercises ADD CONSTRAINT favourite_exercises_pk PRIMARY KEY ( exercise_id,
                                                                                    client_id );

CREATE TABLE gym (
    gym_id            INTEGER NOT NULL,
    name              VARCHAR2(30) NOT NULL,
    phone_number      VARCHAR2(13),
    city              VARCHAR2(40),
    street            VARCHAR2(40),
    house_number      NVARCHAR2(10),
    county            VARCHAR2(40),
    zip_code          VARCHAR2(13),
    monday_opening    VARCHAR2(20),
    monday_closing    VARCHAR2(20),
    tuesday_opening   VARCHAR2(20),
    tuesday_closing   VARCHAR2(20),
    wednesday_opening VARCHAR2(20),
    wednesday_closing VARCHAR2(20),
    thursday_opening  VARCHAR2(20),
    thursday_closing  VARCHAR2(20),
    friday_opening    VARCHAR2(20),
    friday_closing    VARCHAR2(20),
    saturday_opening  VARCHAR2(20),
    saturday_closing  VARCHAR2(20),
    sunday_opening    VARCHAR2(20),
    sunday_closing    VARCHAR2(20)
)
LOGGING;

ALTER TABLE gym ADD CONSTRAINT gym_pk PRIMARY KEY ( gym_id );

CREATE TABLE gym_classe (
    gym_classe_id INTEGER NOT NULL,
    name          VARCHAR2(30),
    price         INTEGER NOT NULL,
    duration      INTEGER NOT NULL,
    max_people    INTEGER,
    description   CLOB
)
LOGGING;

ALTER TABLE gym_classe ADD CONSTRAINT gym_classe_pk PRIMARY KEY ( gym_classe_id );

CREATE TABLE gym_equipment (
    gym_equipment_id INTEGER NOT NULL,
    gym_id           INTEGER NOT NULL,
    equipment_id     INTEGER NOT NULL,
    purchase_date    DATE
)
LOGGING;

ALTER TABLE gym_equipment ADD CONSTRAINT gym_equipment_pk PRIMARY KEY ( gym_equipment_id );

CREATE TABLE gym_ticket_history (
    gym_ticket_history_id INTEGER NOT NULL,
    purchase_date         DATE NOT NULL,
    activation_date       DATE,
    gym_ticket_offer_id   INTEGER NOT NULL,
    discount_id           INTEGER,
    client_id             INTEGER NOT NULL
)
LOGGING;

ALTER TABLE gym_ticket_history ADD CONSTRAINT ticket_history_pk PRIMARY KEY ( gym_ticket_history_id );

CREATE TABLE gym_ticket_offer (
    gym_ticket_offer_id INTEGER NOT NULL,
    name                VARCHAR2(40),
    duration            INTEGER NOT NULL,
    price               INTEGER NOT NULL,
    type                VARCHAR2(20) NOT NULL
    CONSTRAINT type_check CHECK (type IN ('Wej�ciowy', 'Dniowy'))
)
LOGGING;

ALTER TABLE gym_ticket_offer ADD CONSTRAINT gym_ticket_pk PRIMARY KEY ( gym_ticket_offer_id );

CREATE TABLE gym_visit (
    gym_visit_id     INTEGER NOT NULL,
    entry_time       DATE NOT NULL,
    departure_time   DATE,
    gym_gym_id       INTEGER NOT NULL,
    client_user_id   INTEGER NOT NULL,
    locker_locker_id INTEGER
)
LOGGING;

ALTER TABLE gym_visit ADD CONSTRAINT gym_visit_pk PRIMARY KEY ( gym_visit_id );

CREATE TABLE illness (
    illness_id INTEGER NOT NULL,
    name       VARCHAR2(30) NOT NULL
)
LOGGING;

ALTER TABLE illness ADD CONSTRAINT illness_pk PRIMARY KEY ( illness_id );

CREATE TABLE locker (
    locker_id     INTEGER NOT NULL,
    locker_number INTEGER NOT NULL,
    gym_id        INTEGER NOT NULL
)
LOGGING;

ALTER TABLE locker ADD CONSTRAINT locker_pk PRIMARY KEY ( locker_id );

CREATE TABLE muscle_groups (
    muscle_groups_id INTEGER NOT NULL,
    name             VARCHAR2(30) NOT NULL
)
LOGGING;

ALTER TABLE muscle_groups ADD CONSTRAINT muscle_pk PRIMARY KEY ( muscle_groups_id );

CREATE TABLE ordered_schedule (
    ordered_schedule_id INTEGER NOT NULL,
    schedule_date       DATE NOT NULL,
    payment_date        DATE,
    week_schedule_id    INTEGER NOT NULL,
    client_user_id      INTEGER NOT NULL
)
LOGGING;

ALTER TABLE ordered_schedule ADD CONSTRAINT ordered_schedule_pk PRIMARY KEY ( ordered_schedule_id );

CREATE TABLE parameter (
    parameter_id INTEGER NOT NULL,
    name         VARCHAR2(30) NOT NULL,
    units        VARCHAR2(10) NOT NULL
)
LOGGING;

ALTER TABLE parameter ADD CONSTRAINT parameter_pk PRIMARY KEY ( parameter_id );

CREATE TABLE rating (
    rating_id           INTEGER NOT NULL,
    rating              INTEGER NOT NULL,
    rate_comment        CLOB,
    ordered_schedule_id INTEGER NOT NULL
)
LOGGING;

ALTER TABLE rating ADD CONSTRAINT rating_pk PRIMARY KEY ( rating_id );

CREATE TABLE standard_parameter_value (
    standard_parameter_value_id INTEGER NOT NULL,
    value                       INTEGER NOT NULL,
    parameter_id                INTEGER NOT NULL,
    exercise_id                 INTEGER NOT NULL
)
LOGGING;

ALTER TABLE standard_parameter_value ADD CONSTRAINT standard_parameter_value_pk PRIMARY KEY ( standard_parameter_value_id );

CREATE TABLE training_goal (
    training_goal_id INTEGER NOT NULL,
    name             VARCHAR2(40) NOT NULL
)
LOGGING;

ALTER TABLE training_goal ADD CONSTRAINT training_goal_pk PRIMARY KEY ( training_goal_id );

CREATE TABLE week_schedule (
    week_schedule_id INTEGER NOT NULL,
    week_day         VARCHAR2(30) NOT NULL,
    start_time       VARCHAR2(20) NOT NULL,
    gym_classe_id    INTEGER NOT NULL,
    trainer_id       INTEGER NOT NULL
)
LOGGING;

ALTER TABLE week_schedule ADD CONSTRAINT schedule_pk PRIMARY KEY ( week_schedule_id );

ALTER TABLE client_data_history
    ADD CONSTRAINT client_data_history_client_fk FOREIGN KEY ( client_user_id )
        REFERENCES client ( client_id );

ALTER TABLE client
    ADD CONSTRAINT client_gym_fk FOREIGN KEY ( gym_id )
        REFERENCES gym ( gym_id );

ALTER TABLE client_illness
    ADD CONSTRAINT client_illness_client_fk FOREIGN KEY ( client_id )
        REFERENCES client ( client_id );

ALTER TABLE client_illness
    ADD CONSTRAINT client_illness_illness_fk FOREIGN KEY ( illness_id )
        REFERENCES illness ( illness_id );

ALTER TABLE client
    ADD CONSTRAINT client_training_goal_fk FOREIGN KEY ( training_goal_id )
        REFERENCES training_goal ( training_goal_id );

ALTER TABLE discount
    ADD CONSTRAINT discount_gym_ticket_offer_fk FOREIGN KEY ( gym_ticket_offer_id )
        REFERENCES gym_ticket_offer ( gym_ticket_offer_id );

ALTER TABLE exercise_history_param_value
    ADD CONSTRAINT ehpv_exercise_history_fk FOREIGN KEY ( exercise_history_id )
        REFERENCES exercise_history ( exercise_history_id );

ALTER TABLE exercise_history_param_value
    ADD CONSTRAINT ehpv_parameter_fk FOREIGN KEY ( parameter_id )
        REFERENCES parameter ( parameter_id );

ALTER TABLE exercise_muscle
    ADD CONSTRAINT em_exercise_fk FOREIGN KEY ( exercise_id )
        REFERENCES exercise ( exercise_id );

ALTER TABLE exercise_muscle
    ADD CONSTRAINT em_muscle_groups_fk FOREIGN KEY ( muscle_groups_id )
        REFERENCES muscle_groups ( muscle_groups_id );

ALTER TABLE employee
    ADD CONSTRAINT employee_gym_fk FOREIGN KEY ( gym_id )
        REFERENCES gym ( gym_id );

ALTER TABLE employee
    ADD CONSTRAINT employee_locker_fk FOREIGN KEY ( locker_id )
        REFERENCES locker ( locker_id );

ALTER TABLE exercise_plan_position
    ADD CONSTRAINT epp_exercise_fk FOREIGN KEY ( exercise_id )
        REFERENCES exercise ( exercise_id );

ALTER TABLE exercise_plan_position
    ADD CONSTRAINT epp_exercise_plan_fk FOREIGN KEY ( exercise_plan_id )
        REFERENCES exercise_plan ( exercise_plan_id );

ALTER TABLE exercise_position_value
    ADD CONSTRAINT epv_exercise_plan_position_fk FOREIGN KEY ( exercise_plan_position_id )
        REFERENCES exercise_plan_position ( exercise_plan_position_id );

ALTER TABLE exercise_position_value
    ADD CONSTRAINT epv_parameter_fk FOREIGN KEY ( parameter_id )
        REFERENCES parameter ( parameter_id );

ALTER TABLE exercise
    ADD CONSTRAINT exercise_equipment_fk FOREIGN KEY ( equipment_id )
        REFERENCES equipment ( equipment_id );

ALTER TABLE exercise_history
    ADD CONSTRAINT exercise_history_client_fk FOREIGN KEY ( client_id )
        REFERENCES client ( client_id );

ALTER TABLE exercise_history
    ADD CONSTRAINT exercise_history_exercise_fk FOREIGN KEY ( exercise_id )
        REFERENCES exercise ( exercise_id );

ALTER TABLE exercise_history
    ADD CONSTRAINT exercise_history_gym_fk FOREIGN KEY ( gym_id )
        REFERENCES gym ( gym_id );

ALTER TABLE exercise_history
    ADD CONSTRAINT exercise_history_trainer_fk FOREIGN KEY ( trainer_id )
        REFERENCES employee ( employee_id );

ALTER TABLE exercise_illness
    ADD CONSTRAINT exercise_illness_exercise_fk FOREIGN KEY ( exercise_exercise_id )
        REFERENCES exercise ( exercise_id );

ALTER TABLE exercise_illness
    ADD CONSTRAINT exercise_illness_illness_fk FOREIGN KEY ( illness_illness_id )
        REFERENCES illness ( illness_id );

ALTER TABLE exercise_plan
    ADD CONSTRAINT exercise_plan_client_fk FOREIGN KEY ( client_id )
        REFERENCES client ( client_id );

ALTER TABLE exercise_plan
    ADD CONSTRAINT exercise_plan_trainer_fk FOREIGN KEY ( trainer_id )
        REFERENCES employee ( employee_id );

ALTER TABLE favourite_exercises
    ADD CONSTRAINT fe_client_fk FOREIGN KEY ( client_id )
        REFERENCES client ( client_id );

ALTER TABLE favourite_exercises
    ADD CONSTRAINT fe_exercise_fk FOREIGN KEY ( exercise_id )
        REFERENCES exercise ( exercise_id );

ALTER TABLE gym_ticket_history
    ADD CONSTRAINT gth_gym_ticket_offer_fk FOREIGN KEY ( gym_ticket_offer_id )
        REFERENCES gym_ticket_offer ( gym_ticket_offer_id );

ALTER TABLE gym_equipment
    ADD CONSTRAINT gym_equipment_equipment_fk FOREIGN KEY ( equipment_id )
        REFERENCES equipment ( equipment_id );

ALTER TABLE gym_equipment
    ADD CONSTRAINT gym_equipment_gym_fk FOREIGN KEY ( gym_id )
        REFERENCES gym ( gym_id );

ALTER TABLE gym_ticket_history
    ADD CONSTRAINT gym_ticket_history_client_fk FOREIGN KEY ( client_id )
        REFERENCES client ( client_id );

ALTER TABLE gym_ticket_history
    ADD CONSTRAINT gym_ticket_history_discount_fk FOREIGN KEY ( discount_id )
        REFERENCES discount ( discount_id );

ALTER TABLE gym_visit
    ADD CONSTRAINT gym_visit_client_fk FOREIGN KEY ( client_user_id )
        REFERENCES client ( client_id );

ALTER TABLE gym_visit
    ADD CONSTRAINT gym_visit_gym_fk FOREIGN KEY ( gym_gym_id )
        REFERENCES gym ( gym_id );

ALTER TABLE gym_visit
    ADD CONSTRAINT gym_visit_locker_fk FOREIGN KEY ( locker_locker_id )
        REFERENCES locker ( locker_id );

ALTER TABLE locker
    ADD CONSTRAINT locker_gym_fk FOREIGN KEY ( gym_id )
        REFERENCES gym ( gym_id );

ALTER TABLE ordered_schedule
    ADD CONSTRAINT ordered_schedule_client_fk FOREIGN KEY ( client_user_id )
        REFERENCES client ( client_id );

ALTER TABLE ordered_schedule
    ADD CONSTRAINT os_week_schedule_fk FOREIGN KEY ( week_schedule_id )
        REFERENCES week_schedule ( week_schedule_id );

ALTER TABLE rating
    ADD CONSTRAINT rating_ordered_schedule_fk FOREIGN KEY ( ordered_schedule_id )
        REFERENCES ordered_schedule ( ordered_schedule_id );

ALTER TABLE standard_parameter_value
    ADD CONSTRAINT spv_exercise_fk FOREIGN KEY ( exercise_id )
        REFERENCES exercise ( exercise_id );

ALTER TABLE standard_parameter_value
    ADD CONSTRAINT spv_parameter_fk FOREIGN KEY ( parameter_id )
        REFERENCES parameter ( parameter_id );

ALTER TABLE week_schedule
    ADD CONSTRAINT week_schedule_gym_classe_fk FOREIGN KEY ( gym_classe_id )
        REFERENCES gym_classe ( gym_classe_id );

ALTER TABLE week_schedule
    ADD CONSTRAINT week_schedule_trainer_fk FOREIGN KEY ( trainer_id )
        REFERENCES employee ( employee_id );

ALTER TABLE exercise_plan
    ADD CONSTRAINT ordered_schedule_fk FOREIGN KEY (ordered_id)
        REFERENCES ordered_schedule(ordered_schedule_id);



-- Oracle SQL Developer Data Modeler Summary Report:
--
-- CREATE TABLE                            30
-- CREATE INDEX                             1
-- ALTER TABLE                             73
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
--
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
--
-- ERRORS                                   0
-- WARNINGS                                 0
