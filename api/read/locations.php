<?php
require_once '../config/db_connect.php';

$response = array();

$query = "SELECT location FROM locations";

$result = mysqli_query($link, $query) or die(mysqli_error());

if(mysqli_num_rows($result) > 0){
    $response['locations'] = array();
    while($row = mysqli_fetch_array($result)){
        $response['locations'][] = $row['location'];
    }

    $response['success'] = 1;
}
else{
    $response['success'] = 0;
}

echo json_encode($response);
?>