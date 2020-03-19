<?php
require_once '../config/db_config.php';

$link = mysqli_connect(DB_SERVER, DB_USER, DB_PASSWORD, DB_DATABASE) or die(mysqli_error());
?>