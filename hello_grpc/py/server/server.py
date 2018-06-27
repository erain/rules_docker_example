import grpc
import time

from concurrent import futures
from hello_grpc.proto import simple_pb2
from hello_grpc.proto import simple_pb2_grpc


class _SimpeService(simple_pb2_grpc.SimpleServicer):

    def Foo(self, foo_request, context):
        foo_reply = simple_pb2.FooReply()
        foo_reply.message = 'DEMO {name}'.format(name=foo_request.name)
        return foo_reply


class _HelloServer(object):

    def __init__(self, simple_service, server_port):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        simple_pb2_grpc.add_SimpleServicer_to_server(simple_service, self.server)
        self.server.add_insecure_port('[::]:{server_port}'.format(server_port=server_port))

    def start(self):
        self.server.start()

    def stop(self):
        self.server.stop(0)

    def await_termination(self):
        try:
            while True:
                time.sleep(60 * 60)
        except KeyboardInterrupt:
            self.server.stop(0)


def main():
    hello_server = _HelloServer(_SimpeService(), 50051)
    hello_server.start()
    hello_server.await_termination()


if __name__ == "__main__":
    main()
