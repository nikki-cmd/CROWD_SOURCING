from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.switch import Switch
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color 
import webbrowser
import psycopg2

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '700') 

con = psycopg2.connect(dbname='d3enfqm54j94kb', user='inwklslvmbmcqu', 
	                        password='22dde5015ec39c192c4ae132802a64fb1638e8dc792dab617da66ef086cfb004',
	              			host='ec2-52-30-161-203.eu-west-1.compute.amazonaws.com')
cur = con.cursor()
def example():
	print(1)

	cur = con.cursor() 
	print(2)
	
	
	cur.execute('CREATE TABLE core_fes(ID INTEGER PRIMARY KEY, Name TEXT, Count INTEGER, Risk FLOAT)')

	print(3)

	data_arr = []
	data_Optimus = [1, "Оптимус", 0, 0]
	data_Samolet = [2, "Самолет", 0, 0]
	data_DA = [3, "ДА", 0, 0]
	data_Magnit = [4, "Магнит", 0, 0]
	data_Assorti = [5, "Ассорти", 0, 0]
	data_Lenta = [6, "Лента", 0, 0]
	data_DomSviasi = [7, "Дом связи", 0, 0]
	data_Boston = [8, "Бостон", 0, 0]
	data_Panorama = [9, "Панорама", 0, 0]
	data_Stroigrad = [10, "Стройград", 0, 0]
	data_Rim = [11, "Рим", 0, 0]
	data_Sozidatel= [12, "Созидатель", 0, 0]
	data_Akvamol = [13, "Аквамол", 0, 0]
	data_Megastroi = [14, "Мегастрой", 0, 0]
	data_Sarai = [15, "Сарай", 0, 0]
	data_VerhTerr = [16, "Верхняя терраса", 0, 0]
	data_Solnechnii = [17, "Солнечный", 0, 0]
	data_Grand = [18, "Гранд", 0, 0]
	data_Lider = [19, "Лидер", 0, 0]

	data_arr.append(data_Optimus)	
	data_arr.append(data_Samolet)
	data_arr.append(data_DA)
	data_arr.append(data_Magnit)
	data_arr.append(data_Assorti)
	data_arr.append(data_Lenta)
	data_arr.append(data_DomSviasi)
	data_arr.append(data_Boston)
	data_arr.append(data_Panorama)
	data_arr.append(data_Stroigrad)
	data_arr.append(data_Rim)
	data_arr.append(data_Sozidatel)
	data_arr.append(data_Akvamol)
	data_arr.append(data_Megastroi)
	data_arr.append(data_Sarai)
	data_arr.append(data_VerhTerr)
	data_arr.append(data_Solnechnii)
	data_arr.append(data_Grand)
	data_arr.append(data_Lider)

	for data_unit in data_arr:
		cur.execute('INSERT INTO CORE_FES VALUES(%s, %s, %s, %s)', data_unit)
	con.commit()  
	print(4)
	

#example()
def transport_base():
	print(1)

	cur = con.cursor() 
	print(2)
	
	
	cur.execute('CREATE TABLE transport_db(ID INTEGER PRIMARY KEY, Nomber INTEGER, Count INTEGER, Risk FLOAT)')

	print(3)

	data_arr = []
	data_1 = [1, 42, 0, 0]
	data_2 = [2, 28, 0, 0]
	data_3 = [3, 68, 0, 0]
	data_4 = [4, 25, 0, 0]
	data_5 = [5, 84, 0, 0]
	data_6 = [6, 96, 0, 0]
	data_7 = [7, 1, 0, 0]
	data_8 = [8, 15, 0, 0]
	data_9 = [9, 107, 0, 0]
	data_10 = [10, 11, 0, 0]
	data_11 = [11, 6, 0, 0]
	data_12 = [12, 22, 0, 0]

	data_arr.append(data_1)	
	data_arr.append(data_2)
	data_arr.append(data_3)
	data_arr.append(data_4)
	data_arr.append(data_5)
	data_arr.append(data_6)
	data_arr.append(data_7)	
	data_arr.append(data_8)
	data_arr.append(data_9)
	data_arr.append(data_10)
	data_arr.append(data_11)
	data_arr.append(data_12)
	

	for data_unit in data_arr:
		cur.execute('INSERT INTO transport_db VALUES(%s, %s, %s, %s)', data_unit)
	con.commit()  
	print(4)
	

#transport_base()
class ScreenManagement(ScreenManager):
    pass

class Menu(Screen):
	pass

class Advice(Screen):
	pass

class Map(Screen):
	def get_count(self, idi_m):
		query = "SELECT Count FROM core_fes WHERE ID = " + str(idi_m) 
		cur.execute(query)
		ind = cur.fetchone()
		arr =[]
		for index in ind:
			arr.append(index)
		return str(arr[0])
		con.commit()  
		 

