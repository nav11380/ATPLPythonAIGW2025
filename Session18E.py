"""
    MySQL Introduction

    1. Database
        Its a collection of tables
    2. Table
        Its a collection of rows(records)

    ORM: Object Relational Mapping

    Class Name i.e. Object Type -> Table Name
    Visitor: serial_no, date_time_stamp, name, phone, address, whome_to_meet, purpose
    Attributes of an Object -> Mapped as Column Names for Table

    MySQL: Commands

    show databases; (show all the databases in MySQL)
    create database dbName; (Create a new database by the name dbName)
    use dbName; (Select the database in which you want to work)

    class Visitor:

        def __init__(self, serial_no=None, 
                    name=None, 
                    phone=None, 
                    address=None, 
                    whome_to_meet=None, 
                    purpose=None):
            self.serial_no = serial_no
            self.name = name
            self.phone = phone
            self.address = address
            self.whome_to_meet = whome_to_meet
            self.purpose = purpose

            # Automatically pickup the date time stamp
            self.date_time_stamp = str`(datetime.datetime.now())

    show tables; (show the tables in database)

    (create a table in database)
    create table Visitor(
        serial_no int primary key auto_increment,
        name varchar(256),
        phone varchar(16),
        address text,
        whome_to_meet varchar(256),
        purpose text,
        date_time_stamp datetime
    );

    (show the table details - column names and types)
    (describe tableName;)
    describe Visitor;

    (show all rows of table)
    (select * from tableName;)
    select * from Visitor;

    (delete the table)
    (drop table tableName;)
    drop table Visitor;

    Add/Create a row in Table
    insert into Visitor values(null, 'John', '+91 99999 11111', 'Redwood Shores', 'Fionna', 'Web Dev', '2025-07-11');
    insert into Visitor values(null, 'George', '+91 99999 22222', 'Redwood Shores', 'Fionna', 'App Dev', '2025-07-12');

    (Delete a row/record from Table)
    delete from Visitor where serial_no = 1;

    (Update a record in table)
    update Visitor set name='John Watson', address='Country Homes' where serial_no = 1;
"""