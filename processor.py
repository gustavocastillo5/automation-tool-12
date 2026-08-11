from typing import List, Dict


def process_data(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Processes a list of dictionaries and returns the modified list.

    Args:
        data (List[Dict[str, str]]): A list of dictionaries containing data to process.

    Returns:
        List[Dict[str, str]]: A modified list of dictionaries after processing.
    """
    processed_data = []
    for item in data:
        processed_item = {"id": item.get("id"), "processed": item.get("value", "").upper()}
        processed_data.append(processed_item)
    return processed_data


def filter_data(data: List[Dict[str, str]], threshold: int) -> List[Dict[str, str]]:
    """Filters data based on a threshold value.

    Args:
        data (List[Dict[str, str]]): A list of dictionaries to filter.
        threshold (int): The threshold value for filtering.

    Returns:
        List[Dict[str, str]]: A list of filtered dictionaries.
    """
    return [item for item in data if int(item.get("value", 0)) > threshold


if __name__ == "__main__":
    example_data = [{"id": "1", "value": "5"}, {"id": "2", "value": "10"}]
    processed = process_data(example_data)
    filtered = filter_data(processed, 6)
    print(filtered)  
