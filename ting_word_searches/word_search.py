def ordernate(word, content, i, order):
    if word.lower() in content.lower():
        if order:
            return {"linha": i + 1, "conteudo": content}
        else:
            return {"linha": i + 1}
    return None


def exists_word(word, instance):
    result = []
    for index in range(len(instance)):
        file = instance.search(index)
        occurrences = [
            occurrencies for occurrencies in [
                ordernate(word, line, index, False)
                for index, line in enumerate(file["linhas_do_arquivo"])
            ] if occurrencies is not None
        ]
        if len(occurrences) > 0:
            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })
    return result


def search_by_word(word, instance):
    result = []
    for index in range(len(instance)):
        file = instance.search(index)
        occurrences = [
            occurrencies for occurrencies in [
                ordernate(word, line, index, True)
                for index, line in enumerate(file["linhas_do_arquivo"])
            ] if occurrencies is not None
        ]
        if len(occurrences) > 0:
            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })
    return result
