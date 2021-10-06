from mongoengine import connect
from mongoengine.document import Document
from mongoengine.fields import BooleanField, ReferenceField, StringField

connect(db='python_course')

class User(Document):
  meta={'collection':'users'}
  first_name=StringField(min_length=2,max_length=15,required=True)
  last_name=StringField(min_length=2,max_length=15)


class Todo(Document):
  meta={"collection":"todos"}
  title=StringField(regex=r"\w{3,20}")
  completed=BooleanField(default=False)
  user=ReferenceField('User')


ada = User(first_name='Ada', last_name='Byron')
ada.save()

todo1 = Todo(
  title="Todo1",
  user=ada
)

todo1.save()