class Stats(Screen):
    pass

class Stats_root(Screen):
    pass

class Map_pharmacy(Screen):
	pass

class Top(Screen):
	
	def top_1(self):
		query = "SELECT Name, Count FROM core_fes ORDER BY Count DESC"
		cur.execute(query)
		big_arr = cur.fetchall()
		ans = []
		for item in big_arr[0]:
			ans.append(item)
		return ans[0] + '------' + str(ans[1])
		con.commit()  
		
	
	def top_2(self):

		query = "SELECT Name, Count FROM core_fes ORDER BY Count DESC"
		cur.execute(query)
		big_arr = cur.fetchall()
		ans = []
		for item in big_arr[1]:
			ans.append(item)
		return ans[0] + '------' + str(ans[1])
		con.commit()  
		
	
	def top_3(self):

		query = "SELECT Name, Count FROM core_fes ORDER BY Count DESC"
		cur.execute(query)
		big_arr = cur.fetchall()
		ans = []
		for item in big_arr[2]:
			ans.append(item)
		return ans[0] + '------' + str(ans[1])
		con.commit() 


	def top_1_good(self):
		cur = con.cursor()
		query = "SELECT Name, Count FROM core_fes ORDER BY Count ASC"
		cur.execute(query)
		big_arr = cur.fetchall()
		ans = []
		for item in big_arr[0]:
			ans.append(item)
		return ans[0]
		con.commit()  
		

	
	def top_2_good(self):
		cur = con.cursor()
		query = "SELECT Name, Count FROM core_fes ORDER BY Count ASC"
		cur.execute(query)
		big_arr = cur.fetchall()
		ans = []
		for item in big_arr[1]:
			ans.append(item)
		return ans[0]
		con.commit()  
		
	
	def top_3_good(self):
		cur = con.cursor()
		query = "SELECT Name, Count FROM core_fes ORDER BY Count ASC"
		cur.execute(query)
		big_arr = cur.fetchall()
		ans = []
		for item in big_arr[2]:
			ans.append(item)
		return ans[0]
		con.commit()  
		
class Top_min(Screen):
	
	def top_1(self):
		cur = con.cursor()
		query = "SELECT Name, Count FROM core_fes ORDER BY Count ASC"
		cur.execute(query)
		big_arr = cur.fetchall()
		ans = []
		for item in big_arr[0]:
			ans.append(item)
		return ans[0] + '------' + str(ans[1])
		con.commit()  
		

	
	def top_2(self):
		cur = con.cursor()
		query = "SELECT Name, Count FROM core_fes ORDER BY Count ASC"
		cur.execute(query)
		big_arr = cur.fetchall()
		ans = []
		for item in big_arr[1]:
			ans.append(item)
		return ans[0] + '------' + str(ans[1])
		con.commit()  
		
	
	def top_3(self):
		cur = con.cursor()
		query = "SELECT Name, Count FROM core_fes ORDER BY Count ASC"
		cur.execute(query)
		big_arr = cur.fetchall()
		ans = []
		for item in big_arr[2]:
			ans.append(item)
		return ans[0] + '------' + str(ans[1])
		con.commit()  
		

class Sites(Screen):
	def open(self, url):
		webbrowser.open_new(url)


class Map_root(Screen):
	def update(self, idi):
		cur = con.cursor()
		query = "UPDATE core_fes SET Count = Count + 1 WHERE ID =" + str(idi)  
		cur.execute(query)
		con.commit()  
	

class Form(Screen):
    b = 0
    def maximum(self):
    	cur = con.cursor()
    	query = "SELECT ID, Name, Count FROM core_fes ORDER BY Count DESC"
    	cur.execute(query)
    	big_arr = cur.fetchall()
    	ans = []
    	for item in big_arr[0]:
    		ans.append(item)
    	query = "UPDATE core_fes SET Count = Count - 1 WHERE ID =" + str(ans[0])  
    	cur.execute(query)
    	con.commit() 

class Form_1(Screen):
    b_simpt = 0

class Transport_root(Screen):
	def update(self, idi):
		cur = con.cursor()
		query = "UPDATE transport_db SET Count = Count + 1 WHERE ID =" + str(idi)  
		cur.execute(query)
		con.commit() 
	def top_warn(self):
		query = "SELECT Nomber, Count FROM transport_db ORDER BY Count DESC"
		cur.execute(query)
		big_arr = cur.fetchall()
		ans = []
		for item in big_arr[0]:
			ans.append(item)
		return str(ans[0]) + '------' + str(ans[1])
		con.commit() 
	def top_warn2(self):
		query = "SELECT Nomber, Count FROM transport_db ORDER BY Count DESC"
		cur.execute(query)
		big_arr = cur.fetchall()
		ans = []
		for item in big_arr[1]:
			ans.append(item)
		return str(ans[0]) + '------' + str(ans[1])
		con.commit() 

	def top_warn3(self):
		query = "SELECT Nomber, Count FROM transport_db ORDER BY Count DESC"
		cur.execute(query)
		big_arr = cur.fetchall()
		ans = []
		for item in big_arr[2]:
			ans.append(item)
		return str(ans[0]) + '------' + str(ans[1])
		con.commit() 


