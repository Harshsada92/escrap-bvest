<?php
	$email = $_POST['email'];
	$password = $_POST['password'];
	// Database connection
	$conn = new mysqli('localhost','root','','harsh');
	if($conn->connect_error){
		echo "$conn->connect_error";
		die("Connection Failed : ". $conn->connect_error);
	} else {
		$stmt = $conn->prepare("insert into register(email, password) values(?, ?)");
		$stmt->bind_param("ss", $email, $password,);
   $stmt->execute();
		echo $execval;
		echo "Registration successfully...";
		$stmt->close();
		$conn->close();
	}
?>