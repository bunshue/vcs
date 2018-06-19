#ifndef __CS8963_MOTOR_FUNCTION_H__
#define __CS8963_MOTOR_FUNCTION_H__

char MtState_changed();
void Start_Motor();
void Stop_Motor();
void MT_drive(unsigned char Hal_sta_tmp);
void Limit_MinMaxSpeed(void);
void do_over_current_protection_adc(void);
void MT_Brake(void);
void MT_Lock(bit on_off);
void MT_drive_A_on();
void MT_drive_A_off();
void MT_drive_B_on();
void MT_drive_B_off();
void MT_drive_C_on();
void MT_drive_C_off();
void MT_drive_ABC_off();
void get_current_hall_state();
BYTE get_current_hall_status();
void do_check_VR_open_loop();
void do_check_VR_close_loop();
void do_check_VR_open_loop_test();
void do_check_VR_close_loop_test();
void do_check_lock_rotor_protection();
UINT check_vdc_voltage();
void do_check_vdc_voltage();
void get_vdc_voltage();
void do_VDC_protection();
void pirnt_mt_drive_value(void);
void reset_mt_drive_value(void);
void precharge_lower_arms();
void do_check_speed();
void do_check_test_start();
void record_open_loop_rpm_data();
void do_check_key();
void calculate_real_speed();
#endif
