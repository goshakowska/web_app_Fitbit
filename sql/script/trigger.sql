CREATE OR REPLACE TRIGGER trg_add_to_exercise_plan
AFTER INSERT ON ordered_schedule
FOR EACH ROW
DECLARE
    v_exercise_name VARCHAR2(50);
BEGIN
    -- Pobierz nazwę ćwiczenia na podstawie week_schedule_id
    SELECT name
    INTO v_exercise_name
    FROM week_schedule w INNER JOIN gym_classe g ON w.gym_classe_id = g.gym_classe_id
    WHERE week_schedule_id = :NEW.week_schedule_id;

    IF v_exercise_name = 'Trening indywidualny' THEN

        -- Dodaj wpis do exercise_plan
        INSERT INTO exercise_plan (ordered_id, done)
        VALUES (:NEW.ordered_schedule_id, 'F');

        COMMIT;
    END IF;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Nie znaleziono informacji o ćwiczeniu.');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Wystąpił błąd: ' || SQLERRM);
END;
/