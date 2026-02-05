web335DB> load("C:/Users/Amanda/web-335-master/week_4/users.js")
true
web335DB> db.users.find({})
[
  {
    _id: ObjectId('6983eb5bd09c89f5f7628ca0'),
    firstName: 'Johann',
    lastName: 'Bach',
    employeeId: '1007',
    email: 'jbach@me.com',
    dateCreated: ISODate('2026-02-05T00:59:07.821Z')
  },
  {
    _id: ObjectId('6983eb5bd09c89f5f7628ca1'),
    firstName: 'Ludwig',
    lastName: 'Beethoven',
    employeeId: '1008',
    email: 'lbeethoven@me.com',
    dateCreated: ISODate('2026-02-05T00:59:07.821Z')
  },
  {
    _id: ObjectId('6983eb5bd09c89f5f7628ca2'),
    firstName: 'Wolfgang',
    lastName: 'Mozart',
    employeeId: '1009',
    email: 'wmozart@me.com',
    dateCreated: ISODate('2026-02-05T00:59:07.821Z')
  },
  {
    _id: ObjectId('6983eb5bd09c89f5f7628ca3'),
    firstName: 'Johannes',
    lastName: 'Brahms',
    employeeId: '1010',
    email: 'jbrahms@me.com',
    dateCreated: ISODate('2026-02-05T00:59:07.821Z')
  },
  {
    _id: ObjectId('6983eb5bd09c89f5f7628ca4'),
    firstName: 'Richard',
    lastName: 'Wagner',
    employeeId: '1011',
    email: 'rwagner@me.com',
    dateCreated: ISODate('2026-02-05T00:59:07.822Z')
  },
  {
    _id: ObjectId('6983eb5bd09c89f5f7628ca5'),
    firstName: 'Claude',
    lastName: 'Debussy',
    employeeId: '1012',
    email: 'cdebussy@me.com',
    dateCreated: ISODate('2026-02-05T00:59:07.822Z')
  }
]
web335DB> db.users.find({ employeeId: "1010" })

web335DB> // Display the user with email jbach@me.com

web335DB> db.users.find({ email: "jbach@me.com" })
[
  {
    _id: ObjectId('6983eb5bd09c89f5f7628ca0'),
    firstName: 'Johann',
    lastName: 'Bach',
    employeeId: '1007',
    email: 'jbach@me.com',
    dateCreated: ISODate('2026-02-05T00:59:07.821Z')
  }
]
web335DB>

web335DB> // Display the user with last name Mozart

web335DB> db.users.find({ lastName: "Mozart" })
[
  {
    _id: ObjectId('6983eb5bd09c89f5f7628ca2'),
    firstName: 'Wolfgang',
    lastName: 'Mozart',
    employeeId: '1009',
    email: 'wmozart@me.com',
    dateCreated: ISODate('2026-02-05T00:59:07.821Z')
  }
]
web335DB>

web335DB> // Display the user with first name Richard

web335DB> db.users.find({ firstName: "Richard" })
[
  {
    _id: ObjectId('6983eb5bd09c89f5f7628ca4'),
    firstName: 'Richard',
    lastName: 'Wagner',
    employeeId: '1011',
    email: 'rwagner@me.com',
    dateCreated: ISODate('2026-02-05T00:59:07.822Z')
  }
]
web335DB>

web335DB> // Display the user with employeeId "1010"

web335DB> db.users.find({ employeeId: "1010" })