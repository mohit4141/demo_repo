package com.rbs.main;

import com.rbs.app.Application;

public class Banking {
	
	public final String strDisplayCustomerType="1. Student\n2. Senior Citizen\n3. Professional";
	public final String strBankType="1. ICICI\n2. HDFC\n3. AXIS\n4. SC";
	public final String strOptions="1. Open Account\n 2. Deposit \n 3. Withdraw\n 4. Open Fixed Deposit\n";
	Application mApplication;
	int mChoice, mBankChoice, mOperationChoice;
	public static void main(String[] args) {
		Banking mBanking = new Banking();
		mBanking.mApplication = Application.getInstance();
		mBanking.CustomerMenu(mBanking, mBanking.mApplication);
	}
	public void CustomerMenu(Banking mBanking, Application mApplication) {
		mApplication.setStatus(true);
		mApplication.displayMessage(strDisplayCustomerType);
		mChoice = mApplication.getScannerInstance().nextInt();
		if(mChoice > 0)
			mBanking.SelectBankMenu(mBanking, mBanking.mApplication);		
	}
	public void SelectBankMenu(Banking mBanking, Application Application) {
		mApplication.setStatus(true);
		mApplication.displayMessage(strBankType);
		mBankChoice = mApplication.getScannerInstance().nextInt();
		if(mBankChoice > 0)
			mBanking.SelectOperationMenu(mBanking, mBanking.mApplication);
	}
	
	public void SelectOperationMenu(Banking mBanking, Application Application) {
		mApplication.setStatus(true);
		mApplication.displayMessage(strOptions);
		mOperationChoice = mApplication.getScannerInstance().nextInt();
		
	}
	
	
	
}
