# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    login = models.CharField(unique=True, max_length=25, blank=True, null=True)
    password_hash = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    gender = models.CharField(max_length=1)
    height = models.BigIntegerField(blank=True, null=True)
    birth_year = models.DateField()
    advancement = models.CharField(max_length=40, null=True)
    target_weight = models.BigIntegerField(blank=True, null=True)
    training_frequency = models.BigIntegerField(blank=True, null=True)
    training_time = models.BigIntegerField(blank=True, null=True)
    training_goal = models.ForeignKey('TrainingGoal', models.DO_NOTHING, blank=True, null=True)
    gym = models.ForeignKey('Gym', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'client'


class ClientDataHistory(models.Model):
    client_data_history_id = models.AutoField(primary_key=True)
    weight = models.BigIntegerField()
    fat_body_level = models.BigIntegerField(blank=True, null=True)
    measurement_date = models.DateField()
    client = models.ForeignKey(Client, models.DO_NOTHING)

    class Meta:
        db_table = 'client_data_history'


class ClientIllness(models.Model):
    illness = models.OneToOneField('Illness', models.DO_NOTHING, primary_key=True)  # The composite primary key (illness_id, client_id) found, that is not supported. The first column is selected.
    client = models.ForeignKey(Client, models.DO_NOTHING)

    class Meta:
        db_table = 'client_illness'
        unique_together = (('illness', 'client'),)


class Discount(models.Model):
    discount_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    start_date = models.DateField()
    stop_date = models.DateField(blank=True, null=True)
    discount_percentages = models.BigIntegerField()
    gym_ticket_offer = models.OneToOneField('GymTicketOffer', models.DO_NOTHING)

    class Meta:
        db_table = 'discount'


class Employee(models.Model):
    employee_id = models.BigIntegerField(primary_key=True)
    login = models.CharField(unique=True, max_length=25)
    password_hash = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=13)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    gender = models.CharField(max_length=1)
    type = models.CharField(max_length=10)
    standar_salary = models.BigIntegerField(blank=True, null=True)
    gym = models.ForeignKey('Gym', models.DO_NOTHING)
    locker_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'employee'


class Equipment(models.Model):
    equipment_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'equipment'