class Transport_Troll_root(Screen):
 	def update(self, idi):
 		cur = con.cursor()
 		query = "UPDATE transport_db SET Count = Count + 1 WHERE ID =" + str(idi)  
 		cur.execute(query)
 		con.commit() 
 	def top_warn(self):
 		query = "SELECT Nomber, Count FROM transport_db ORDER BY Count DESC"
 		cur.execute(query)
 		big_arr = cur.fetchall()
 		ans = []
 		for item in big_arr[0]:
 			ans.append(item)
 		return str(ans[0]) + '------' + str(ans[1])
 		con.commit() 
 	def top_warn2(self):
 		query = "SELECT Nomber, Count FROM transport_db ORDER BY Count DESC"
 		cur.execute(query)
 		big_arr = cur.fetchall()
 		ans = []
 		for item in big_arr[1]:
 			ans.append(item)
 		return str(ans[0]) + '------' + str(ans[1])
 		con.commit() 
 	def top_warn3(self):
 		query = "SELECT Nomber, Count FROM transport_db ORDER BY Count DESC"
 		cur.execute(query)
 		big_arr = cur.fetchall()
 		ans = []
 		for item in big_arr[2]:
 			ans.append(item)
 		return str(ans[0]) + '------' + str(ans[1])
 		con.commit()  


class Transport(Screen):
	def top_warn(self):
		query = "SELECT Nomber, Count FROM transport_db ORDER BY Count DESC"
		cur.execute(query)
		big_arr = cur.fetchall()
		ans = []
		for item in big_arr[0]:
			ans.append(item)
		return str(ans[0]) + '------' + str(ans[1])
		con.commit() 
	def top_warn2(self):
		query = "SELECT Nomber, Count FROM transport_db ORDER BY Count DESC"
		cur.execute(query)
		big_arr = cur.fetchall()
		ans = []
		for item in big_arr[1]:
			ans.append(item)
		return str(ans[0]) + '------' + str(ans[1])
		con.commit() 

	def top_warn3(self):
		query = "SELECT Nomber, Count FROM transport_db ORDER BY Count DESC"
		cur.execute(query)
		big_arr = cur.fetchall()
		ans = []
		for item in big_arr[2]:
			ans.append(item)
		return str(ans[0]) + '------' + str(ans[1])
		con.commit()

	def select(self, idi):
		query = "SELECT Count FROM transport_db WHERE ID =" + str(idi)
		cur.execute(query)
		big_arr = cur.fetchone()
		for i in big_arr:
			return i
			con.commit() 


class Transport_Troll(Screen):
 	def update(self, idi):
 		cur = con.cursor()
 		query = "UPDATE transport_db SET Count = Count + 1 WHERE ID =" + str(idi)  
 		cur.execute(query)
 		con.commit()
 	
 	def update(self, idi):
 		cur = con.cursor()
 		query = "UPDATE transport_db SET Count = Count + 1 WHERE ID =" + str(idi)  
 		cur.execute(query)
 		con.commit() 
 	
 	def top_warn(self):
 		query = "SELECT Nomber, Count FROM transport_db ORDER BY Count DESC"
 		cur.execute(query)
 		big_arr = cur.fetchall()
 		ans = []
 		for item in big_arr[0]:
 			ans.append(item)
 		return str(ans[0]) + '------' + str(ans[1])
 		con.commit() 
 	
 	def top_warn2(self):
 		query = "SELECT Nomber, Count FROM transport_db ORDER BY Count DESC"
 		cur.execute(query)
 		big_arr = cur.fetchall()
 		ans = []
 		for item in big_arr[1]:
 			ans.append(item)
 		return str(ans[0]) + '------' + str(ans[1])
 		con.commit() 
 	
 	def top_warn3(self):
 		query = "SELECT Nomber, Count FROM transport_db ORDER BY Count DESC"
 		cur.execute(query)
 		big_arr = cur.fetchall()
 		ans = []
 		for item in big_arr[2]:
 			ans.append(item)
 		return str(ans[0]) + '------' + str(ans[1])
 		con.commit()

 	def select(self, idi):
 		query = "SELECT Count FROM transport_db WHERE ID =" + str(idi)
 		cur.execute(query)
 		big_arr = cur.fetchone()
 		for i in big_arr:
 			return i
 		con.commit()

class MainApp(App):
	def build(self):
		return ScreenManagement()

MainApp().run()
