
--CREATE SEQUENCE  "PZSP05"."EXERCISE_PLAN_ID_SEQ"  MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 49 NOCACHE  NOORDER  NOCYCLE  NOKEEP  NOSCALE  GLOBAL ;

ALTER TABLE EXERCISE_PLAN MODIFY (EXERCISE_PLAN_ID DEFAULT EXERCISE_PLAN_ID_seq.NEXTVAL);

--CREATE SEQUENCE  "PZSP05"."GYM_VSIT_ID_SEQ"  MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 49 NOCACHE  NOORDER  NOCYCLE  NOKEEP  NOSCALE  GLOBAL ;

ALTER TABLE GYM_VISIT MODIFY (GYM_VISIT_ID DEFAULT GYM_VISIT_ID_seq.NEXTVAL);

--CREATE SEQUENCE  "PZSP05"."ORDERED_SCHEDULE_ID_SEQ"  MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 49 NOCACHE  NOORDER  NOCYCLE  NOKEEP  NOSCALE  GLOBAL ;

ALTER TABLE ORDERED_SCHEDULE MODIFY (ORDERED_SCHEDULE_ID DEFAULT ORDERED_SCHEDULE_ID_seq.NEXTVAL);
