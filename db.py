from proga import db
from proga import Item

db.create_all()
text1 = Item(id = 1, user_id = '1', text = 'user1text1')
text2 = Item(id = 2, user_id = '1', text = 'user1text2')
text3 = Item(id = 3, user_id = '2', text = 'user2text1')
text4 = Item(id = 4, user_id = '2', text = 'user2text2')
db.session.add(text1)
db.session.add(text2)
db.session.add(text3)
db.session.add(text4)
db.session.commit()