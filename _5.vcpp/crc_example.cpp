#include <cassert>
#include <iostream>
#include <string>

class Crc
{
public:
	typedef unsigned long Type;

	Crc (Type key)
		: _key (key), _register (0)
	{}
	Type Done ()
	{
		Type tmp = _register;
		_register = 0;
		return tmp;
	}
protected:
	Type _key;	// really 33-bit key, counting implicit 1 top-bit
	Type _register;
};

class SlowCrc: public Crc
{
public:
	SlowCrc (Crc::Type key)
		: Crc (key)
	{}
	void PutByte (unsigned char byte);
private:
	void PutBit (bool bit);
};

void SlowCrc::PutByte (unsigned char byte)
{
	unsigned char mask = 0x80; // leftmost bit
	for (int j = 0; j < 8; ++j)
	{
		PutBit ((byte & mask) != 0);
		mask >>= 1;
	}
}

void SlowCrc::PutBit (bool bit)
{
	bool topBit = (_register & 0x80000000) != 0;
	// shift bit into register from the right
	_register <<= 1;
	_register ^= (bit? 0x1: 0x0); // OR or XOR, same result
	if (topBit)
	{
		// XOR the 32-bits of the key.
		// The implicit high bit of the 33-bit key
		// conceptually clears the topBit shifted out of the register
		_register ^= _key;
	}
}

class FastCrc: public Crc
{
public:
	FastCrc (Crc::Type key) 
		: Crc (key) 
	{
		_table.Init (key);
	}
	void PutByte (unsigned byte);
private:
	class Table
	{
	public:
		Table () : _key (0) {}
		void Init (Crc::Type key);
		Crc::Type operator [] (unsigned i)
		{
			return _table [i];
		}
	private:
		Crc::Type _table [256];
		Crc::Type _key;
	};
private:
	static Table _table;
};

// define static member

FastCrc::Table FastCrc::_table;

void FastCrc::Table::Init (Crc::Type key)
{
	assert (key != 0);
	if (key == _key)
		return;
	_key = key;

	// for all possible byte values
	for (unsigned i = 0; i < 256; ++i)
	{
		Crc::Type reg = i << 24;
		// for all bits in a byte
		for (int j = 0; j < 8; ++j)
		{
			bool topBit = (reg & 0x80000000) != 0;
			reg <<= 1;
			if (topBit)
				reg ^= _key;
		}
		_table [i] = reg;
	}
}

void FastCrc::PutByte (unsigned byte)
{
	unsigned top = _register >> 24;
	top ^= byte;
	_register = (_register << 8) ^ _table [top];
}

int main ()
{
	std::string msg ("Harry had a little lamp");
	std::string exMsg (msg);
	exMsg.resize (msg.length () + 4);
	
	Crc::Type const ethernetKey = 0x04c11db7;
	SlowCrc slowCrc (ethernetKey);

	for (size_t i = 0; i < exMsg.length (); ++i)
	{
		slowCrc.PutByte (exMsg [i]);
	}
	Crc::Type crc = slowCrc.Done ();
	std::cout << "\n0x" << std::hex << crc << std::endl;

	FastCrc fastCrc (ethernetKey);

	for (i = 0; i < msg.length (); ++i)
	{
		fastCrc.PutByte (msg [i]);
	}
	Crc::Type newCrc = fastCrc.Done ();
	std::cout << "\n0x" << std::hex << newCrc << std::endl;

	return 0;
}
