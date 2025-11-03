import locale


locale.setlocale(locale.LC_COLLATE, 'ru_RU.UTF-8') # to sort russian letters too

def remove_and_add_hashtag(tags:tuple) -> tuple:
    """Adding a hashtag '#' to every tag"""
    remove_hash = lambda string: string.replace("#", "")
    tags = tuple(map(remove_hash, tags))
    add_hash = lambda string, begin='#': begin + string
    return tuple(map(add_hash, tags))

def join_tags(tags:tuple) -> str:
    """Joining tags together to a one string"""
    return ' '.join(tags)

def sort_tags(tags:tuple) -> tuple:
    """Sorting tags by alphabet"""
    return tuple(sorted(tags, key=str.casefold)) # key=str.casefold to sort them equally whether it's capital letter or not

# For testing purposes
def main() -> None:
    """Main function"""
    tags = map(str, "join_tags sort_tags add_hashtag".split())
    tags = sort_tags(add_hashtag(tags))
    tags_text = join_tags(tags)
    print(tags_text)


if __name__ == "__main__":
    main()