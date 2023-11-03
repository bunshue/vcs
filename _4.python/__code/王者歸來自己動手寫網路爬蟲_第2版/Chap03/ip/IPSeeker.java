package ip;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.ByteOrder;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.log4j.Level;

public class IPSeeker {
	//�¯uIP��Ʈw�W
	private String IP_FILE="QQWry.Dat";
	//�x�s���ɮק�
	private String INSTALL_DIR="c:\\qqwry";
	
	
	// �@�ǩT�w�`�ơA�Ҧp�O�����׵���
	private static final int IP_RECORD_LENGTH = 7;
	private static final byte REDIRECT_MODE_1 = 0x01;
	private static final byte REDIRECT_MODE_2 = 0x02;
	
	// �ΨӰ���cache�A�d�ߤ@��ip�ɭ����˵�cache�A�H��֤����n�����ƴM��
	private Map<String, IPLocation> ipCache;
	// �H���ɮצs����
	private RandomAccessFile ipFile;
	// �O����M�g�ɮ�
	private MappedByteBuffer mbb;
	// �_�l�a�Ϫ��}�l�M���������ﰾ��
	private long ipBegin, ipEnd;
	// �����@�Ĳv�ӱĥΪ��{���ܼ�
	private IPLocation loc;
	private byte[] buf;
	private byte[] b4;
	private byte[] b3;
	
	public IPSeeker(String fileName,String dir)  {
		this.INSTALL_DIR=dir;
		this.IP_FILE=fileName;
		ipCache = new HashMap<String, IPLocation>();
		loc = new IPLocation();
		buf = new byte[100];
		b4 = new byte[4];
		b3 = new byte[3];
		try {
			ipFile = new RandomAccessFile(IP_FILE, "r");
		} catch (FileNotFoundException e) {
			// �p�G�䤣��o���ɮסA�A���զA�ثe�ؿ��U�j���A�o��������Τp�g�ɮצW
			//     �]�����Ǩt�Υi��Ϥ��j�p�g�ɭP�䤣��ip�a�}��T�ɮ�
			String filename = new File(IP_FILE).getName().toLowerCase();
			File[] files = new File(INSTALL_DIR).listFiles();
			for(int i = 0; i < files.length; i++) {
				if(files[i].isFile()) {
					if(files[i].getName().toLowerCase().equals(filename)) {
						try {
							ipFile = new RandomAccessFile(files[i], "r");
						} catch (FileNotFoundException e1) {
							LogFactory.log("IP�a�}��T�ɮרS�����AIP��ܥ\��N�L�k�ϥ�",Level.ERROR,e1);
							ipFile = null;
						}
						break;
					}
				}
			}
		} 
		// �p�G�}���ɮצ��\�AŪ���ɮ��Y��T
		if(ipFile != null) {
			try {
				ipBegin = readLong4(0);
				ipEnd = readLong4(4);
				if(ipBegin == -1 || ipEnd == -1) {
					ipFile.close();
					ipFile = null;
				}			
			} catch (IOException e) {
				LogFactory.log("IP�a�}��T�ɮ׮榡�����~�AIP��ܥ\��N�L�k�ϥ�",Level.ERROR,e);
				ipFile = null;
			}			
		}
	}
	
	
	/**
	 * ���w�@�Ӧa�I���������W�r�A�o��@�t�C�]�ts�l�r�ꪺIP�d��O��
	 * @param s �a�I�l�r��
	 * @return �]�tIPEntry������List
	 */
	public List getIPEntriesDebug(String s) {
	    List<IPEntry> ret = new ArrayList<IPEntry>();
	    long endOffset = ipEnd + 4;
	    for(long offset = ipBegin + 4; offset <= endOffset; offset += IP_RECORD_LENGTH) {
	        // Ū������IP����
	        long temp = readLong3(offset);
	        // �p�Gtemp������-1�AŪ��IP���a�I��T
	        if(temp != -1) {
	            IPLocation ipLoc = getIPLocation(temp);
	            // �P�_�O�_�o�Ӧa�I�̭��]�t�Fs�l�r��A�p�G�]�t�F�A�W�[�o�ӰO����List���A�p�G�S���A�~��
	            if(ipLoc.getCountry().indexOf(s) != -1 || ipLoc.getArea().indexOf(s) != -1) {
	                IPEntry entry = new IPEntry();
	                entry.country = ipLoc.getCountry();
	                entry.area = ipLoc.getArea();
	                // �o��_�lIP
	    	        readIP(offset - 4, b4);
	                entry.beginIp = Util.getIpStringFromBytes(b4);
	                // �o�쵲��IP
	                readIP(temp, b4);
	                entry.endIp = Util.getIpStringFromBytes(b4);
	                // �W�[�ӰO��
	                ret.add(entry);
	            }
	        }
	    }
	    return ret;
	}
	
