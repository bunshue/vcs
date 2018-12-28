#include <iostream>

#include <iomanip>	//for setw

using namespace std;

enum dirs {NONE, EAST, SOUTH, WEST, NORTH, RIGHT, BACK, LEFT};

class Robot
{
	private:
		int total_steps;
		int direction;
		int position_x;
		int position_y;
	public:
		Robot();				//constructor
		Robot(int dir);				//constructor overload
		Robot(int pos_x, int pox_y);		//constructor overload
		Robot(int dir, int pos_x, int pox_y);	//constructor overload
		void resetRobot();
		void setDirection(int dir);
		void run(int steps);
		void stop();
		void showRobotInfo();
		static int sum;				//static
		int getRobotSum(){return sum;}		//inline fx
		int getDirection(){return direction;}	//inline fx
		void checkBoundary();
};

class Poli:public Robot
{
	private:
		int poli_power;
	public:
		Poli();
		void setPower(int power);
};

Robot::Robot()
{
	total_steps = 0;
	direction = EAST;
	position_x = 0;
	position_y = 0;
	sum++;
	cout << "\ncreate a robot\n";
}

void Robot::resetRobot()
{
	total_steps = 0;
	direction = EAST;
	position_x = 0;
	position_y = 0;
}

void Robot::setDirection(int dir)
{
	if((dir == RIGHT) || (dir == LEFT) ||(dir == BACK))
	{
		if(dir == NONE)
		{
			cout << "can not set direction when direction unknown\n";
			return;
		}
	}

	if(dir == EAST)
		direction = EAST;
	else if(dir == SOUTH)
		direction = SOUTH;
	else if(dir == WEST)
		direction = WEST;
	else if(dir == NORTH)
		direction = NORTH;
	else if(dir == RIGHT)
		direction = SOUTH;
	else if(dir == NONE)
		direction = NONE;

	if(dir == RIGHT)
		direction = (dir + 1) % 4;
	else if(dir == BACK)
		direction = (dir + 2) % 4;
	else if(dir == LEFT)
		direction = (dir + 3) % 4;
	return;
}

void Robot::run(int steps)
{
	if((direction >= EAST) && (direction <= NORTH))
	{
		switch(direction)
		{
			case EAST:	position_x += steps;total_steps += steps;break;
			case SOUTH:	position_y += steps;total_steps += steps;break;
			case WEST:	position_x -= steps;total_steps += steps;break;
			case NORTH:	position_y -= steps;total_steps += steps;break;
			default:
				cout << "unknown, direction = " << direction << "\n";break;
		}
	}
	else
	{
		cout << "can not run, direction = " << direction << "\n";
	}
	return;
}


void Robot::showRobotInfo()
{
	cout << "total " << sum << " robot(s).\t";
	cout << "direction : ";
	switch(direction)
	{
		case NONE:	cout << "NONE";break;
		case EAST:	cout << "EAST";break;
		case SOUTH:	cout << "SOUTH";break;
		case WEST:	cout << "WEST";break;
		case NORTH:	cout << "NORTH";break;
		default:
				cout << "unknown, direction = " << direction;break;
	}
	cout << "\tposition : (" << position_x << ", " << position_y << ")";
	cout << "\ttotal_steps : " << total_steps << "\n";
}


Poli::Poli()
{
	cout << "create a poli.\n";

}

void Poli::setPower(int power)
{
	poli_power = power;
	return;
}

int Robot::sum = 0;

int main()
{
	Robot rb1;
	rb1.run(2);
	rb1.setDirection(RIGHT);
	rb1.run(5);
	rb1.showRobotInfo();

	Poli po1;
	po1.setDirection(WEST);
	po1.setPower(100);

	int i;
	for(i = 0; i <= 10; i++)
	{
		cout << setw(3) << i;
	}
	cout << "\n";

	int a = 123;
	cout << "a = 0x" << hex << a << "\n";
	cout << "a = " << dec << a << "\n";
	cout << "a = " << a << "\n";

	cout.setf(ios::hex);
	cout << "a = " << a << "\n";
	cout.unsetf(ios::hex);
	cout << "a = " << a << "\n";




	return 0;
}


