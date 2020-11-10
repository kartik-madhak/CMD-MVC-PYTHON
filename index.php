<?php

require __DIR__ . '/vendor/autoload.php';
require_once('Database.php');

$dotEnv = \Dotenv\Dotenv::createImmutable(__DIR__);
$dotEnv->load();

echo 'testing database connection class...';

try {
    $database = new Database($_ENV['DB_HOST'], $_ENV['DB_USERNAME'], $_ENV['DB_PASSWORD'], $_ENV['DB_DATABASE']);
} catch (ConnectionException $e) {
    echo "FAILED!";
}

echo "Prob success...";