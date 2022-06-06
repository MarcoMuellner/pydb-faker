from typing import Dict, List, Optional

_engine = None


def init_engine(db_url : str):
    pass

def get_engine():
    return _engine


def add_schema(schema_name: str, rows: int, random_foreign_keys: bool = True,
               specific_foreign_keys: Optional[Dict[str, List[int]]] = None):
    pass


def generate_data():
    pass
