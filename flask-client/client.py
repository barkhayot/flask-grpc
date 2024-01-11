from flask import Flask, jsonify
import grpc
import books_pb2
import books_pb2_grpc

app = Flask(__name__)

@app.route('/api/books', methods=['GET'])
def get_books():
    try:
        # Make gRPC call to the BookService
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = books_pb2_grpc.BookServiceStub(channel)
            grpc_request = books_pb2.GetBooksRequest()
            grpc_response = stub.GetBooks(grpc_request)

        # Process gRPC response and return to the Flask app
        books_data = [{'id': book.id, 'title': book.title, 'author': book.author} for book in grpc_response.books]
        return jsonify({'books': books_data})
    except Exception as e:
        return jsonify({'message': f"Error: {e}"})
if __name__ == '__main__':
    app.run(debug=True)
