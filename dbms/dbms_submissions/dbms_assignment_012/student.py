class DoesNotExist(Exception):
	pass
class MultipleObjectsReturned(Exception):
	pass

class InvalidField(Exception):
	pass

class Student:
	def __init__(self, name, age, score):
		self.name = name
		self.student_id = None
		self.age = age
		self.score = score

	@classmethod
	def get(cls,**args): 
		
		for k,v in args.items():
			cls.key = k
			cls.value = v
			
		if cls.key not in ('student_id','name','age','score'):
			raise InvalidField('InvalidField')
			
		if cls.key == 'name':
			record = read_data(f"select * from Student where {cls.key} = \'{cls.value}\'")
		else:
			record = read_data(f"select * from Student where {cls.key} = {cls.value}")
			
		
		if len(record)==0:
			raise DoesNotExist('DoesNotExist')
		elif len(record)>1:
			raise MultipleObjectsReturned('MultipleObjectsReturned')
	
		output = Student(record[0][1],record[0][2],record[0][3])
		output.student_id = record[0][0]
		return output

	def save(self):
		import sqlite3
		connection = sqlite3.connect("students.sqlite3")
		crsr = connection.cursor() 
		crsr.execute("PRAGMA foreign_keys=on;") 
		if self.student_id == None:
			crsr.execute(f"insert into Student (name,age,score) values (\'{self.name}\',{self.age},{self.score})")        
			self.student_id = crsr.lastrowid
		else:
			data = read_data(f"select * from Student where student_id = {self.student_id}")
			if len(data) != 0:
				crsr.execute(f"update Student SET name=\'{self.name}\',age={self.age},score={self.score}")
			else:
				crsr.execute(f"insert into Student (student_id,name,age,score) values ({self.student_id},\'{self.name}\',{self.age},{self.score})")
		connection.commit()
		connection.close()
			
		

	def delete(self):
		write_data(f"delete from student where student_id={self.student_id}")
	
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor()
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans
	
	
	
#student_object.save()
# student_object = Student.get(student_id=10)

# student_object.student_id = 1
# student_object.save()
# print(student_object.name)
# print(student_object.get())