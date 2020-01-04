import boto3
rds = boto3.client('rds', region_name="eu-west-2")

# try:
#     dbs = rds.describe_db_instances()
#     for db in dbs['DBInstances']:
#         print("{}@{}:{} {}".format(db['MasterUsername'], db['Endpoint']['Address'], db['Endpoint']['Port'], db['DBInstanceStatus']))
# except Exception as e:
#     raise e

# print("\n\r Create Database Instance")

response = rds.create_db_instance(
    DBInstanceIdentifier="newdb",
    MasterUsername="youtube",
    MasterUserPassword="abcdef1234",
    DBInstanceClass="db.t2.micro",
    Engine="mysql",
    AllocatedStorage=5
)