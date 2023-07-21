import datetime

appointment_list = ["10:30", "11:30", "12:30", "1:30"]
if len(appointment_list) == 0:
    time_slot_per_patient_time = "30 min"
    probable_start_time = "9:30 a.m."
    actual_end_time = probable_start_time + "30" + "10"
else:
    probable_start_time = appointment_list[-1]
    actual_end_time = probable_start_time + "30" + "10"
