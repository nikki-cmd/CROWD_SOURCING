Это небольшой пользовательский мануал. 
Здесь вы узнаете как запустить приложение и что делать в случае ошибки импорта библиотеки.






Как запустить программу.

	
	Для этого Вам понадобится любой редактор кода для Python и немного манипуляций с установкой библиотек.


	
	
		Если у Вас Linux:

		
					Откройте консоль и поставьте все нужные зависимости

		
					Вот список команд:

			
						pip install kivy  (Для установки kivy)

			
						garden install mapview  (Для установки MapView)

			
						pip install webbrowser (Для открытия браузера)

			
						pip install psycopg2 (Для работы с БД)
		
		
					Откройте папку "CrowdSourcing_Linux" --> main.py в редакторе.
 
		
					Или же просто откройте папку с проектом в консоли и пропишите: python main.py

		
	

	

Если у Вас Windows:


					Откройте консоль и поставьте все нужные зависимости


					Вот список команд:

			
						pip install kivy  (Для установки kivy)

			
						garden install mapview  (Для установки MapView)

			
						pip install webbrowser (Для открытия браузера)

			
						pip install psycopg2 (Для работы с БД)


		
		
					Откройте папку "CrowdSourcing_Windows" --> main.py в редакторе.
 
		
					Или же просто откройте папку с проектом в консоли и пропишите: python main.py

		
		
		

				Если у Вас Android:

		
				///comming soon...///

		
				Установите CrowdSourcing.apk и запустите его как обычное приложение.






В случае, если при запуске появляется ошибка ModuleNotFoundError или ImportError проделайте следующие шаги:

	
Для Windows и для Linux решение одинаковое.

	
Пропишите в консоль pip install и название библиотеки, на которой вылетает ошибка. 
Ниже список ВСЕХ библиотек, использованных в проекте:


	
	
	Kivy


	kivy-garden.mapview
 
	
	Kivy-Garden
 
	
	mapview (в этом случае можно применить и garden install mapview)

	
	psycopg2

	
	webbrowser



		

										
				

				CrowdSourcing
	
											
					by ChinaGriB team