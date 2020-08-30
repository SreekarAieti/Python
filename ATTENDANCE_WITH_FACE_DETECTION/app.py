from root_views.authView import AuthView, Register_page
class MyApp:
    def run(self):
        av = AuthView()
        av.load()

app = MyApp()
app.run()
