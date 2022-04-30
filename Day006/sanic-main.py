from sanic import Sanic
from sanic.response import json

app = Sanic("library")


@app.route('/')
async def test(request):
    return json({'hello': 'world'})

@app.route('/books', methods=['GET'])
async def get_book(request):
    return json({'status': 'books'})

@app.route('/books', methods=['POST'])
async def add_book(request):
    return json({'status': 'ok'})

if __name__ == '__main__':
    app.run()