	public IPLocation getIPLocation(String ip){
		IPLocation location=new IPLocation();
		location.setArea(this.getArea(ip));
		location.setCountry(this.getCountry(ip));
		return location;
	}
	
	/**
	 * ���w�@�Ӧa�I���������W�r�A�o��@�t�C�]�ts�l�r�ꪺIP�d��O��
	 * @param s �a�I�l�r��
	 * @return �]�tIPEntry������List
	 */
	public List<IPEntry> getIPEntries(String s) {
	    List<IPEntry> ret = new ArrayList<IPEntry>();
	    try {
	        // �M�gIP��T�ɮר�O���餤
	        if(mbb == null) {
			    FileChannel fc = ipFile.getChannel();
	            mbb = fc.map(FileChannel.MapMode.READ_ONLY, 0, ipFile.length());
	            mbb.order(ByteOrder.LITTLE_ENDIAN);	            
	        }
            
		    int endOffset = (int)ipEnd;
            for(int offset = (int)ipBegin + 4; offset <= endOffset; offset += IP_RECORD_LENGTH) {
                int temp = readInt3(offset);
                if(temp != -1) {
    	            IPLocation ipLoc = getIPLocation(temp);
    	            // �P�_�O�_�o�Ӧa�I�̭��]�t�Fs�l�r��A�p�G�]�t�F�A�W�[�o�ӰO����List���A�p�G�S���A�~��
    	            if(ipLoc.getCountry().indexOf(s) != -1 || ipLoc.getArea().indexOf(s) != -1) {
    	                IPEntry entry = new IPEntry();
    	                entry.country = ipLoc.getCountry();
    	                entry.area = ipLoc.getArea();
    	                // �o��_�lIP
    	    	        readIP(offset - 4, b4);
    	                entry.beginIp = Util.getIpStringFromBytes(b4);
    	                // �o�쵲��IP
    	                readIP(temp, b4);
    	                entry.endIp = Util.getIpStringFromBytes(b4);
    	                // �W�[�ӰO��
    	                ret.add(entry);
    	            }
                }
            }           
        } catch (IOException e) {
            LogFactory.log("",Level.ERROR,e);
        }
        return ret;
	}

	/**
	 * �q�O����M�g�ɮת�offset��m�}�l��3�Ӧr�`Ū���@��int
	 * @param offset
	 * @return
	 */
	private int readInt3(int offset) {
	    mbb.position(offset);
	    return mbb.getInt() & 0x00FFFFFF;
	}

	/**
	 * �q�O����M�g�ɮת��ثe��m�}�l��3�Ӧr�`Ū���@��int
	 * @return
	 */
	private int readInt3() {
	    return mbb.getInt() & 0x00FFFFFF;
	}
	
	/**
	 * �ھ�IP�o���a�W
	 * @param ip ip���r�`�}�C�Φ�
	 * @return ��a�W�r��
	 */
	public String getCountry(byte[] ip) {
		// �ˬdip�a�}�ɮ׬O�_���`
		if(ipFile == null) 
			return Message.bad_ip_file;
		// �x�sip�A�ഫip�r�`�}�C���r��Φ�
		String ipStr = Util.getIpStringFromBytes(ip);
		// ���ˬdcache���O�_�w�g�]�t���o��ip�����G�A�S���A�j���ɮ�
		if(ipCache.containsKey(ipStr)) {
			IPLocation ipLoc = ipCache.get(ipStr);
			return ipLoc.getCountry();
		} else {
			IPLocation ipLoc = getIPLocation(ip);
			ipCache.put(ipStr, ipLoc.getCopy());
			return ipLoc.getCountry();
		}
	}
	
	/**
	 * �ھ�IP�o���a�W
	 * @param ip IP���r��Φ�
	 * @return ��a�W�r��
	 */
	public String getCountry(String ip) {
	    return getCountry(Util.getIpByteArrayFromString(ip));
	}
	
