package com.rbs.app;

import java.util.Scanner;

public class Application {
	static Application mApplication;
	boolean status;
	Scanner mScanner;
	public boolean isStatus() {
		return status;
	}
	public void setStatus(boolean status) {
		this.status = status;
	}
	public static Application getInstance() {
		if(mApplication == null)
			return mApplication = new Application();
		else
			return mApplication;
	}
	public Scanner getScannerInstance() {
		if(mScanner == null)
			return mScanner = new Scanner(System.in);
		else
			return mScanner;
	}
	public void displayMessage(String strMessage) {
		if(status)
			System.out.println(strMessage);
	}

}
