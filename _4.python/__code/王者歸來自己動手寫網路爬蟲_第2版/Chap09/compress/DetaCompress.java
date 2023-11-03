package com.test;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

public class DetaCompress {

	public static byte[] longToBytes(long n) {
		byte[] buf = new byte[8];// 新增一個byte陣列
		for (int i = buf.length - 1; i >= 0; i--) {
			buf[i] = (byte) (n & 0x00000000000000ff);// 取低8位的值
			n >>>= 8;// 右移8位
		}
		return buf;
	}

	// 把一個long型的資料進行壓縮
	public static void writeVLong(long i, BufferedOutputStream dos)
			throws IOException {
		while ((i & ~0x7F) != 0) {
			dos.write((byte) ((i & 0x7f) | 0x80)); // 寫入低位字節
			i >>>= 7; // 右移7位
		}

		dos.write((byte) i);
		// System.out.println((byte)i+"    寫入低位字節");

	}

	// 把一個壓縮後的long型的資料讀取出來
	static long readVLong(DataInputStream dis) throws IOException {
		byte b = dis.readByte(); // 讀入一個字節
		int i = b & 0x7F; // 取低7位的值
		// 每個高位的字節多乘個2的7次方，也就是128
		for (int shift = 7; (b & 0x80) != 0; shift += 7) {
			if (dis.available() != 0) {
				b = dis.readByte();
				i |= (b & 0x7F) << shift; // 目前字節表示的位乘2的shift次方
			}
		}
		return i;// 傳回最終結果i
	}

	// 把long型陣列simHashSet寫入fileName指定的檔案中去
	static int write(long[] simHashSet, String fileName) {
		int j = 0;
		try {
			BufferedOutputStream dos = new BufferedOutputStream(
					new FileOutputStream(fileName));
			byte[] b = longToBytes(simHashSet[0]);// 陣列的第一個數字一個轉換成二進位
			dos.write(b);// 把它寫到檔案中
			for (int i = 1; i < simHashSet.length; i++) {
				long lo = simHashSet[i] - simHashSet[i - 1];// 用一個變數記錄陣列中後一個數減前一個數的差
				writeVLong(lo, dos);// 把這個差值寫入檔案
			}
			dos.close();
			j = simHashSet.length;
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return j;
	}

	// 從fileName指定的檔案中把long型陣列寫出來
	static long[] read(int len, String fileName) {
		try {
			DataInputStream dis = new DataInputStream(new BufferedInputStream(
					new FileInputStream(fileName)));
			long[] simHashSet = new long[len];
			simHashSet[0] = dis.readLong();// 從檔案讀取第一個long型數字放入陣列
			for (int i = 1; i < len; i++) {
				simHashSet[i] = readVLong(dis);// 讀取檔案剩下的元素
				simHashSet[i] = simHashSet[i] + simHashSet[i - 1];  // 將元素都變成陣列後一個數和前一個數字的和
			}
			dis.close();
			
			return simHashSet;
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return null;
	}
}
