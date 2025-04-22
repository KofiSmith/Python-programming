username_helper="""
MDTextField:
	pos_hint: {"center_x":0.5, "center_y":0.6}
	
	size_hint_x: None
	width: 500	
	hint_text: "Enter username"
	icon_left: "account"
	icon_left_color:app.theme_cls.primary_color
	
"""

password_helper="""
MDTextField:
	pos_hint: {"center_x":0.5, "center_y":0.5}
	
	size_hint_x: None
	width: 500	
	hint_text: "Enter password"
	helper_text: "Or click on forgot password"
	helper_text_mode: "on_focus"
	icon_left: "lock"
	icon_left_color:app.theme_cls.primary_color
	
"""
button_helper="""
MDRectangleFlatButton:
	text: "login"
	pos_hint: {"center_x":0.5, "center_y":0.4}
	on_release:self.show_data
"""
