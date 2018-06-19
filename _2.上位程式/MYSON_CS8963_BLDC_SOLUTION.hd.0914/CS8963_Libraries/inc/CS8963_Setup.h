#ifndef __CS8963_SETUP_H__
#define __CS8963_SETUP_H__

void Show_SETUP_Info(void);
void SETUP_System(void);
void SETUP_Parameter(void);
void SETUP_HallSensor(void);
void SETUP_PWM(void);
void SETUP_Key(void);
void SETUP_LED(void);
void SETUP_Timer(void);
void SETUP_enable_brake(unsigned char enable_brake);
void SETUP_enable_speed_up_fast(unsigned char enable_speed_up_fast);
void SETUP_enable_speed_down_fast(unsigned char enable_speed_down_fast);
void SETUP_vr_max_speed(unsigned int speed);
void SETUP_vr_min_speed(unsigned int speed);
void SETUP_max_power(unsigned int power);
void SETUP_AC_voltage(unsigned int voltage);
void SETUP_target_speed(unsigned int speed);
void SETUP_PWM_period(unsigned int pwm_period);
void SETUP_PWM_start_duty(unsigned char pwm_start_duty);
void SETUP_PWM_duty(unsigned char pwm_duty);
void SETUP_PWM_duty_target(unsigned char pwm_duty_target);
void SETUP_PWM_duty_new(unsigned char pwm_duty_new);
void SETUP_PWM_dead_time(unsigned char pwm_dead_time);
void SETUP_motor_uvw_sequence(unsigned char uvw_sequence);
void SETUP_direction(unsigned char direction);
void SETUP_slow_modify_speed(unsigned char speed);
void SETUP_mode_type(unsigned char mode_type);
void SETUP_sensor_mode(unsigned char sensor_type);
void SETUP_speed_control_mode(unsigned char speed_control_mode);
void SETUP_debug_mode(unsigned char debug_mode);
void SETUP_phase_compensation_mode(unsigned char phase_compensation_mode);
void SETUP_enable_watchdog(unsigned char enable_watchdog);
void SETUP_enable_over_current_protection(unsigned char over_current_protection);
void SETUP_enable_lock_rotor_protection(unsigned char lock_rotor_protection);
void SETUP_enable_vdc_protection(unsigned char vdc_protection);
void SETUP_enable_hall_protection(unsigned char hall_protection);
void SETUP_motor_pole_pair(unsigned char motor_pole_pair);
void SETUP_rpm_step_size(UINT rpm_step_size);
void SETUP_PWMCNT_diff(ULONG PWM16INT_cnt_start, ULONG PWM16INT_cnt_diff);
void SETUP_PWMCNT_diff2(ULONG PWM16INT_cnt_start, ULONG PWM16INT_cnt_diff);
void SETUP_Over_Current_ADC(UINT adc);
void SETUP_VDC_protection_value(UINT v1, UINT v2, UINT v3, UINT v4);
void SETUP_VDC_protection_adc(UINT adc_1, UINT adc_2, UINT adc_3, UINT adc_4);
#endif

