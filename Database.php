<?php


class Database
{
    private $server;
    private $user;
    private $password;
    private $database;

    private $conn;

    /**
     * Database constructor.
     *
     * @param $server
     * @param $user
     * @param $password
     * @param $database
     *
     * @throws ConnectionException
     */
    public function __construct($server, $user, $password, $database)
    {
        $this->server = $server;
        $this->user = $user;
        $this->password = $password;
        $this->database = $database;

        $conn = new mysqli($this->server, $this->user, $this->password, $this->database);

        if ($conn->connect_error)
            throw new ConnectionException($conn->connect_error);
    }

}