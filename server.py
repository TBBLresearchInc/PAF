import web

urls = ("/(.*)/", "Index",
        "/py/json", "Json",)


class Index:
    def GET(self, name):
        if not name:
            name = "World"
        return "Home Page"

class Json:
    def GET(self):
        user_data = web.input(id = "no data")
        return user_data.id

    def POST(self):
        data = web.input()
        print(data["row"])
        print(data["column"])
        print(data["content"])
        return "row : " + data["row"] + " , column : " + data["column"] + ", content : " + data["content"]




if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()
