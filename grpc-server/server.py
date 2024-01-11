import grpc
from concurrent import futures
import books_pb2
import books_pb2_grpc

class BookService(books_pb2_grpc.BookServiceServicer):
    def GetBooks(self, request, context):
        # Simulate fetching books from a database or external service
        books = [
            books_pb2.Book(id="1", title="Book 1", author="Author 1"),
            books_pb2.Book(id="2", title="Book 2", author="Author 2"),
            # Add more books as needed
        ]

        return books_pb2.GetBooksResponse(books=books)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    books_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC Server started. Listening on port 50051...")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
