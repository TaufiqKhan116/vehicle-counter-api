class MakeUrl:
    def invoke(self, protocol, host, path):
        relative_path = '/media/' + path.split('/media/')[1]
        return f"{protocol}://{host}{relative_path}"