	/**
	 * �ھ�IP�o��a�ϦW
	 * @param ip ip���r�`�}�C�Φ�
	 * @return �a�ϦW�r��
	 */
	public String getArea(byte[] ip) {
		// �ˬdip�a�}�ɮ׬O�_���`
		if(ipFile == null) 
			return Message.bad_ip_file;
		// �x�sip�A�ഫip�r�`�}�C���r��Φ�
		String ipStr = Util.getIpStringFromBytes(ip);
		// ���ˬdcache���O�_�w�g�]�t���o��ip�����G�A�S���A�j���ɮ�
		if(ipCache.containsKey(ipStr)) {
			IPLocation ipLoc = ipCache.get(ipStr);
			return ipLoc.getArea();
		} else {
			IPLocation ipLoc = getIPLocation(ip);
			ipCache.put(ipStr, ipLoc.getCopy());
			return ipLoc.getArea();
		}
	}
	
	/**
	 * �ھ�IP�o��a�ϦW
	 * @param ip IP���r��Φ�
	 * @return �a�ϦW�r��
	 */
	public String getArea(String ip) {
	    return getArea(Util.getIpByteArrayFromString(ip));
	}
	
	/**
	 * �ھ�ip�j��ip��T�ɮסA�o��IPLocation���c�A�ҷj����ip�ѼƱq������ip���o��
	 * @param ip �n�d�ߪ�IP
	 * @return IPLocation���c
	 */
	private IPLocation getIPLocation(byte[] ip) {
		IPLocation info = null;
		long offset = locateIP(ip);
		if(offset != -1)
			info = getIPLocation(offset);
		if(info == null) {
			info = new IPLocation();
			info.setCountry (  Message.unknown_country);
			info.setArea(Message.unknown_area);
		}
		return info;
	}	

	/**
	 * �qoffset��mŪ��4�Ӧr�`���@��long�A�]��java��big-endian�榡�A�ҥH�S��k
	 * �ΤF�o��@�Ө�ƨӰ��ഫ
	 * @param offset
	 * @return Ū����long�ȡA�Ǧ^-1���Ū���ɮץ���
	 */
	private long readLong4(long offset) {
		long ret = 0;
		try {
			ipFile.seek(offset);
			ret |= (ipFile.readByte() & 0xFF);
			ret |= ((ipFile.readByte() << 8) & 0xFF00);
			ret |= ((ipFile.readByte() << 16) & 0xFF0000);
			ret |= ((ipFile.readByte() << 24) & 0xFF000000);
			return ret;
		} catch (IOException e) {
			return -1;
		}
	}

	/**
	 * �qoffset��mŪ��3�Ӧr�`���@��long�A�]��java��big-endian�榡�A�ҥH�S��k
	 * �ΤF�o��@�Ө�ƨӰ��ഫ
	 * @param offset ��ƪ��_�l����
	 * @return Ū����long�ȡA�Ǧ^-1���Ū���ɮץ���
	 */
	private long readLong3(long offset) {
		long ret = 0;
		try {
			ipFile.seek(offset);
			ipFile.readFully(b3);
			ret |= (b3[0] & 0xFF);
			ret |= ((b3[1] << 8) & 0xFF00);
			ret |= ((b3[2] << 16) & 0xFF0000);
			return ret;
		} catch (IOException e) {
			return -1;
		}
	}	
	
	/**
	 * �q�ثe��mŪ��3�Ӧr�`�ഫ��long
	 * @return Ū����long�ȡA�Ǧ^-1���Ū���ɮץ���
	 */
	private long readLong3() {
		long ret = 0;
		try {
			ipFile.readFully(b3);
			ret |= (b3[0] & 0xFF);
			ret |= ((b3[1] << 8) & 0xFF00);
			ret |= ((b3[2] << 16) & 0xFF0000);
			return ret;
		} catch (IOException e) {
			return -1;
		}
	}
  
	/**
	 * �qoffset��mŪ���|�Ӧr�`��ip�a�}��Jip�}�C���AŪ���᪺ip��big-endian�榡�A���O
	 * �ɮפ��Olittle-endian�Φ��A�N�|�i���ഫ
	 * @param offset
	 * @param ip
	 */
	private void readIP(long offset, byte[] ip) {
		try {
			ipFile.seek(offset);
			ipFile.readFully(ip);
			byte temp = ip[0];
			ip[0] = ip[3];
			ip[3] = temp;
			temp = ip[1];
			ip[1] = ip[2];
			ip[2] = temp;
		} catch (IOException e) {
		    LogFactory.log("",Level.ERROR,e);
		}
	}
	
