def calculate_love_score(name1, name2):
    names = name1.lower() + name2.lower()

    t = names.count("t")
    r = names.count("r")
    u = names.count("u")
    e = names.count("e")
    true_score = t + r + u + e

    l = names.count("l")
    o = names.count("o")
    v = names.count("v")
    e = names.count("e")
    love_score = l + o + v + e

    print(f"score: {str(true_score) + str(love_score)}")


calculate_love_score("Messi", "Kim Kardashian")
