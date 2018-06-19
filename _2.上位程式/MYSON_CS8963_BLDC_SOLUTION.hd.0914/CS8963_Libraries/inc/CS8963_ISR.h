#ifndef __CS8963_ISR_H__
#define __CS8963_ISR_H__

void parse_euart2_command();
void check_hall_sequence();
void clear_rpm_data();
void show_rpm_time_data(UINT round);
void do_power_warning(void);
#endif