	/**
	 * �qoffset��mŪ���|�Ӧr�`��ip�a�}��Jip�}�C���AŪ���᪺ip��big-endian�榡�A���O
	 * �ɮפ��Olittle-endian�Φ��A�N�|�i���ഫ
	 * @param offset
	 * @param ip
	 */
	private void readIP(int offset, byte[] ip) {
	    mbb.position(offset);
	    mbb.get(ip);
		byte temp = ip[0];
		ip[0] = ip[3];
		ip[3] = temp;
		temp = ip[1];
		ip[1] = ip[2];
		ip[2] = temp;
	}
	
	/**
	 * ��������ip�MbeginIp����A�`�N�o��beginIp�Obig-endian��
	 * @param ip �n�d�ߪ�IP
	 * @param beginIp �M�Q�d��IP�ۤ����IP
	 * @return �۵��Ǧ^0�Aip�j��beginIp�h�Ǧ^1�A�p��Ǧ^-1�C
	 */
	private int compareIP(byte[] ip, byte[] beginIp) {
		for(int i = 0; i < 4; i++) {
			int r = compareByte(ip[i], beginIp[i]);
			if(r != 0)
				return r;
		}
		return 0;
	}
	
	/**
	 * ����byte��@�L�Ÿ��ƶi����
	 * @param b1
	 * @param b2
	 * @return �Yb1�j��b2�h�Ǧ^1�A�۵��Ǧ^0�A�p��Ǧ^-1
	 */
	private int compareByte(byte b1, byte b2) {
		if((b1 & 0xFF) > (b2 & 0xFF)) // ����O�_�j��
			return 1;
		else if((b1 ^ b2) == 0)// �P�_�O�_�۵�
			return 0;
		else 
			return -1;
	}
	
	/**
	 * �o�Ӥ�k�N�ھ�ip�����e�A�w���]�t�o��ip��a�a�Ϫ��O���B�A�Ǧ^�@�ӵ��ﰾ��
	 * ��k�ϥΤG���k�M��C
	 * @param ip �n�d�ߪ�IP
	 * @return �p�G���F�A�Ǧ^����IP�������A�p�G�S�����A�Ǧ^-1
	 */
	private long locateIP(byte[] ip) {
		long m = 0;
		int r;
		// ����Ĥ@��ip��
		readIP(ipBegin, b4);
		r = compareIP(ip, b4);
		if(r == 0) return ipBegin;
		else if(r < 0) return -1;
		// �}�l�G���j��
		for(long i = ipBegin, j = ipEnd; i < j; ) {
			m = getMiddleOffset(i, j);
			readIP(m, b4);
			r = compareIP(ip, b4);
			// log.debug(Utils.getIpStringFromBytes(b));
			if(r > 0)
				i = m;
			else if(r < 0) {
				if(m == j) {
					j -= IP_RECORD_LENGTH;
					m = j;
				} else 
					j = m;
			} else
				return readLong3(m + 4);
		}
		// �p�G�`�������F�A����i�Mj���w�O�۵����A�o�ӰO�����̥i�઺�O���A���O�ëD
		//     �֩w�N�O�A�٭n�ˬd�@�U�A�p�G�O�A�N�Ǧ^�����a�}�Ϫ����ﰾ��
		m = readLong3(m + 4);
		readIP(m, b4);
		r = compareIP(ip, b4);
		if(r <= 0) return m;
		else return -1;
	}
	
	/**
	 * �o��begin�����Mend����������m�O��������
	 * @param begin
	 * @param end
	 * @return
	 */
	private long getMiddleOffset(long begin, long end) {
		long records = (end - begin) / IP_RECORD_LENGTH;
		records >>= 1;
		if(records == 0) records = 1;
		return begin + records * IP_RECORD_LENGTH;
	}
	
	/**
	 * ���w�@��ip��a�a�ϰO���������A�Ǧ^�@��IPLocation���c
	 * @param offset ��a�O�����_�l����
	 * @return IPLocation�ﹳ
	 */
	private IPLocation getIPLocation(long offset) {
		try {
			// ���L4�r�`ip
			ipFile.seek(offset + 4);
			// Ū���Ĥ@�Ӧr�`�P�_�O�_�лx�r�`
			byte b = ipFile.readByte();
			if(b == REDIRECT_MODE_1) {
				// Ū����a����
				long countryOffset = readLong3();
				// ���D�ܰ����B
				ipFile.seek(countryOffset);
				// �A�ˬd�@���лx�r�`�A�]���o�ӮɭԳo�Ӧa�褴�M�i��O�ӭ��s�ɦV
				b = ipFile.readByte();
				if(b == REDIRECT_MODE_2) {
					loc.setCountry (  readString(readLong3()));
					ipFile.seek(countryOffset + 4);
				} else
					loc.setCountry ( readString(countryOffset));
				// Ū���a�ϼлx
				loc.setArea( readArea(ipFile.getFilePointer()));
			} else if(b == REDIRECT_MODE_2) {
				loc.setCountry ( readString(readLong3()));
				loc.setArea( readArea(offset + 8));
			} else {
				loc.setCountry (  readString(ipFile.getFilePointer() - 1));
				loc.setArea( readArea(ipFile.getFilePointer()));
			}
			return loc;
		} catch (IOException e) {
			return null;
		}
	}	
	
