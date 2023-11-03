package test.com.lietu.filter;

import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.Date;
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.GregorianCalendar;
import java.util.Properties;

public class TestContent {

	/**
	 * @param args
	 * @throws SQLException 
	 * @throws IOException 
	 * @throws ClassNotFoundException 
	 * @throws IllegalAccessException 
	 * @throws InstantiationException 
	 */
	public static void main(String[] args) throws InstantiationException, IllegalAccessException, ClassNotFoundException, IOException, SQLException {
		new TestContent();
	}
	
	public TestContent() throws InstantiationException, IllegalAccessException, ClassNotFoundException, IOException, SQLException
	{
        Properties props = new Properties();
        InputStream is = getClass().getResourceAsStream("/database.properties");
        props.load(is);
		is.close();
		
		String driver = props.getProperty("driver");
		System.out.println("driver:"+driver);
		String url = props.getProperty("url");
		System.out.println("url:"+url);
		
		String user = props.getProperty("user");
		System.out.println("user:"+user);
		
		String password = props.getProperty("password");
		System.out.println("password:"+password);
		
		Driver drv = (Driver)Class.forName(driver).newInstance();
		DriverManager.registerDriver(drv);
		Connection con = DriverManager.getConnection(url,user,password);

		String sql = "select content from  spider";
		PreparedStatement stmt = con.prepareStatement(sql);

    	ResultSet rs = stmt.executeQuery();
    	
    	while(rs.next())
    	{
    		System.out.println(rs.getString("content"));
    	}//while1 end !!! 
    	rs.close();
    	stmt.close();
    	con.close();
	}

}
