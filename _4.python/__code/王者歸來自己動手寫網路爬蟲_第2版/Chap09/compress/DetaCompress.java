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
		byte[] buf = new byte[8];// �s�W�@��byte�}�C
		for (int i = buf.length - 1; i >= 0; i--) {
			buf[i] = (byte) (n & 0x00000000000000ff);// ���C8�쪺��
			n >>>= 8;// �k��8��
		}
		return buf;
	}

	// ��@��long������ƶi�����Y
	public static void writeVLong(long i, BufferedOutputStream dos)
			throws IOException {
		while ((i & ~0x7F) != 0) {
			dos.write((byte) ((i & 0x7f) | 0x80)); // �g�J�C��r�`
			i >>>= 7; // �k��7��
		}

		dos.write((byte) i);
		// System.out.println((byte)i+"    �g�J�C��r�`");

	}

	// ��@�����Y�᪺long�������Ū���X��
	static long readVLong(DataInputStream dis) throws IOException {
		byte b = dis.readByte(); // Ū�J�@�Ӧr�`
		int i = b & 0x7F; // ���C7�쪺��
		// �C�Ӱ��쪺�r�`�h����2��7����A�]�N�O128
		for (int shift = 7; (b & 0x80) != 0; shift += 7) {
			if (dis.available() != 0) {
				b = dis.readByte();
				i |= (b & 0x7F) << shift; // �ثe�r�`��ܪ��쭼2��shift����
			}
		}
		return i;// �Ǧ^�̲׵��Gi
	}

	// ��long���}�CsimHashSet�g�JfileName���w���ɮפ��h
	static int write(long[] simHashSet, String fileName) {
		int j = 0;
		try {
			BufferedOutputStream dos = new BufferedOutputStream(
					new FileOutputStream(fileName));
			byte[] b = longToBytes(simHashSet[0]);// �}�C���Ĥ@�ӼƦr�@���ഫ���G�i��
			dos.write(b);// �⥦�g���ɮפ�
			for (int i = 1; i < simHashSet.length; i++) {
				long lo = simHashSet[i] - simHashSet[i - 1];// �Τ@���ܼưO���}�C����@�Ӽƴ�e�@�Ӽƪ��t
				writeVLong(lo, dos);// ��o�Ӯt�ȼg�J�ɮ�
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

	// �qfileName���w���ɮפ���long���}�C�g�X��
	static long[] read(int len, String fileName) {
		try {
			DataInputStream dis = new DataInputStream(new BufferedInputStream(
					new FileInputStream(fileName)));
			long[] simHashSet = new long[len];
			simHashSet[0] = dis.readLong();// �q�ɮ�Ū���Ĥ@��long���Ʀr��J�}�C
			for (int i = 1; i < len; i++) {
				simHashSet[i] = readVLong(dis);// Ū���ɮ׳ѤU������
				simHashSet[i] = simHashSet[i] + simHashSet[i - 1];  // �N�������ܦ��}�C��@�ӼƩM�e�@�ӼƦr���M
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
