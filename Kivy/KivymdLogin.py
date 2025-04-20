from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from helper import username_helper
from helper import password_helper
#from helper import button_helper


		 
class DemoApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette="Green"
		self.theme_cls.primary_hue="A700"
		self.theme_cls.theme_style="Light"
		screen = Screen()
		
		self.username = Builder.load_string(username_helper)
		self.password = Builder.load_string(password_helper)
		#login_btn = Builder.load_string(button_helper)
		login_btn=MDRectangleFlatButton(text="Login",pos_hint={"center_x":0.5, "center_y":0.4}, on_release=self.show_data)
		screen.add_widget(self.username)
		screen.add_widget(self.password)
		screen.add_widget(login_btn)
		
		return screen
		
		
		
	def close_dialog(self,obj):
		self.dialog.dismiss()
			
			
			
	def show_data(self,obj):
		txt=""
		if self.username.text==txt:
			txt="Enter username"
		else:
			txt=f'Hello {self.username.text}'
		close_btn=MDFlatButton(text="close", on_release=self.close_dialog)
		more_btn=MDFlatButton(text="more")
		self.dialog = MDDialog(text=txt,title="Message",size=(0.8,0.6), buttons=[close_btn,more_btn])
		self.dialog.open()
		
		
DemoApp().run()
