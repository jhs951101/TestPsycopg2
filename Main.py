import PostgreSQLController;

dbController = PostgreSQLController.PostgreSQLController()
dbController.connect()

result = dbController.executeQuery('SELECT * FROM testtable')

if result is not None:
    for i in range(len(result)):
        print(result[i][0], result[i][1], result[i][2])
else:
    print('Error')

dbController.disconnect()