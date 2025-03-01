# TODO ООП Ч3. Инкапсуляция. Приватные методы и атрибуты. Урок 24

# _ это protected - доступно при наследовании
# __ это private - доаступно только внутри класса

# собественные getters и  setters
# @property
# @speed.setter
# @speed.deleter

# https://pypi.org/project/tabulate/

available_formats = [
            "plain", "simple", "github", "grid", "simple_grid", 
            "rounded_grid", "heavy_grid", "mixed_grid", "double_grid", 
            "fancy_grid", "outline", "simple_outline", "rounded_outline", 
            "heavy_outline", "mixed_outline", "double_outline", 
            "fancy_outline", "pipe", "orgtbl", "asciidoc", "jira", 
            "presto", "pretty", "psql", "rst", "mediawiki", 
            "moinmoin", "youtrack", "html", "unsafehtml", 
            "latex", "latex_raw", "latex_booktabs", "latex_longtable", 
            "textile", "tsv"
        ]

from tabulate import tabulate
from typing import List, Dict, Union, Any, Optional

class TabulateTable:
    
    __awaitable_styles = [
            "plain", "simple", "github", "grid", "simple_grid", 
            "rounded_grid", "heavy_grid", "mixed_grid", "double_grid", 
            "fancy_grid", "outline", "simple_outline", "rounded_outline", 
            "heavy_outline", "mixed_outline", "double_outline", 
            "fancy_outline", "pipe", "orgtbl", "asciidoc", "jira", 
            "presto", "pretty", "psql", "rst", "mediawiki", 
            "moinmoin", "youtrack", "html", "unsafehtml", 
            "latex", "latex_raw", "latex_booktabs", "latex_longtable", 
            "textile", "tsv"
        ]
    def __init__(self):
        self.__data: Union[List[Dict[str, Any]], List[List[Any]]] = []
        self.__style: str = "pretty"
        self.__headers: Optional[List[str]] = None
        self.__tupe_data: Optional[str] = None
    
    @property
    def style(self):
        return self.__style
    
    @style.setter
    def style(self, style: str):
        if style in self.__awaitable_styles:
            self.__style = style
        else:
            raise ValueError(f"такого стиля нет. Выберите из {self.__awaitable_styles}")
    @property
    def data(self) -> List[Dict[str, Any]] | List[List[Any]]:
        return self.__data
    @data.setter
    def data(self, data: Union[List[Dict[str, Any]], List[List[Any]]]):
        self.__type_data = self.__validate_data(data)
        self.__data = data
        
    def __validate_data(self, data: Union[List[Dict[str, Any]], List[List[Any]]]):
        if isinstance(data[0], dict):
            return "dicts"
        elif isinstance(data[0], list):
            return "lists"
        else:
            raise ValueError("данные должны быть списками словарей или списками значений")
        
    def render(self) -> str:
        if self.__type_data == "dicts":
            return tabulate(self.__data, headers="keys", tablefmt=self.__style)
        elif self.__type_data == "lists":
            return tabulate(self.__data, tablefmt=self.__style)
        else:
            raise ValueError("неверные данные для рендеринга таблицы")
        
if __name__ == "__main__":
    table = TabulateTable()
    table.data = [
        {"name": "John", "age": 25},
        {"name": "Alice", "age": 30},
    ]
    table.style = "github"
    print(table.render())

    