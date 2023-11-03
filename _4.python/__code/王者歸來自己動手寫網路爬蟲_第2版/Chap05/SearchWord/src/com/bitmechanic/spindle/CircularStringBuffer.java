/*
 * Created on 2006-5-1
 *
 */
package com.bitmechanic.spindle;

import java.io.IOException;

/**
 * Implements the Circular Buffer producer/consumer model for characters.
 * More information about this class is available from <a target="_top" href=
 * "http://ostermiller.org/utils/CircularCharBuffer.html">ostermiller.org</a>.
 * <p>
 * Using this class is a simpler alternative to using a PipedReader
 * and a PipedWriter. PipedReaders and PipedWriters don't support the
 * mark operation, don't allow you to control buffer sizes that they use,
 * and have a more complicated API that requires instantiating two
 * classes and connecting them.
 * <p>
 *
 * @author Stephen Ostermiller http://ostermiller.org/contact.pl?regarding=Java+Utilities
 * @since ostermillerutils 1.00.00
 */

public class CircularStringBuffer {
    /**
     * The default size for a circular object buffer.
     *
     * @since ostermillerutils 1.00.00
     */
    private final static int DEFAULT_SIZE = 256;

    /**
     * The circular buffer.
     * <p>
     * The actual capacity of the buffer is one less than the actual length
     * of the buffer so that an empty and a full buffer can be
     * distinguished.  An empty buffer will have the readPostion and the
     * writePosition equal to each other.  A full buffer will have
     * the writePosition one less than the readPostion.
     * <p>
     * There are two important indexes into the buffer:
     * The readPosition, and the writePosition. The Objects
     * available to be read go from the readPosition to the writePosition,
     * wrapping around the end of the buffer.  The space available for writing
     * goes from the write position to one less than the readPosition,
     * wrapping around the end of the buffer.
     *
     * @since ostermillerutils 1.00.00
     */
    protected String[] buffer;
    
    /**
     * Index of the first Object available to be read.
     *
     * @since ostermillerutils 1.00.00
     */
    protected volatile int readPosition = 0;
    /**
     * Index of the first Object available to be written.
     *
     * @since ostermillerutils 1.00.00
     */
    protected volatile int writePosition = 0;
    
    /**
     * Make this buffer ready for reuse.  The contents of the buffer
     * will be cleared and the streams associated with this buffer
     * will be reopened if they had been closed.
     *
     * @since ostermillerutils 1.00.00
     */
    public void clear(){
        readPosition = 0;
        writePosition = 0;
    }

    /**
     * Get number of Objects that are available to be read.
     * <p>
     * Note that the number of Objects available plus
     * the number of Objects free may not add up to the
     * capacity of this buffer, as the buffer may reserve some
     * space for other purposes.
     *
     * @return the size in Objects of this buffer
     *
     * @since ostermillerutils 1.00.00
     */
    public int getAvailable(){
        return available();
    }

    /**
     * Get the capacity of this buffer.
     * <p>
     * Note that the number of Objects available plus
     * the number of Objects free may not add up to the
     * capacity of this buffer, as the buffer may reserve some
     * space for other purposes.
     *
     * @return the size in Objects of this buffer
     *
     * @since ostermillerutils 1.00.00
     */
    public int getSize(){
        return buffer.length;
    }

    /**
     * Objects available for reading.
     *
     * @since ostermillerutils 1.00.00
     */
    private int available(){
        if (readPosition <= writePosition){
            // any space between the first read and
            // the first write is available.  In this case i
            // is all in one piece.
            return (writePosition - readPosition);
        } else {
            // space at the beginning and end.
            return (buffer.length - (readPosition - writePosition));
        }
    }

    /**
     * Create a new buffer with a default capacity and
     * given blocking behavior.
     *
     * @since ostermillerutils 1.00.00
     */
    public CircularStringBuffer(){
        this (DEFAULT_SIZE);
    }

    /**
     * Create a new buffer with the given capacity and
     * blocking behavior.
     * <p>
     * Note that the buffer may reserve some Objects for
     * special purposes and capacity number of Objects may
     * not be able to be written to the buffer.
     * <p>
     * Note that if the buffer is of INFINITE_SIZE it will
     * neither block or throw exceptions, but rather grow
     * without bound.
     *
     * @param size desired capacity of the buffer in Objects or CircularObjectBuffer.INFINITE_SIZE.
     *
     * @since ostermillerutils 1.00.00
     */
    public CircularStringBuffer(int size){
        if (size <= 0){
            buffer = new String[DEFAULT_SIZE];
        } else {
            buffer = new String[size];
        }
    }


    /**
     * Get a single Object from this buffer.  This method should be called
     * by the consumer.
     * This method will block until a Object is available or no more
     * objects are available.
     *
     * @return The Object read, or null if there are no more objects
     * @throws InterruptedException if the thread is inturrupted while waiting.
     *
     * @since ostermillerutils 1.00.00
     */
    public String read() {
        int available = available();
        if (available > 0){
        	String result = buffer[readPosition];
            readPosition++;
            if (readPosition == buffer.length){
                readPosition = 0;
            }
            return result;
        }
        return null;
    }

    /**
     * Skip Objects.  This method should be used by the consumer
     * when it does not care to examine some number of Objects.
     * This method will block until some Objects are available,
     * or there will be no more Objects available.
     *
     * @param n The number of Objects to skip
     * @return The number of Objects actually skipped
     * @throws IllegalArgumentException if n is negative.
     * @throws InterruptedException if the thread is inturrupted while waiting.
     *
     * @since ostermillerutils 1.00.00
     */
    public long skip(long n) {
        while (true){
            int available = available();
            if (available > 0){
                int length = Math.min((int)n, available);
                int firstLen = Math.min(length, buffer.length - readPosition);
                int secondLen = length - firstLen;
                if (secondLen > 0){
                    readPosition = secondLen;
                } else {
                    readPosition += length;
                }
                if (readPosition == buffer.length) {
                    readPosition = 0;
                }
                return length;
            } else {
                return 0;
            }
        }
    }
    
    /**
     * Add a single Object to this buffer.  This method should be
     * called by the producer.
     * If the buffer allows blocking writes, this method will block until
     * all the data has been written rather than throw an IOException.
     *
     * @param o Object to be written.
     * @throws BufferOverflowException if buffer does not allow blocking writes
     *   and the buffer is full.  If the exception is thrown, no data
     *   will have been written since the buffer was set to be non-blocking.
     * @throws IllegalStateException if done() has been called.
     * @throws InterruptedException if the write is interrupted.
     *
     * @since ostermillerutils 1.00.00
     */
    public void write(String o)
    {
        buffer[writePosition] = o;
        writePosition++;
        if (writePosition == buffer.length) {
            writePosition = 0;
        }
    }
    
	public boolean contains(String o)
    {
		for(int i=0;i<buffer.length;++i){
            if(o.equals(buffer[i]))
            	return true;
        }
        return false;
    }
}
