#ifndef __CS8963_PWM_H__
#define __CS8963_PWM_H__

void Initial_PWM16(unsigned int pwmprd, unsigned char pwmduty);
void Initial_PWM16_Test_Gate_Driver(unsigned int pwmprd, unsigned char pwmdutya, unsigned char pwmdutyb, unsigned char pwmdutyc);
void PWM16_Modify0(unsigned int pwmprd,unsigned char pwmduty);
void PWM16_Modify(unsigned int pwmprd,unsigned char pwmduty);
void PWM16_disable(void);
void do_PWM16_Modify(void);
void check_speed_by_pwm(BYTE type, BYTE amount);
#endif

