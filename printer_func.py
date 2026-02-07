from attribute_rect import block

def printer(blocks_list):
    if blocks_list:
        # Handle both block objects and integers (block_ids)
        ids = ', '.join(str(item.block_id if hasattr(item, 'block_id') else item) for item in blocks_list)
        print(f"{{{ids}}}")
    else:
        print("{}")


def print_set(s):
    if s:
        formatted_sets = ['{' + ', '.join(str(item) for item in x) + '}' for x in s]
        print('{' + ', '.join(formatted_sets) + '}')
    else:
        print("{}")