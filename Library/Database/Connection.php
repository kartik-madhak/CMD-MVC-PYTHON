<?php

class Connection
{
    private $conn;

    /**
     * Database constructor.
     *
     *
     * @param Config $config
     *
     * @throws ConnectionException
     */
    public function __construct(Config $config)
    {
        $conn = new mysqli($config->host, $config->user, $config->pass, $config->dbname);

        if ($conn->connect_error) {
            throw new ConnectionException($conn->connect_error);
        }
    }


}
