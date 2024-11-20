from typing import Optional


class TreeStore:
    def __init__(self, items: list[dict]):
        self.__items: list[dict] = items
        self.__id_and_item: dict = {item['id']: item for item in items}
        self.__children: dict = {}
        self.__get_children(self.__items)

    def __get_children(self, items: list[dict]) -> None:
        for item in items:
            parent_id = item['parent']
            if parent_id not in self.__children:
                self.__children[parent_id] = []
            self.__children[parent_id].append(item)

    def getAll(self) -> list[dict]:
        return self.__items

    def getItem(self, id: int) -> Optional[dict]:
        return self.__id_and_item.get(id, None)

    def getChildren(self, id: int) -> list[dict]:
        return self.__children.get(id, [])

    def getAllParents(self, id: int) -> list[dict]:
        parents: list = []
        current_id: int = id

        while current_id != 'root':
            current_item: Optional[int] = self.__id_and_item.get(
                current_id, None)
            if current_item is None:
                break
            current_id: int = current_item['parent']
            if current_item['id'] == id:
                continue
            parents.append(current_item)

        return parents


if __name__ == '__main__':
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]
    tree_store = TreeStore(items)
    print(f'{tree_store.getAll()=}')
    print(f'{tree_store.getItem(7)=}')
    print(f'{tree_store.getChildren(4)=}')
    print(f'{tree_store.getChildren(5)=}')
    print(f'{tree_store.getAllParents(7)=}')
