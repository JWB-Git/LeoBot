<?php
require_once '../config/db_connect.php';

$response = array();

if(isset($_POST['person'])){
    $query = "INSERT INTO team_party_ring (person) VALUES (?)";
    $stmt = $link->prepare($query);
    $stmt->bind_param("s", $_POST['person']);
    if($stmt->execute()){
        $response['success'] = 1;
    }
    else{
        $response['success'] = 0;
    }
}
else{
    $response['success'] = 0;
}

echo json_encode($response);
?>