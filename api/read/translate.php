<?php
require_once '../config/db_connect.php';

$response = array();

if(isset($_GET['id'])){
    $id = $_GET['id'];

    $query = "SELECT translation, phrase_usage FROM phrases WHERE id = '". $id ."'";

    $result = mysqli_query($link, $query) or die(mysqli_error());

    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)){
            $response['translation'] = $row['translation'];
            $response['usage'] = $row['phrase_usage'];
        }

        $response['success'] = 1;
    }
    else{
        $response['success'] = 1;
    }
}
else{
    $response['success'] = 0;
}

echo json_encode($response);
?>