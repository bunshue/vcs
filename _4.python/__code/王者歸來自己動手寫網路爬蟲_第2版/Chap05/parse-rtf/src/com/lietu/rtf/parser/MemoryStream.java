package com.lietu.rtf.parser;

public class MemoryStream {
	boolean canWrite;
	boolean allowGetBuffer;
	int capacity;
	int length;
	byte [] internalBuffer;
	int initialIndex;
	boolean expandable;
	boolean streamClosed;
	int position;

	public MemoryStream ()
	{
	}

	public MemoryStream (int capacity)
	{		
		canWrite = true;

		this.capacity = capacity;
		internalBuffer = new byte [capacity];

		expandable = true;
		allowGetBuffer = true;
	}

	public MemoryStream (byte [] buffer) throws Exception
	{
		if (buffer == null)
			throw new Exception ("buffer");
		
		InternalConstructor (buffer, 0, buffer.length, true, false);                        
	}

	public MemoryStream (byte [] buffer, boolean writeable) throws Exception
	{
		if (buffer == null)
			throw new Exception ("buffer");
		
		InternalConstructor (buffer, 0, buffer.length, writeable, false);
	}

	public MemoryStream (byte [] buffer, int index, int count) throws Exception
	{
		InternalConstructor (buffer, index, count, true, false);
	}

	public MemoryStream (byte [] buffer, int index, int count, boolean writeable) throws Exception
	{
		InternalConstructor (buffer, index, count, writeable, false);
	}

	public MemoryStream (byte [] buffer, int index, int count, boolean writeable, boolean publicallyVisible) throws Exception
	{
		InternalConstructor (buffer, index, count, writeable, publicallyVisible);
	}

	void InternalConstructor (byte [] buffer, int index, int count, boolean writeable, boolean publicallyVisible) throws Exception
	{
		if (buffer == null)
			throw new Exception ("buffer");

		if (index < 0 || count < 0)
			throw new Exception ("index or count is less than 0.");

		if (buffer.length - index < count)
			throw new Exception ("The size of the buffer is less than index + count.");

		canWrite = writeable;

		internalBuffer = buffer;
		capacity = count + index;
		length = capacity;
		position = index;
		initialIndex = index;

		allowGetBuffer = publicallyVisible;
		expandable = false;                
	}

	void CheckIfClosedThrowIO () throws Exception
	{
		if (streamClosed)
			throw new Exception ("MemoryStream is closed");
	}
	
	public boolean CanRead() {
		return !streamClosed;
	}

	public boolean CanSeek() {
		return !streamClosed;
	}

	public boolean CanWrite() {
		return (!streamClosed && canWrite);
	}

	public int getCapacity() throws Exception {
			return capacity - initialIndex;
	}

	public void	setCapacity(int value) {
			if (value == capacity)
				return; // LAMENESS: see MemoryStreamTest.ConstructorFive

			//if (!expandable)
			//	throw new Exception ("Cannot expand this MemoryStream");

			//if (value < 0 || value < length)
			//	throw new Exception ("New capacity cannot be negative or less than the current capacity " + value + " " + capacity);

			byte [] newBuffer = null;
			if (value != 0) {
				newBuffer = new byte [value];
				System.arraycopy(internalBuffer, 0, newBuffer, 0, length);
			}

			internalBuffer = newBuffer; // It's null when capacity is set to 0
			capacity = value;
		}

	public int Length(){
		
			// LAMESPEC: The spec says to throw an IOException if the
			// stream is closed and an ObjectDisposedException if
			// "methods were called after the stream was closed".  What
			// is the difference?

			// This is ok for MemoryStreamTest.ConstructorFive
			return length - initialIndex;
	}

	public long getPosition() throws Exception
	{
		return position - initialIndex;
	}

	public void	setPosition(long value) throws Exception
	{
			if (value < 0)
				throw new Exception ("Position cannot be negative" );

			//if (value > Int32.MaxValue)
			//	throw new Exception ("value",
			//	"Position must be non-negative and less than 2^31 - 1 - origin");

			position = initialIndex + (int) value;
	}

	public void Close ()
	{
		streamClosed = true;
		expandable = false;
	}

	public void Flush ()
	{
		// Do nothing
	}

	public byte [] GetBuffer () throws Exception
	{
		if (!allowGetBuffer)
			throw new Exception ();

		return internalBuffer;
	}

