package com.bitmechanic.spindle;

import java.util.ArrayList;

/** struct class to store results and total count.  
 * listlib's ListContainer isn't used here just in case someone is using
 * this library without listlib.jar in their CLASSPATH
 */
public class ListDesc {
    public ArrayList list;
    public int count;
}
