import psycopg2 as psycopg2

# curd
conni = psycopg2.connect(host="localhost", dbname="TestDB", user="postgres", password="piyush@123", port="5555")
print(conni)

# table crateion
query = """CREATE TABLE Arijit (name TEXT)"""

# single insertion
quertI = """INSERT INTO Arijit VALUES('Software')"""

# bulk insert
queryInsert = """INSERT INTO Arijit (name) VALUES('Software'),('hindi'),('english')"""

# update
queryUPDATE = """UPDATE Arijit SET name = 'ipad' WHERE name = 'hindi'"""

# delete
queryDELETE = """DELETE FROM Arijit WHERE name = 'Software'"""

# cur = conni.cursor()
# cur.execute(query)
# cur.close()
# conni.commit()

# retrive
queryGET = """SELECT * from Arijit"""


# cur = conni.cursor()
# cur.execute(query)
# output = cur.fetchall()
# for item in output:
#     print(item[0])
# cur.close()
# conni.commit()
#

# create a table

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE parts (
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE part_drawings (
                part_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vendor_parts (
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id , part_id),
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    conn = None
    try:
        # read the connection parameters
        # connect to the PostgreSQL server
        conn = psycopg2.connect(host="localhost", dbname="TestDB", user="postgres", password="piyush@123", port="5555")

        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# create_tables()



def executeAndCommit(Q):
    cur = conni.cursor()
    cur.execute(Q)
    conni.commit()
    rows = cur.fetchall()
    for row in rows:
        print(row[0])
    cur.close()


#
# def deleteTable(tableName):
#     deleteQuery = """DROP TABLE Alexa"""
#     cur = conni.cursor()
#     cur.execute(deleteQuery)
#     conni.commit()
#     cur.close()


def getAllTableData():
    pickQuery = """SELECT name,gg FROM wow"""
    # executeAndCommit(pickQuery)
    cur = conni.cursor()
    cur.execute(pickQuery)
    conni.commit()
    rows = cur.fetchall()
    for row in rows:
        print(row)
        print(row[0])
        # print(row[1])
        print("---------------")

    cur.close()


def instertIntoTable():
    instertQuery = """INSERT INTO wow VALUES ('s','g')"""
    cur = conni.cursor()
    result = cur.execute(instertQuery)
    print("(1)insert result is " + str(result))
    conni.commit()
    print("insert result is " + str(result))


# deleteTable("Alexa")
getAllTableData()
instertIntoTable()
