import zerorpc


class StreamingRPC:
    @zerorpc.stream
    def signal_stream(self, generator):
        return generator


s = zerorpc.Server(StreamingRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
