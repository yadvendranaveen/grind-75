from dataclasses import dataclass, field

@dataclass
class FilePath:
    children: defaultdict[str, "FilePath"] = field(default_factory=lambda: defaultdict(FilePath))
    content: str = ""
    is_file: bool = False

class FileSystem:

    def __init__(self):
        self.root = FilePath()

    def _traverse_to_dir(self, path:str):
        if path =='/':  
            return (path, self.root)
        queue = path[1:].split('/')
        curr = self.root
        while queue:
            name = queue.pop(0)
            curr = curr.children[name]
        return (name, curr)

    def ls(self, path: str) -> List[str]:
        name, curr = self._traverse_to_dir(path)
        return [name] if curr.is_file else sorted(list(curr.children.keys()))


    def mkdir(self, path: str) -> None:
        self._traverse_to_dir(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        name,curr = self._traverse_to_dir(filePath)
        curr.is_file = True
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        name,curr = self._traverse_to_dir(filePath)
        return curr.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)