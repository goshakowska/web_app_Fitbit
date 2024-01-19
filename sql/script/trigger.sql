create or replace TRIGGER trg_add_to_exercise_plan
AFTER INSERT ON ordered_schedule
FOR EACH ROW
DECLARE
    v_exercise_name VARCHAR2(50);
BEGIN
    -- Pobierz nazwê æwiczenia na podstawie week_schedule_id
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
        DBMS_OUTPUT.PUT_LINE('Nie znaleziono informacji o æwiczeniu.');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Wyst¹pi³ b³¹d: ' || SQLERRM);
END;
/


create or replace TRIGGER trg_delete_ordered_schedule
BEFORE DELETE ON ordered_schedule
FOR EACH ROW
BEGIN

    -- Usuñ powi¹zane wpisy z exercise_plan_position
    DELETE FROM exercise_plan_position WHERE exercise_plan_id IN (
        SELECT exercise_plan_id FROM exercise_plan WHERE ordered_id = :OLD.ordered_schedule_id
    );

    -- Usuñ wiersze z exercise_plan
    DELETE FROM exercise_plan WHERE ordered_id = :OLD.ordered_schedule_id;

END;
/