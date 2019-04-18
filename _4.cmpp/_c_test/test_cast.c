#include <stdio.h>

typedef struct {
  union {
    struct ATTR_PACKED {
      uint16_t connect_status             : 1;
      uint16_t port_enable                : 1;
      uint16_t suspend                    : 1;
      uint16_t over_current               : 1;
      uint16_t reset                      : 1;

      uint16_t                            : 3;
      uint16_t port_power                 : 1;
      uint16_t low_speed_device_attached  : 1;
      uint16_t high_speed_device_attached : 1;
      uint16_t port_test_mode             : 1;
      uint16_t port_indicator_control     : 1;
      uint16_t : 0;
    };

    uint16_t value;
  } status_current, status_change;
} hub_port_status_response_t;

struct usbcmd
{
	uint8_t bmRequest;
	uint8_t bRequest;
	uint16_t wValue;
	uint16_t wIndex;
	uint16_t wLength;
};

int main(int argc,char* argv[])
{
        unsigned char enum_data_buffer[4];

	enum_data_buffer[0] = 0x01;
	enum_data_buffer[1] = 0x10;
	enum_data_buffer[2] = 0x00;
	enum_data_buffer[3] = 0x00;

	hub_port_status_response_t * p_port_status;
	p_port_status = ((hub_port_status_response_t *) enum_data_buffer);

	printf("status_change\n");
	printf("connect_status = %d\n\r", p_port_status->status_change.connect_status);
	printf("port_enable = %d\n\r", p_port_status->status_change.port_enable);
	printf("suspend = %d\n\r", p_port_status->status_change.suspend);
	printf("over_current = %d\n\r", p_port_status->status_change.over_current);
	printf("reset = %d\n\r", p_port_status->status_change.reset);
	printf("port_power = %d\n\r", p_port_status->status_change.port_power);
	printf("low_speed_device_attached = %d\n\r", p_port_status->status_change.low_speed_device_attached);
	printf("high_speed_device_attached = %d\n\r", p_port_status->status_change.high_speed_device_attached);
	printf("port_test_mode = %d\n\r", p_port_status->status_change.port_test_mode);
	printf("port_indicator_control = %d\n\r", p_port_status->status_change.port_indicator_control);

	printf("\nstatus_current\n");
	printf("connect_status = %d\n\r", p_port_status->status_current.connect_status);
	printf("port_enable = %d\n\r", p_port_status->status_current.port_enable);
	printf("suspend = %d\n\r", p_port_status->status_current.suspend);
	printf("over_current = %d\n\r", p_port_status->status_current.over_current);
	printf("reset = %d\n\r", p_port_status->status_current.reset);
	printf("port_power = %d\n\r", p_port_status->status_current.port_power);
	printf("low_speed_device_attached = %d\n\r", p_port_status->status_current.low_speed_device_attached);
	printf("high_speed_device_attached = %d\n\r", p_port_status->status_current.high_speed_device_attached);
	printf("port_test_mode = %d\n\r", p_port_status->status_current.port_test_mode);
	printf("port_indicator_control = %d\n\r", p_port_status->status_current.port_indicator_control);



	printf("size of usbcmd is %ld\n", sizeof(struct usbcmd));

	struct usbcmd * uc;
	uc->bmRequest = 0x80;
	uc->bRequest = 0x06;
	uc->wValue = 0x0100;
	uc->wIndex = 0x1234;
	uc->wLength = 0x4567;

	uint8_t uu[8];
	uu = (uint8_t*)uc;

	int i;

	for(i = 0;i<8;i++)
	{
		printf("0x%2x\t", uu[i]);
	}
	printf("\n");

        return 0;
}

