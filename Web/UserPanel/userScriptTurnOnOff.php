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
		
		$string = file_get_contents($foldername.'/settings.json');
		$response = json_decode($string, true);
		
		$response['PHONE'] = '+1'.$phonenumber;
		$response['PASSWORD'] = $password;
		$response['MINIMUM_PRICE'] = (int)$editEstimate;
		$response['LOCATION_LATITUDE'] = $latitude;
		$response['LOCATION_LONGITUDE'] = $longitude;
	   	$response['DELIVERY_SERVICE'] = $deliveryService;
	   	$response['REQUEST_STOP'] = false;
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