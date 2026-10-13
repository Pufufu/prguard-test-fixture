def get_item(items, index):
    """Return the item, or None when the index is outside the list."""
    if 0 <= index <= len(items):
        return items[index]
    return None