	public int Read (byte [] buffer, int offset, int count) throws Exception
	{		
		if (buffer == null)
			throw new Exception ("buffer");

		if (offset < 0 || count < 0)
			throw new Exception ("offset or count less than zero.");

		if (buffer.length - offset < count )
			throw new Exception ("The size of the buffer is less than offset + count.");

		if (position >= length || count == 0)
			return 0;

		if (position > length - count)
			count = length - position;

		System.arraycopy (internalBuffer, position, buffer, offset, count);
		position += count;
		return count;
	}

	public int ReadByte () throws Exception
	{
		if (position >= length)
			return -1;

		return internalBuffer [position++];
	}

	/*public override long Seek (long offset, SeekOrigin loc)
	{
		CheckIfClosedThrowDisposed ();

		// It's funny that they don't throw this exception for < Int32.MinValue
		if (offset > (long) Int32.MaxValue)
			throw new ArgumentOutOfRangeException ("Offset out of range. " + offset);

		int refPoint;
		switch (loc) {
		case SeekOrigin.Begin:
			if (offset < 0)
				throw new IOException ("Attempted to seek before start of MemoryStream.");
			refPoint = initialIndex;
			break;
		case SeekOrigin.Current:
			refPoint = position;
			break;
		case SeekOrigin.End:
			refPoint = length;
			break;
		default:
			throw new ArgumentException ("loc", "Invalid SeekOrigin");
		}

		// LAMESPEC: My goodness, how may LAMESPECs are there in this
		// class! :)  In the spec for the Position property it's stated
		// "The position must not be more than one byte beyond the end of the stream."
		// In the spec for seek it says "Seeking to any location beyond the length of the 
		// stream is supported."  That's a contradiction i'd say.
		// I guess seek can go anywhere but if you use position it may get moved back.

		refPoint += (int) offset;
		if (refPoint < initialIndex)
			throw new IOException ("Attempted to seek before start of MemoryStream.");

		position = refPoint;
		return position;
	}*/

	int CalculateNewCapacity (int minimum)
	{
		if (minimum < 256)
			minimum = 256; // See GetBufferTwo test

		if (minimum < capacity * 2)
			minimum = capacity * 2;

		return minimum;
	}

	public void SetLength (long value)
	{
		//if (!expandable && value > capacity)
		//	throw new Exception ("Expanding this MemoryStream is not supported");

		//CheckIfClosedThrowDisposed ();

		// LAMESPEC: AGAIN! It says to throw this exception if value is
		// greater than "the maximum length of the MemoryStream".  I haven't
		// seen anywhere mention what the maximum length of a MemoryStream is and
		// since we're this far this memory stream is expandable.
		//if (value < 0 )
		//	throw new Exception ();

		int newSize = (int) value + initialIndex;
		if (newSize > capacity)
			setCapacity(CalculateNewCapacity (newSize));
		else if (newSize < length)
			// zeroize present data (so we don't get it 
			// back if we expand the stream using Seek)
		{
			
			//Array.Clear (internalBuffer, newSize, length - newSize);
			for(int i=newSize;i<length;++i)
			{
				internalBuffer[i] = 0;
			}
		}

		length = newSize;
		if (position > length)
			position = length;
	}

	public byte [] ToArray ()
	{
		int l = length - initialIndex;
		byte[] outBuffer = new byte [l];

		if (internalBuffer != null)
			System.arraycopy (internalBuffer, initialIndex, outBuffer, 0, l);
		return outBuffer; 
	}

	public void Write (byte [] buffer, int offset, int count) throws Exception
	{
		
		if (!canWrite)
			throw new Exception ("Cannot write to this stream.");

		if (buffer == null)
			throw new Exception ("buffer");
		
		if (offset < 0 || count < 0)
			throw new Exception ();

		if (buffer.length - offset < count)
			throw new Exception ("The size of the buffer is less than offset + count.");

		// reordered to avoid possible integer overflow
		if (position > capacity - count)
			setCapacity(CalculateNewCapacity (position + count));

		System.arraycopy (buffer, offset, internalBuffer, position, count);
		position += count;
		if (position >= length)
			length = position;
	}

	public void WriteByte (byte value) throws Exception
	{
		if (!canWrite)
			throw new Exception ("Cannot write to this stream.");

		if (position >= capacity)
			setCapacity(CalculateNewCapacity (position + 1));

		if (position >= length)
			length = position + 1;

		internalBuffer [position++] = value;
	}
}
