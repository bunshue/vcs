/* 
*	ARDUINO CLASS for Action Script 3 - version 0.1 - 4 Aug,2009
*  	this Actionscript class makes it easier to connect Flash to the Arduino Board (www.arduino.cc)
*   Copyright (C) 2009 motohiro, SUNOUCHI | sunouchi@withassistant.net | http://bloggers.ja.bz/sunouchi/
*   ambient label project 43d | http://www.43d.jp/
*
* 	# credits must also be given to:
*	Yaniv Steiner and the instant soup crew (instantsoup.interaction-ivrea.it) for generating the original flash client
*	beltran berrocal, 2005 - b@progetto25zero1.com - www.progetto25zero1.com
*   
*  	# you will also need the serialProxy developed by Stefano Busti(1999) and David A. Mellis(2005)
*   that can be found either on the Arduino Site (www.arduino.cc) or redistributed with this example (see update url)
*
*---------------------------------------------------------------
*
*   # METHODS & DESCRIPTIONS
*
*	@@ CONSTRUCTOR
*	@@ creates the Arduino Object inside Flash 
*				usage:
*						var portNumber   = 5333;		//read the serialProxy documentation to understand this
*						var hostIpAdress = "127.0.0.1"; //optional it deafaults to this
*						var ArduinoInstance:Arduino = new Arduino(portNumber, hostIpAdress);
*	
*	@@ CONNECT
*	@@ connects to the XMLSocket server, you must have provided a port and a host adress via the constructor
*				usage:
*						ArduinoInstance.connect()
*	
*	@@ DISCONNECT
*	@@ disconnects from the XMLSocket server
*				usage:
*						ArduinoInstance.disconnect()
*	
*	@@ SEND
*	@@ sends data to Arduino via the XMLSocket server(the serialProxy)
*				usage:
*						ArduinoInstance.send("some data here");
*	
*	## EVENT: ArduinoEvent.ON_RECEIVE_DATA
*	## event that is dispatched when data is sent from Arduino through the XMLSocket server(the serial Proxy)
*				usage:
*						var a:Arduino = new Arduino();
*						a.addEventListener(ArduinoEvent.ON_RECEIVE_DATA, getParam);
*						a.connect();
*
*						function getParam(e:ArduinoEvent):void
*						{
*							trace(e.data);
*						}
*						
*	## OTHER EVENTS: onConnect,  onConnectError,  onDisconnect
*				usage: use in the same way as the ArduinoEvent.ON_RECEIVE_DATA event
*
*-----------------------------------------------------------------------------
*	LICENCE
*   Copyright (C) 2009 motohiro, SUNOUCHI | sunouchi@withassistant.net | http://bloggers.ja.bz/sunouchi/
*   ambient label project 43d | http://www.43d.jp/
*
*   This library is free software; you can redistribute it and/or modify it 
*	under the terms of the GNU Lesser General Public License 
*	as published by the Free Software Foundation; either version 2.1 of the License
*	
*   You should have received a copy of the GNU Lesser General Public License along with this library;
*   Alternatively you can find it here http://www.gnu.org/licenses/lgpl.html
*    
*   Brief Explanation of the Licence:
*   - you can you use, redistribute, modify this software for free,
*	- you can put it into commercial projects
*   - but if you modify/enhance this Library you should release it under the same licence or alternatively under the GPL licence
*   - in all cases you should also credit the original author and all contributors
*
* 
*-----------------------------------------------------------------------------
*/

package org.p43d.arduino
{
	import flash.net.XMLSocket;
	import flash.events.*;
	import flash.utils.ByteArray;

	public class Arduino extends EventDispatcher
	{
		private var _socket:XMLSocket;
		private var _connected:Boolean = false;	// is connected?
		private var _host:String = "127.0.0.1"; // Host name or IP address
		private var _port:uint = 5331			// read the config file of the socket server for this one
			
		//constructor - provide a port number and a host ip adress
		//read the documentation of the SerialProxy to better understandwhat this means
		public function Arduino(port:uint = 0, host:String = null)
		{
			super();

			//check if the selected port is correct or set default
			if(port == 0) {
				trace("** Arduino ** default port:"+_port+" initialized! to change it use new Arduino(onPortNumber)")
			} else if ((_port < 1024) || (_port > 65535)) {
				trace("** Arduino ** Port must be from 1024 to 65535 ! read the Flash Documentation and the serProxy config file to better understand")		
			} else {
				_port = port;
			}
			
			//check for host or set default
			if(host != null) {
				_host = host;
			}			
		}
		
		//---------------------------------------
		//	CONNECT and DISCONNECT + handlers
		//---------------------------------------
		
		public function connect():void
		{
			trace("** Arduino ** 連線到 " + _host + ":" + _port + " . . .");

			_socket = new XMLSocket();			
			_socket.addEventListener(Event.CONNECT, onConnectToSocket);
			_socket.addEventListener(Event.CLOSE, onDisconnectSocket);
			_socket.addEventListener(IOErrorEvent.IO_ERROR, onConnectError);
			_socket.addEventListener(DataEvent.DATA, onDataReceived);
			
			_socket.connect(_host, _port);
		}
		
		public function disconnect():void
		{
			if (_connected)	{
				trace("** Arduino ** 中斷連線");
				_socket.close();
				_connected = false;
			}
		}
		
		private function onConnectToSocket(succeeded:Boolean):void
		{
			if (succeeded) {
				_connected = true;
				//launch event
				trace ("** Arduino ** 建立連線。")
				dispatchEvent(new ArduinoEvent(ArduinoEvent.ON_CONNECT, null));
			} else {
				trace ("** Arduino ** 連線失敗！請先啟動serProxy程式");
				dispatchEvent(new ArduinoEvent(ArduinoEvent.ON_CONNECT_ERROR, null));
			}
		}
		
		private function onConnectError(e:IOErrorEvent):void
		{
			trace ("** Arduino ** 連線失敗！")
			_connected = false;
			dispatchEvent(new ArduinoEvent(ArduinoEvent.ON_CONNECT_ERROR, null));
		}

		private function onDisconnectSocket(e:Event):void
		{
			_connected = false;
			trace ("** Arduino ** onDisconnectSocket ** 遠端伺服器中斷連線。");
			dispatchEvent(new ArduinoEvent(ArduinoEvent.ON_CLOSE, null));;
		}		

		//---------------------------------------
		//	SEND and receive data from server
		//---------------------------------------
	
		//sends data to arduino
		public function send(dataStr:String):void
		{
			if (_connected) {
				if (dataStr.length) {
					_socket.send(dataStr);
					dispatchEvent(new ArduinoEvent(ArduinoEvent.ON_SEND_DATA, dataStr));
				}
			}			
		}
		
		private function onDataReceived(e:DataEvent):void
		{
			dispatchEvent(new ArduinoEvent(ArduinoEvent.ON_RECEIVE_DATA, e.data));
		}
	}
}