class Exercise(models.Model):
    exercise_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    calories = models.BigIntegerField()
    duration = models.BigIntegerField()
    advancement_level = models.CharField(max_length=40)
    repetitions_number = models.BigIntegerField()
    description = models.TextField()
    equipment = models.ForeignKey(Equipment, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'exercise'


class ExerciseHistory(models.Model):
    exercise_history_id = models.AutoField(primary_key=True)
    exercise_date = models.DateTimeField()
    duration = models.BigIntegerField(blank=True, null=True)
    repetitions_number = models.BigIntegerField()
    exercise_comment = models.TextField(blank=True, null=True)
    gym = models.ForeignKey('Gym', models.DO_NOTHING)
    exercise = models.ForeignKey(Exercise, models.DO_NOTHING)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    calories = models.BigIntegerField()
    gym_equipment = models.ForeignKey('GymEquipment', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'exercise_history'


class ExerciseHistoryParamValue(models.Model):
    param_value_id = models.AutoField(primary_key=True)
    value = models.BigIntegerField()
    parameter = models.ForeignKey('Parameter', models.DO_NOTHING)
    exercise_history = models.ForeignKey(ExerciseHistory, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'exercise_history_param_value'


class ExerciseIllness(models.Model):
    exercise_exercise = models.OneToOneField(Exercise, models.DO_NOTHING, primary_key=True)  # The composite primary key (exercise_exercise_id, illness_illness_id) found, that is not supported. The first column is selected.
    illness_illness = models.ForeignKey('Illness', models.DO_NOTHING)

    class Meta:
        db_table = 'exercise_illness'
        unique_together = (('exercise_exercise', 'illness_illness'),)


class ExercisePlan(models.Model):
    exercise_plan_id = models.BigIntegerField(primary_key=True)
    ordered = models.ForeignKey('OrderedSchedule', models.DO_NOTHING)
    done = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'exercise_plan'


class ExercisePlanPosition(models.Model):
    exercise_plan_position_id = models.AutoField(primary_key=True)
    position = models.BigIntegerField()
    duration = models.BigIntegerField(blank=True, null=True)
    repetitions_number = models.BigIntegerField(blank=True, null=True)
    plan_comment = models.TextField(blank=True, null=True)
    exercise = models.ForeignKey(Exercise, models.DO_NOTHING)
    exercise_plan = models.ForeignKey(ExercisePlan, models.DO_NOTHING)

    class Meta:
        db_table = 'exercise_plan_position'


class ExercisePositionValue(models.Model):
    exercise_position_value_id = models.BigIntegerField(primary_key=True)
    value = models.BigIntegerField()
    parameter = models.ForeignKey('Parameter', models.DO_NOTHING)
    exercise_plan_position = models.ForeignKey(ExercisePlanPosition, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'exercise_position_value'


class FavouriteExercises(models.Model):
    exercise = models.OneToOneField(Exercise, models.DO_NOTHING, primary_key=True)  # The composite primary key (exercise_id, client_id) found, that is not supported. The first column is selected.
    client = models.ForeignKey(Client, models.DO_NOTHING)

    class Meta:
        db_table = 'favourite_exercises'
        unique_together = (('exercise', 'client'),)


class Gym(models.Model):
    gym_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    street = models.CharField(max_length=40, blank=True, null=True)
    house_number = models.CharField(max_length=10, blank=True, null=True)
    county = models.CharField(max_length=40, blank=True, null=True)
    zip_code = models.CharField(max_length=13, blank=True, null=True)
    monday_opening = models.CharField(max_length=20, blank=True, null=True)
    monday_closing = models.CharField(max_length=20, blank=True, null=True)
    tuesday_opening = models.CharField(max_length=20, blank=True, null=True)
    tuesday_closing = models.CharField(max_length=20, blank=True, null=True)
    wednesday_opening = models.CharField(max_length=20, blank=True, null=True)
    wednesday_closing = models.CharField(max_length=20, blank=True, null=True)
    thursday_opening = models.CharField(max_length=20, blank=True, null=True)
    thursday_closing = models.CharField(max_length=20, blank=True, null=True)
    friday_opening = models.CharField(max_length=20, blank=True, null=True)
    friday_closing = models.CharField(max_length=20, blank=True, null=True)
    saturday_opening = models.CharField(max_length=20, blank=True, null=True)
    saturday_closing = models.CharField(max_length=20, blank=True, null=True)
    sunday_opening = models.CharField(max_length=20, blank=True, null=True)
    sunday_closing = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'gym'


class GymClasse(models.Model):
    gym_classe_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    price = models.BigIntegerField()
    duration = models.BigIntegerField()
    max_people = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'gym_classe'


class GymEquipment(models.Model):
    gym_equipment_id = models.BigIntegerField(primary_key=True)
    gym = models.ForeignKey(Gym, models.DO_NOTHING)
    equipment = models.ForeignKey(Equipment, models.DO_NOTHING)
    purchase_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'gym_equipment'


class GymTicketHistory(models.Model):
    gym_ticket_history_id = models.BigIntegerField(primary_key=True)
    purchase_date = models.DateField()
    activation_date = models.DateField(blank=True, null=True)
    gym_ticket_offer = models.ForeignKey('GymTicketOffer', models.DO_NOTHING)
    discount = models.ForeignKey(Discount, models.DO_NOTHING, blank=True, null=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)

    class Meta:
        db_table = 'gym_ticket_history'


class GymTicketOffer(models.Model):
    gym_ticket_offer_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    duration = models.BigIntegerField()
    price = models.BigIntegerField()
    type = models.CharField(max_length=20)

    class Meta:
        db_table = 'gym_ticket_offer'


class GymVisit(models.Model):
    gym_visit_id = models.AutoField(primary_key=True)
    entry_time = models.DateTimeField()
    departure_time = models.DateTimeField(blank=True, null=True)
    gym_gym = models.ForeignKey(Gym, models.DO_NOTHING)
    client_user = models.ForeignKey(Client, models.DO_NOTHING)
    locker_locker = models.ForeignKey('Locker', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'gym_visit'


class Illness(models.Model):
    illness_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'illness'


class Locker(models.Model):
    locker_id = models.BigIntegerField(primary_key=True)
    locker_number = models.BigIntegerField()
    gym = models.ForeignKey(Gym, models.DO_NOTHING)

    class Meta:
        db_table = 'locker'


class MuscleGroups(models.Model):
    muscle_groups_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'muscle_groups'


class OrderedSchedule(models.Model):
    ordered_schedule_id = models.BigIntegerField(primary_key=True)
    schedule_date = models.DateTimeField()
    payment_date = models.DateTimeField(blank=True, null=True)
    week_schedule = models.ForeignKey('WeekSchedule', models.DO_NOTHING)
    client_user = models.ForeignKey(Client, models.DO_NOTHING)

    class Meta:
        db_table = 'ordered_schedule'


class Parameter(models.Model):
    parameter_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    units = models.CharField(max_length=10)

    class Meta:
        db_table = 'parameter'


class Rating(models.Model):
    rating_id = models.BigIntegerField(primary_key=True)
    rating = models.BigIntegerField()
    rate_comment = models.TextField(blank=True, null=True)
    ordered_schedule = models.ForeignKey(OrderedSchedule, models.DO_NOTHING)

    class Meta:
        db_table = 'rating'


class StandardParameterValue(models.Model):
    standard_parameter_value_id = models.BigIntegerField(primary_key=True)
    value = models.BigIntegerField()
    parameter = models.ForeignKey(Parameter, models.DO_NOTHING)
    exercise = models.ForeignKey(Exercise, models.DO_NOTHING)

    class Meta:
        db_table = 'standard_parameter_value'


class TrainingGoal(models.Model):
    training_goal_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'training_goal'


class WeekSchedule(models.Model):
    week_schedule_id = models.BigIntegerField(primary_key=True)
    week_day = models.CharField(max_length=30)
    start_time = models.CharField(max_length=20)
    gym_classe = models.ForeignKey(GymClasse, models.DO_NOTHING)
    trainer = models.ForeignKey(Employee, models.DO_NOTHING)

    class Meta:
        db_table = 'week_schedule'
