<?php
	header('Access-Control-Allow-Origin: *');

	if (isset($_GET['type'])) {
	    $type = $_GET['type'];
	} else {
		echo 'failed';
	    return;
	}	
	if (isset($_GET['phonenumber'])) {
	    $phonenumber = $_GET['phonenumber'];
	} else {
		echo 'failed';
	    return;
	}	
	$response = array();
	$phonenumber = $_GET['phonenumber'];
	$foldername = "+1".$phonenumber;
	if($type == 0) {		
		$password = $_GET['password'];
		$latitude = $_GET['latitude'];
		$longitude = $_GET['longitude'];
		$editEstimate = $_GET['editEstimate'];
		$deliveryService = $_GET['deliveryService'];			
		
		$response['PHONE'] = '+1'.$phonenumber;
		$response['PASSWORD'] = $password;
		$response['MINIMUM_PRICE'] = (int)$editEstimate;
		$response['LOCATION_LATITUDE'] = $latitude;
		$response['LOCATION_LONGITUDE'] = $longitude;
		
	    $response['ACCESS_TOKEN'] = "ccb4aef8bf6620cb23c6516ae1381887c73f02e845600fb2e4476e7f502e62c6";
	    $response['CLIENT_ID'] = "2c34304d1ea8a8e56626e0ac8939eb486c08a9e40d0a113a95f76ec196097a47";
	    $response['CLIENT_SECRET'] = "c3e1d27a5682a614ce860fb3683cb9a6c8d7fe0e519fc1dbe2622aece2ca6658";
	    $response['KOCHAVA_DEVICE_ID'] = "KA3601571807197t2f0e32f059644f2ba020cf82441d62a4";
	    $response['REQUEST_PAUSE_TIME'] = 0.00;
	    $response['DEVICE_TOKEN'] = "dEufrctRID8:APA91bHg3I73QPT42Xms1IpWGGANUflVeu8sPzCxoAhJ0Z5K28xVCKwQPrZ_gNWNP2RXXHKhZo7uxHdH0n8QXWzOkDQkBUlXkt-zia_jExlYcUC6F5bVGfLdFHLOATkIYcBKq5v0ovdu";
	   	if($deliveryService == "Delivery only")
			$response['DELIVERY_ONLY'] = true;
		else $response['DELIVERY_ONLY'] = false;	
		$response['ZONE'] = 183;
	} else {
		$string = file_get_contents($foldername.'/settings.json');
		$response = json_decode($string, true);
		$response['REQUEST_STOP'] = true;
	}
	try {
		$fileName = $response['PHONE'].'/settings.json';
		if ( !file_exists($fileName) ) {
        	throw new Exception('File not found.');
      	}
		$fp = fopen($fileName, 'w+');
		fwrite($fp, json_encode($response));
		fclose($fp);
				
		if($type == 0) {
			//exec("START  ".$foldername."/".$phonenumber.".exe");
			//file_get_contents("http://localhost/".$foldername."/run.php?phonenumber=".$phonenumber);			
			//header('Location: '.'http://localhost/'.$foldername.'/run.php?phonenumber='.$phonenumber);		
		}
		echo 'success';
	}catch(Exception  $e){
		echo 'failed';
	}
?>