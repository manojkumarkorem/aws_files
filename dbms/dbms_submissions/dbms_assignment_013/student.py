class DoesNotExist(Exception):
	pass
class MultipleObjectsReturned(Exception):
	pass

class InvalidField(Exception):
	pass

class Student:
	#constructor
	def __init__(self, name, age, score):
		self.name = name
		self.student_id = None
		self.age = age
		self.score = score
    
	def __repr__(self):
		return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            self.student_id,
            self.name,
            self.age,
            self.score)
    
    #get_method        
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
	
		Temp = Student(record[0][1],record[0][2],record[0][3])
		Temp.student_id = record[0][0]
		return Temp
	
	#save_method
	def save(self):
		import sqlite3
		connection = sqlite3.connect("selected_students.sqlite3")
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
	
	#delete_method
	def delete(self):
		write_data(f"delete from student where student_id={self.student_id}")
	
	
	#filter_method
	@classmethod
	def filter(cls, **data):
		cls.details=[]
		cls.operator={'lt':'<', 'lte':'<=', 'gt':'>', 'gte':'>=', 'neq':'!=', 'in':'in','contain':''}

		if(len(data)) >= 1:
			temp = []
			for ke,val in data.items():
				cls.key = ke
				cls.value = val
				
				fields = cls.key
				fields = fields.split('__')
				
				if fields[0] not in ('name','age','score','student_id'):
					raise InvalidField 
				
				
				
				if(len(fields)) == 1:
					query = " {} ='{}'".format(cls.key, cls.value)
				elif fields[1] == 'contains':
					query = " {} like '%{}%'".format(fields[0],cls.value)
				elif fields[1] == 'in':
					query = " {} {} {}".format(fields[0],cls.operator[fields[1]],tuple(cls.value))
				else:
					query = "{} {} '{}'".format(fields[0],cls.operator[fields[1]],cls.value)
		
				temp.append(query)
			
			additinal_operation = " and ".join(tuple(temp))       
			query = "select * from student where " + additinal_operation
			
		
		Temp_data = read_data(query)
		
		for _ in range(len(Temp_data)):
			Temp = Student(Temp_data[_][1], Temp_data[_][2], Temp_data[_][3])
			Temp.student_id = Temp_data[_][0]
			cls.details.append(Temp)
		return cls.details
	
#write_data_method		
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

#read_data_method
def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor()
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans


# student_object = Student(name="Maude Vanhorne", age=23, score=89)
# student_object.save()
# student_object = Student(name="Sarah Kirwan", age=34, score=44)
# student_object.save()
# student_object = Student(name="Fletcher Lomago", age=40, score=7)
# student_object.save()
# student_object = Student(name="Jesse Couch", age=34, score=62)
# student_object.save()
# student_object = Student(name="Israel Gilliland", age=38, score=77)
# student_object.save()
# student_object = Student(name="Michael Aguas", age=34, score=87) 
# student_object.save()

# selected_students = Student.filter(age = 40,score = 7)
# print(selected_students)
# ages = [25, 34]
# selected_students = Student.filter(age__in=ages)
# print(selected_students)
# selected_students = Student.filter(age__in = [25, 34], score__lt=50)
# print(selected_students)