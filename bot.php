<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $message = $_POST['message'];

    // Process the message and generate a response
    $response = getBotResponse($message);

    // Return the response
    echo $response;
}

function getBotResponse($message) {
    $diseaseInfo = [
        'COVID-19' => 'COVID-19 is a highly contagious respiratory illness caused by the novel coronavirus. Symptoms include fever, cough, and difficulty breathing. It can spread through respiratory droplets.',
        'Influenza' => 'Influenza, commonly known as the flu, is a contagious respiratory illness caused by influenza viruses. Symptoms include fever, chills, cough, sore throat, muscle aches, and fatigue.',
        'Measles' => 'Measles is a highly contagious viral infection. Symptoms include high fever, cough, runny nose, red, watery eyes, and a rash. It spreads through respiratory droplets.',
        // Add more diseases and their information here
    ];

    $response = '';

    if (isset($diseaseInfo[$message])) {
        $response = $diseaseInfo[$message];
    } else {
$response = "I am sorry, I don't have information about that disease. Please ask about another disease.";

    }

    return $response;
}
?>
