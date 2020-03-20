<?php
require_once '../config/db_connect.php';

$response = array();

$query = "SELECT id, geordie FROM phrases";

$result = mysqli_query($link, $query) or die(mysqli_error());

if(mysqli_num_rows($result) > 0){
    $response['phrases'] = array();
    while($row = mysqli_fetch_array($result)){
        $phrase = array(
            "id" => $row['id'],
            "geordie" => $row['geordie']
        );

        $response['phrases'][] = $phrase;
    }

    $response['success'] = 1;
}
else{
    $response['success'] = 0;
}

echo json_encode($response);
?>