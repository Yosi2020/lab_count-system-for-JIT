<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "btest";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

echo "Live and the value is writen";

while (true) {

	$myFile = "t.txt";
	$fh = fopen($myFile, 'r');
	$theData = fread($fh, 5);
	fclose($fh);



	$sql = "UPDATE btest SET Text = ($theData) WHERE Id = 1 ";


    if ($conn->query($sql) === TRUE) {
  	
  	 usleep(0.1 * 1000000);
     
	} else {
	  echo "Error: " . $sql . "<br>" . $conn->error;
	}

    }


$conn->close();
?>