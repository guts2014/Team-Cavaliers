package com.estimote.hereiam;

import java.io.IOException;
import java.util.List;
import java.util.concurrent.TimeUnit;

import org.apache.http.HttpResponse;
import org.apache.http.HttpStatus;
import org.apache.http.StatusLine;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;

import com.estimote.hereiam.R;
import com.estimote.sdk.Beacon;
import com.estimote.sdk.BeaconManager;
import com.estimote.sdk.Region;
import com.estimote.sdk.BeaconManager.MonitoringListener;

import android.app.Activity;
import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.telephony.TelephonyManager;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;

public class StudentActivity extends Activity
{
	private static final String TAG = StudentActivity.class.getSimpleName();
	private static final int NOTIFICATION_ID = 123;
	private BeaconManager beaconManager;
	private NotificationManager notificationManager;
	private Region region;
	private Context context;
	private String deviceId;

	@Override
	protected void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_student);
		
//		Beacon beacon = getIntent().getParcelableExtra(
//				ListBeaconsActivity.EXTRAS_BEACON);
//		region = new Region("regionId", beacon.getProximityUUID(),
//				beacon.getMajor(), beacon.getMinor());
//		notificationManager = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
//		beaconManager = new BeaconManager(this);
//
//		// Default values are 5s of scanning and 25s of waiting time to save CPU
//		// cycles.
//		// In order for this demo to be more responsive and immediate we lower
//		// down those values.
//		beaconManager.setBackgroundScanPeriod(TimeUnit.SECONDS.toMillis(1), 0);
//
//		beaconManager.setMonitoringListener(new MonitoringListener() {
//			@Override
//			public void onEnteredRegion(Region region, List<Beacon> beacons) {
//				postNotification("Entered region");
//				TelephonyManager tm = (TelephonyManager) context.getSystemService(TELEPHONY_SERVICE);
//				deviceId = tm.getDeviceId();
//			}
//
//			@Override
//			public void onExitedRegion(Region region) {
//				postNotification("Exited region");
//			}
//		});
		
		Button HereIAm = (Button) findViewById(R.id.hereIamButton);
		HereIAm.setOnClickListener(
			new OnClickListener()
			{
				@Override
				public void onClick(View arg0)
				{
					connectToServer();
				}
	        }
		);
	}
	
//	private void postNotification(String msg)
//	{
//		Intent notifyIntent = new Intent(StudentActivity.this,
//				StudentActivity.class);
//		notifyIntent.setFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP);
//		PendingIntent pendingIntent = PendingIntent.getActivities(
//				StudentActivity.this, 0, new Intent[] { notifyIntent },
//				PendingIntent.FLAG_UPDATE_CURRENT);
//		Notification notification = new Notification.Builder(
//				StudentActivity.this).setSmallIcon(R.drawab+le.beacon_gray)
//				.setContentTitle("Notify Demo").setContentText(msg)
//				.setAutoCancel(true).setContentIntent(pendingIntent).build();
//		notification.defaults |= Notification.DEFAULT_SOUND;
//		notification.defaults |= Notification.DEFAULT_LIGHTS;
//		notificationManager.notify(NOTIFICATION_ID, notification);
//
//		TextView statusTextView = (TextView) findViewById(R.id.status);
//		statusTextView.setText(msg);
//	}

	@Override
	protected void onDestroy()
	{
		super.onDestroy();
	}
	
	private void connectToServer()
	{
		String DEVICE_ID = deviceId;
		HttpClient httpclient = new DefaultHttpClient();
		HttpResponse response;
		try 
		{
			response = httpclient.execute(new HttpGet("http://hereiam.cjc.scot/register/cs1p/" + DEVICE_ID));
			StatusLine statusLine = response.getStatusLine();
			if(statusLine.getStatusCode() == HttpStatus.SC_OK)
			{
				 // THEY HAVE SIGNED IN SUCCESSFULLY
			}
			else 
			{
				 // THEY FAILED TO SIGN IN
			}
		} 
		catch (ClientProtocolException e)
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		catch (IOException e)
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
}