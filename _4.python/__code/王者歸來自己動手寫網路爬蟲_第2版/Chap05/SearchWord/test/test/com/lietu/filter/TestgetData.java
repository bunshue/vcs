package test.com.lietu.filter;

import java.io.InputStream;
import java.sql.Connection;
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.List;
import java.util.Properties;

import org.jdom.Document;
import org.jdom.Element;
import org.jdom.input.SAXBuilder;

public class TestgetData {

	/**
	 * @param args
	 */
	private Connection con = null;
	public TestgetData(){
		try{
			Properties properties = new Properties();
			InputStream is = this.getClass().getResourceAsStream("/mysqldb.properties");
			properties.load(is);
			is.close();
			String driver = properties.getProperty("driver");
			System.out.println(driver);
			String dburl = properties.getProperty("dburl");
			System.out.println(dburl);
			String user = properties.getProperty("user");
			System.out.println(user);
			String password = properties.getProperty("password");
			System.out.println(password);
			Driver drv = (Driver)Class.forName(driver).newInstance();
			DriverManager.registerDriver(drv);
			con = DriverManager.getConnection(dburl,user,password);			
		}catch(Exception err){err.printStackTrace();}
	}
	public void getXml(String configFile)
	{			
		try{
			String sql = "select url,type,rank from spider";
			PreparedStatement pstmt = con.prepareStatement(sql);
					
			ResultSet result = pstmt.executeQuery();			
			while (result.next()) {
				
					String url = result.getString(1);
					String type = new String(result.getString(2).getBytes("gb2312"),"ISO-8859-1");					
					String rank = result.getString(3);
					System.out.println("\nurl:"+url+"\ntype:"+type+"\nrank:"+rank);												
			}
			result.close();
			pstmt.close();
			if (con != null) {
				con.close();
				System.out.println("Close Success!");
			}	
		}catch(Exception e)
		{
			e.printStackTrace();			
		}	
			
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
