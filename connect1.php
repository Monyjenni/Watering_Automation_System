
<html>
<body>

<?php

$dbname = 'example';
$dbuser = 'root';
$dbpass = '';
$dbhost = 'localhost';

$connect = @mysqli_connect($dbhost,$dbuser,$dbname,$dbpass);

if(!$connect){
 echo "Error: " . mysqli_connect_error();
 exit();   
}
echo "Connection Success!<br><br>";

$b1 = $_GET["Wet or Dry"];

$query = "INSERT INTO iot_watering_automation(Moisture) VALUES('$Moisture')";
result = mysqli_query($connect,$query);

echo "Insertion Success! <br>";

?>
</body>
</html>