	/**
	 * ���w�@��ip��a�a�ϰO���������A�Ǧ^�@��IPLocation���c�A����k���λP�O����M�g�ɮפ覡
	 * @param offset ��a�O�����_�l����
	 * @return IPLocation�ﹳ
	 */
	private IPLocation getIPLocation(int offset) {
		// ���L4�r�`ip
	    mbb.position(offset + 4);
		// Ū���Ĥ@�Ӧr�`�P�_�O�_�лx�r�`
		byte b = mbb.get();
		if(b == REDIRECT_MODE_1) {
			// Ū����a����
			int countryOffset = readInt3();
			// ���D�ܰ����B
			mbb.position(countryOffset);
			// �A�ˬd�@���лx�r�`�A�]���o�ӮɭԳo�Ӧa�褴�M�i��O�ӭ��s�ɦV
			b = mbb.get();
			if(b == REDIRECT_MODE_2) {
				loc.setCountry (  readString(readInt3()));
				mbb.position(countryOffset + 4);
			} else
				loc.setCountry (  readString(countryOffset));
			// Ū���a�ϼлx
			loc.setArea(readArea(mbb.position()));
		} else if(b == REDIRECT_MODE_2) {
			loc.setCountry ( readString(readInt3()));
			loc.setArea(readArea(offset + 8));
		} else {
			loc.setCountry (  readString(mbb.position() - 1));
			loc.setArea(readArea(mbb.position()));
		}
		return loc;
	}
	
	/**
	 * �qoffset�����}�l�ѪR�᭱���r�`�AŪ�X�@�Ӧa�ϦW
	 * @param offset �a�ϰO�����_�l����
	 * @return �a�ϦW�r��
	 * @throws IOException
	 */
	private String readArea(long offset) throws IOException {
		ipFile.seek(offset);
		byte b = ipFile.readByte();
		if(b == REDIRECT_MODE_1 || b == REDIRECT_MODE_2) {
			long areaOffset = readLong3(offset + 1);
			if(areaOffset == 0)
				return Message.unknown_area;
			else
				return readString(areaOffset);
		} else
			return readString(offset);
	}
	
	/**
	 * @param offset �a�ϰO�����_�l����
	 * @return �a�ϦW�r��
	 */
	private String readArea(int offset) {
		mbb.position(offset);
		byte b = mbb.get();
		if(b == REDIRECT_MODE_1 || b == REDIRECT_MODE_2) {
			int areaOffset = readInt3();
			if(areaOffset == 0)
				return Message.unknown_area;
			else
				return readString(areaOffset);
		} else
			return readString(offset);
	}
	
	/**
	 * �qoffset�����BŪ���@�ӥH0�������r��
	 * @param offset �r��_�l����
	 * @return Ū�����r��A�X���Ǧ^�Ŧr��
	 */
	private String readString(long offset) {
		try {
			ipFile.seek(offset);
			int i;
			for(i = 0, buf[i] = ipFile.readByte(); buf[i] != 0; buf[++i] = ipFile.readByte());
			if(i != 0) 
			    return Util.getString(buf, 0, i, "GBK");
		} catch (IOException e) {			
		    LogFactory.log("",Level.ERROR,e);
		}
		return "";
	}
	
	/**
	 * �q�O����M�g�ɮת�offset��m�o��@��0�����r��
	 * @param offset �r��_�l����
	 * @return Ū�����r��A�X���Ǧ^�Ŧr��
	 */
	private String readString(int offset) {
	    try {
			mbb.position(offset);
			int i;
			for(i = 0, buf[i] = mbb.get(); buf[i] != 0; buf[++i] = mbb.get());
			if(i != 0) 
			    return Util.getString(buf, 0, i, "GBK");       
	    } catch (IllegalArgumentException e) {
	        LogFactory.log("",Level.ERROR,e);
	    }
	    return "";	 
	}
}
