import web

urls = (
    '/py/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello motherfucking bitch, ' + name + '!'

    def POST(self, name):
        return "OKLM " + name


if __name__ == "__main__":
    app.run()
