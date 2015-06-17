import web

urls = ("/(.*)/", "Index",
        "/py/hello/(.+)", "hello",
        "/py/upload", "Upload",
        "/py/json", "Json",
        "/py/julien/(.*)", 'Julien')

class Julien:
    def GET(self, name):
        if not name:
            name = "Fuck"
        return "Motherfucking Julien " + name

class Index:
    def GET(self, name):
        if not name:
            name = "World"
        return "Home Page"


class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello World ' + name

class Upload:
    def GET(self):
        return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
</body></html>"""

    def POST(self):
        x = web.input(myfile={})
        web.debug(x['myfile'].filename) # This is the filename
        web.debug(x['myfile'].value) # This is the file contents
        web.debug(x['myfile'].file.read()) # Or use a file(-like) object
        print(x)
        raise web.seeother('/py/upload')


class Json:
    def GET(self):
        user_data = web.input(id = "no data")
        return user_data.id

    def POST(self):
        data = web.input()
        print(data["content"])
        return data["content"]




if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()
