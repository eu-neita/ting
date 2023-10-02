def exists_word(word, instance):
    results = []

    for index in range(len(instance)):
        file_info = instance.search(index)

        lines_with_word = []
        num = enumerate(file_info["linhas_do_arquivo"], start=1)
        for line_index, line in num:
            if word.lower() in line.lower():
                lines_with_word.append({"linha": line_index})

        if lines_with_word:
            result_entry = {
                "palavra": word,
                "arquivo": file_info["nome_do_arquivo"],
                "ocorrencias": lines_with_word
            }
            results.append(result_entry)

    return results


def search_by_word(word, instance):
    results = []

    for index in range(len(instance)):
        file_info = instance.search(index)

        lines_with_word = []
        num = enumerate(file_info["linhas_do_arquivo"], start=1)
        for line_index, line in num:
            if word.lower() in line.lower():
                # paiaçada
                lines_with_word.append({"linha": line_index, "conteudo": line})

        if lines_with_word:
            result_entry = {
                "palavra": word,
                "arquivo": file_info["nome_do_arquivo"],
                "ocorrencias": lines_with_word
            }
            results.append(result_entry)

    return results
