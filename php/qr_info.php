<?php
// select.php

if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    include_once("config.php");

    @$barcode = $_POST['barcode'];

    // if($id == '' || $name == '' || $code == '')
    // {
    //     echo json_encode(array(
    //         "status" => "false",
    //         "message" => "필수 인자가 부족합니다")
    //     );
    // }
    // else
    // {
    $query= "SELECT a.id, a.name, a.barcode, b.location FROM item_barcode a, item_location b WHERE a.barcode = '$barcode' AND a.id = b.id LIMIT 1;";
    $result= mysqli_query($con, $query);
    $emparray = array();

    if(mysqli_num_rows($result) == 1)
    {  
        while ($row = mysqli_fetch_assoc($result))
        {
            // $emparray[] = $row;
            echo json_encode(
                ($row
            ), JSON_UNESCAPED_UNICODE
        );

        }

        // echo json_encode(
        //     array(
        //         // "id" => $emparray[0],
        //         // "name" => $emparray[1],
        //         // "code" => $emparray[2]
        //         $emparray
        //     ), JSON_UNESCAPED_UNICODE
        // );
    }
    else
    {
        echo json_encode(
            array(
            "status" => "false",
            "message" => "조회 내역에 문제가 있습니다. 바코드를 확인 하세요."
            ), JSON_UNESCAPED_UNICODE
        );
    }

}
else{
    echo json_encode(
        array(
        "status" => "false",
        "message" => "호출방식 에러입니다."
        ), JSON_UNESCAPED_UNICODE
    );
}
        
mysqli_close($con);


?>