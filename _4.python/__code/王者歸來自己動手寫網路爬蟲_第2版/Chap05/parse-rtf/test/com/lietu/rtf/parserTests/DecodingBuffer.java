package com.lietu.rtf.parserTests;

import com.lietu.rtf.parser.MemoryStream;

public class DecodingBuffer {

	/**
	 * @param args
	 * @throws Exception 
	 */
	public static void main(String[] args) throws Exception {
		MemoryStream hexDecodingBuffer = new MemoryStream(10);
		int decodedByte = 203;
		hexDecodingBuffer.WriteByte( (byte)decodedByte );
		System.out.println(hexDecodingBuffer.ToArray());
	}

}
